
"""
AI-F-001 공공데이터 전처리.

원천:
ai.dataset
ai.dataset_record

데이터셋:
job_context_public v0.2

데이터베이스 수정 없이 조회 및 전처리만 수행한다.
"""

import json
import re
import unicodedata

import pandas as pd
from sqlalchemy import text


DATASET_NAME = "job_context_public"
DATASET_VERSION = "v0.2"

EXPECTED_COUNTS = {
    "PUB-001": 19,
    "PUB-002A": 340,
    "PUB-002B": 3935,
    "PUB-003": 1485,
}


def normalize_text(value):
    """공백·유니코드 정규화."""

    if value is None or pd.isna(value):
        return None

    value = unicodedata.normalize(
        "NFKC", str(value)
    )

    value = re.sub(r"\s+", " ", value).strip()

    return value or None


def normalize_code(value):
    """문자열 코드 정규화. 선행 0 유지."""

    if value is None or pd.isna(value):
        return None

    value = str(value).strip()

    if re.fullmatch(r"\d+\.0", value):
        value = value[:-2]

    return value or None


def parse_features(value):
    """PostgreSQL JSONB → Python dict."""

    if isinstance(value, dict):
        return value

    if isinstance(value, str):
        value = json.loads(value)

        if isinstance(value, dict):
            return value

    raise ValueError(
        "features는 JSON 객체여야 합니다."
    )


def load_job_context(engine):
    """DB에서 실제 적재 데이터를 조회."""

    sql = text("""
        SELECT
            r.record_id,
            r.source_record_key,
            r.features
        FROM ai.dataset_record r
        JOIN ai.dataset d
          ON d.dataset_id = r.dataset_id
        WHERE d.feature_code = 'AI-F-001'
          AND d.dataset_name = :name
          AND d.dataset_version = :version
        ORDER BY r.record_id
    """)

    with engine.connect() as conn:
        df = pd.read_sql_query(
            sql,
            conn,
            params={
                "name": DATASET_NAME,
                "version": DATASET_VERSION,
            },
        )

    if df.empty:
        raise RuntimeError(
            "AI-F-001 공공데이터가 없습니다."
        )

    return df


def prepare_job_context(df):
    """기능별 원본 컬럼을 표준 구조로 변환."""

    rows = []

    for _, record in df.iterrows():
        f = parse_features(record["features"])

        raw = f.get("raw_attributes") or {}

        if not isinstance(raw, dict):
            raw = {}

        dataset_code = f.get("dataset_code")

        region_code = normalize_code(
            f.get("region_code")
            or raw.get("dstrcd")
            or raw.get("contregnstr2code")
        )

        region_name = normalize_text(
            f.get("region_name")
            or raw.get("dstrname")
            or raw.get("contregnstr2name")
        )

        organization_code = normalize_code(
            f.get("organization_code")
            or raw.get("orgcd")
        )

        organization_name = normalize_text(
            f.get("organization_name")
            or raw.get("orgname")
        )

        rows.append({
            "dataset_code": dataset_code,
            "source_record_key": record.get(
                "source_record_key"
            ),
            "region_code": region_code,
            "region_name": region_name,
            "organization_code": organization_code,
            "organization_name": organization_name,
            "organization_type": normalize_text(
                f.get("organization_type")
                or raw.get("orgtypenm")
            ),
            "source_endpoint": f.get(
                "source_endpoint"
            ),
        })

    return pd.DataFrame(rows)


def build_quality_report(df):
    """데이터셋별 검증 보고서."""

    counts = (
        df.groupby("dataset_code")
        .size()
        .to_dict()
    )

    duplicate_keys = int(
        df.duplicated(
            subset=[
                "dataset_code",
                "source_record_key",
            ]
        ).sum()
    )

    missing_source_keys = int(
        df["source_record_key"].isna().sum()
    )

    return {
        "total_rows": int(len(df)),
        "expected_total": sum(
            EXPECTED_COUNTS.values()
        ),
        "counts_by_source": {
            key: int(value)
            for key, value in counts.items()
        },
        "count_matches_expected": {
            code: counts.get(code, 0) == expected
            for code, expected in EXPECTED_COUNTS.items()
        },
        "duplicate_source_keys": duplicate_keys,
        "missing_source_keys": missing_source_keys,
        "null_counts": {
            col: int(df[col].isna().sum())
            for col in df.columns
        },
    }

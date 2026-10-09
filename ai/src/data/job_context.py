
"""
AI-F-001 공공데이터 조회 및 전처리.

대상:
- ai.dataset
- ai.dataset_record
- job_context_public

원본 DB는 수정하지 않는다.
"""

import json
import re
import unicodedata

import pandas as pd
from sqlalchemy import inspect, text


DATASET_NAME = "job_context_public"

SOURCE_CODES = {
    "PUB-001",
    "PUB-002A",
    "PUB-002B",
    "PUB-003",
}


def load_job_context(engine):
    """AI-F-001 데이터셋을 DB에서 읽는다."""

    inspector = inspect(engine)

    for table in ("dataset", "dataset_record"):
        if not inspector.has_table(table, schema="ai"):
            raise RuntimeError(
                f"ai.{table} 테이블이 없습니다."
            )

    dataset_cols = {
        c["name"]
        for c in inspector.get_columns(
            "dataset", schema="ai"
        )
    }

    record_cols = {
        c["name"]
        for c in inspector.get_columns(
            "dataset_record", schema="ai"
        )
    }

    required_dataset = {
        "dataset_id",
        "dataset_name",
        "feature_code",
    }

    required_record = {
        "dataset_id",
        "features",
    }

    missing = (
        required_dataset - dataset_cols
    ) | (
        required_record - record_cols
    )

    if missing:
        raise RuntimeError(
            f"AI 데이터셋 컬럼 확인 필요: {sorted(missing)}"
        )

    # 실제 PK 이름이 다를 수 있으므로
    # 고정 ID 대신 PostgreSQL의 내부 행 식별자를 사용하지 않고
    # 데이터셋 FK와 JSONB만 읽는다.
    sql = text("""
        SELECT
            d.dataset_id,
            d.dataset_name,
            d.feature_code,
            r.features
        FROM ai.dataset AS d
        JOIN ai.dataset_record AS r
          ON r.dataset_id = d.dataset_id
        WHERE d.feature_code = :feature_code
          AND d.dataset_name = :dataset_name
    """)

    with engine.connect() as conn:
        df = pd.read_sql_query(
            sql,
            conn,
            params={
                "feature_code": "AI-F-001",
                "dataset_name": DATASET_NAME,
            },
        )

    if df.empty:
        raise RuntimeError(
            "AI-F-001 job_context_public 데이터가 없습니다."
        )

    return df


def parse_features(value):
    """JSONB 데이터를 Python dict로 변환."""

    if isinstance(value, dict):
        return value

    if isinstance(value, str):
        parsed = json.loads(value)

        if isinstance(parsed, dict):
            return parsed

    raise ValueError("features는 JSON 객체여야 합니다.")


def normalize_text(value):
    """명칭 표준화. 코드값은 별도로 처리."""

    if value is None:
        return None

    result = unicodedata.normalize(
        "NFKC", str(value)
    )

    result = re.sub(r"\s+", " ", result).strip()

    return result or None


def normalize_code(value):
    """코드 문자열 정규화. 선행 0은 유지."""

    if value is None:
        return None

    value = str(value).strip()

    if not value:
        return None

    # CSV에서 숫자로 변환된 123.0 형태만 복구.
    if re.fullmatch(r"\d+\.0", value):
        value = value[:-2]

    return value


def prepare_job_context(df):
    """원본 JSON을 분석용 테이블로 전개."""

    rows = []

    for _, record in df.iterrows():
        features = parse_features(
            record["features"]
        )

        # 원천 데이터셋 식별자는 실제 JSON에서 추출.
        # 존재하지 않는 값은 임의로 생성하지 않는다.
        dataset_code = (
            features.get("dataset_code")
            or features.get("source_code")
        )

        # 원본 컬럼명은 그대로 보존한다.
        row = {
            "dataset_id": record["dataset_id"],
            "dataset_code": dataset_code,
            **features,
        }

        rows.append(row)

    result = pd.DataFrame(rows)

    code_columns = [
        "dstrcd",
        "contregnstr1code",
        "contregnstr2code",
        "orgcd",
    ]

    name_columns = [
        "dstrname",
        "contregnstr1name",
        "contregnstr2name",
        "orgname",
        "orgtypenm",
    ]

    for col in code_columns:
        if col in result.columns:
            result[col] = result[col].map(
                normalize_code
            )

    for col in name_columns:
        if col in result.columns:
            result[col] = result[col].map(
                normalize_text
            )

    return result


def build_quality_report(df):
    """전처리 데이터의 품질 요약."""

    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "duplicate_rows": int(
            df.duplicated(
                subset=[
                    c for c in [
                        "dataset_id",
                        "dataset_code",
                        "dstrcd",
                        "orgcd",
                        "orgname",
                    ]
                    if c in df.columns
                ]
            ).sum()
        ),
        "null_counts": {
            column: int(df[column].isna().sum())
            for column in df.columns
        },
    }

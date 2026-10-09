
"""AI-F-002: 저장된 분석 근거를 이용한 Baseline 서비스."""
from functools import lru_cache
from pathlib import Path

import pandas as pd

from .model import RiskEvidence


DATA_DIR = Path(__file__).resolve().parent / "artifacts" / "data"

MAPPING_PATH = DATA_DIR / "job_industry_mapping_review.csv"


@lru_cache(maxsize=1)
def load_mapping() -> pd.DataFrame:
    """F-001 직무별 F-002 산업분류 검토 결과를 로드한다."""
    if not MAPPING_PATH.is_file():
        raise FileNotFoundError(
            f"매핑 검토 파일이 없습니다: {MAPPING_PATH}"
        )

    df = pd.read_csv(MAPPING_PATH, dtype={"job_id": str})

    required = {
        "job_id",
        "title",
        "candidate_category",
        "industry_candidate",
        "mapping_audit",
        "evidence_status",
        "evidence_year",
        "industry_accident_count",
        "evidence_usable",
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"필수 컬럼 누락: {sorted(missing)}")

    if df["job_id"].isna().any():
        raise ValueError("job_id에 결측값이 있습니다.")

    if df["job_id"].duplicated().any():
        raise ValueError("job_id 중복이 있습니다.")

    return df.set_index("job_id", drop=False)


def _nullable_str(value):
    return None if pd.isna(value) else str(value)


def get_risk_evidence(job_id: str) -> dict:
    """직무 ID에 해당하는 통계 근거와 검토 상태를 반환한다."""
    if not str(job_id).strip():
        raise ValueError("job_id가 비어 있습니다.")

    df = load_mapping()
    key = str(job_id).strip()

    if key not in df.index:
        raise LookupError(f"직무를 찾을 수 없습니다: {key}")

    row = df.loc[key]

    # 제목 키워드는 산업 확정 근거가 아니므로
    # 업종 검토 완료로 처리하지 않는다.
    mapping_audit = str(row["mapping_audit"])

    # 수동 검수된 산업 매핑이 아직 없으므로
    # 통계가 존재해도 위험 계산에는 사용하지 않는다.
    usable = False

    year = row["evidence_year"]
    count = row["industry_accident_count"]

    result = RiskEvidence(
        feature_id="AI-F-002",
        job_id=key,
        title=str(row["title"]),
        candidate_category=str(row["candidate_category"]),
        industry_candidate=_nullable_str(
            row["industry_candidate"]
        ),
        mapping_status="REVIEW_REQUIRED",
        mapping_audit=mapping_audit,
        evidence_status=str(row["evidence_status"]),
        evidence_year=(
            int(year) if pd.notna(year) else None
        ),
        industry_accident_count=(
            float(count) if pd.notna(count) else None
        ),
        evidence_usable=usable,
        risk_score=None,
    )

    return result.to_dict()



# ============================================================
# F-002 연령별 산업재해 통계 근거 조회
# ============================================================

AGE_PATH = DATA_DIR / "age_accident_clean.csv"


@lru_cache(maxsize=1)
def load_age_statistics() -> pd.DataFrame:
    """검증된 연령별 통계를 CSV에서 읽는다."""
    if not AGE_PATH.is_file():
        raise FileNotFoundError(
            f"연령별 통계 파일이 없습니다: {AGE_PATH}"
        )

    df = pd.read_csv(AGE_PATH)

    required = {
        "statistic_year",
        "age_group",
        "metric_name",
        "accident_count",
        "quality_status",
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"연령별 데이터 필수 컬럼 누락: {sorted(missing)}"
        )

    if not df["quality_status"].eq("PASS").all():
        raise ValueError("검증되지 않은 연령별 데이터 존재")

    if df["accident_count"].isna().any():
        raise ValueError("재해자수 누락")

    if df["accident_count"].lt(0).any():
        raise ValueError("음수 재해자수 존재")

    keys = ["statistic_year", "age_group", "metric_name"]

    if df.duplicated(subset=keys).any():
        raise ValueError("연령별 집계 키 중복")

    return df


def get_age_statistics(year: int) -> dict:
    """특정 연도의 연령대별 재해자수를 조회한다."""
    df = load_age_statistics()

    selected = df[
        df["statistic_year"].eq(year)
        & df["metric_name"].eq("재해자수")
    ].copy()

    if selected.empty:
        raise LookupError(
            f"해당 연도 통계가 없습니다: {year}"
        )

    selected = selected.sort_values("age_group")

    items = [
        {
            "age_group": str(row.age_group),
            "accident_count": int(row.accident_count),
        }
        for row in selected.itertuples(index=False)
    ]

    return {
        "feature_id": "AI-F-002",
        "statistic_year": year,
        "metric_name": "재해자수",
        "age_statistics": items,
        "risk_score": None,
        "risk_probability": None,
        "data_status": "VALIDATED_AGGREGATES",
        "limitations": (
            "연령별 재해자수 집계이며, "
            "연령별 사고율이나 개인 사고 확률이 아닙니다."
        ),
    }


def get_combined_risk_evidence(
    job_id: str,
    year: int | None = None,
) -> dict:
    """직무별 산업 통계와 연령별 통계를 묶어서 반환한다."""

    # 기존 직무 조회 서비스 재사용
    job = get_risk_evidence(job_id)

    # 기본 연도는 연령 통계에서 가장 최근 연도
    if year is None:
        year = int(
            load_age_statistics()["statistic_year"].max()
        )

    # 기존 연령 통계 서비스 재사용
    age = get_age_statistics(year)

    # 산업분류는 검증되지 않았으므로 참고자료로 제공
    return {
        "feature_id": "AI-F-002",
        "job": job,
        "age_reference": age,
        "risk_score": None,
        "risk_probability": None,
        "assessment_status": "EVIDENCE_ONLY",
        "limitations": [
            "직무군과 사업장 산업분류는 아직 검증되지 않았습니다.",
            "연령별 통계는 특정 개인의 나이를 반영하지 않습니다.",
            "산업별 재해 건수와 연령별 재해 건수를 합산하지 않습니다.",
            "개인의 사고 확률 또는 위험도를 산출하지 않습니다.",
        ],
    }
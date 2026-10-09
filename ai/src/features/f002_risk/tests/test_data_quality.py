"""AI-F-002: 실제 분석 산출물 품질 테스트."""

from pathlib import Path

import pandas as pd
import pytest


DATA_DIR = (
    Path(__file__).resolve().parents[1]
    / "artifacts"
    / "data"
)


@pytest.fixture(scope="module")
def datasets():
    clean = pd.read_csv(
        DATA_DIR / "industry_accident_clean.csv"
    )

    review = pd.read_csv(
        DATA_DIR / "industry_accident_review.csv"
    )

    mapping = pd.read_csv(
        DATA_DIR / "job_industry_mapping_review.csv",
        dtype={"job_id": str},
    )

    return clean, review, mapping


def test_clean_industry_data(datasets):
    clean, _, _ = datasets

    keys = [
        "statistic_year",
        "industry_major_clean",
        "industry_middle_clean",
        "accident_category",
        "metric_name",
    ]

    assert len(clean) == 657
    assert clean["quality_status"].eq("PASS").all()
    assert clean["accident_count"].notna().all()
    assert clean["accident_count"].ge(0).all()
    assert not clean.duplicated(subset=keys).any()


def test_conflicting_groups_are_separated(datasets):
    _, review, _ = datasets

    assert len(review) == 12
    assert review["quality_status"].eq("CONFLICT").all()


def test_job_mapping_integrity(datasets):
    _, _, mapping = datasets

    assert len(mapping) == 20000
    assert mapping["job_id"].notna().all()
    assert mapping["job_id"].is_unique


def test_unverified_risk_scores_are_empty(datasets):
    _, _, mapping = datasets

    assert mapping["risk_score"].isna().all()
    assert not mapping["evidence_usable"].fillna(False).any()


def test_mapping_audit_statuses(datasets):
    _, _, mapping = datasets

    allowed = {
        "NO_INDUSTRY_SIGNAL",
        "POSSIBLE_MISMATCH",
        "UNMAPPED_WITH_SIGNAL",
        "CANDIDATE_CONSISTENT",
        "MULTIPLE_SIGNALS",
    }

    assert set(mapping["mapping_audit"]).issubset(allowed)
    assert mapping["mapping_audit"].notna().all()
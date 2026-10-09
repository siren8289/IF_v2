
"""AI-F-002 Baseline 테스트."""
import pandas as pd
import pytest

from src.features.f002_risk import service


@pytest.fixture
def sample_mapping(monkeypatch):
    df = pd.DataFrame([
        {
            "job_id": "JOB-001",
            "title": "건설현장 경비원",
            "candidate_category": "SECURITY",
            "industry_candidate": "기타의사업",
            "mapping_audit": "POSSIBLE_MISMATCH",
            "evidence_status": "PROVISIONAL_EVIDENCE",
            "evidence_year": 2025,
            "industry_accident_count": 49471,
            "evidence_usable": False,
        },
        {
            "job_id": "JOB-002",
            "title": "직무 미분류",
            "candidate_category": "UNKNOWN",
            "industry_candidate": None,
            "mapping_audit": "NO_INDUSTRY_SIGNAL",
            "evidence_status": "NOT_MAPPED",
            "evidence_year": None,
            "industry_accident_count": None,
            "evidence_usable": False,
        },
    ])

    monkeypatch.setattr(
        service,
        "load_mapping",
        lambda: df.set_index("job_id", drop=False)
    )


def test_conflict_is_not_risk_score(sample_mapping):
    result = service.get_risk_evidence("JOB-001")

    assert result["feature_id"] == "AI-F-002"
    assert result["mapping_audit"] == "POSSIBLE_MISMATCH"
    assert result["risk_score"] is None
    assert result["evidence_usable"] is False


def test_unmapped_job_has_no_score(sample_mapping):
    result = service.get_risk_evidence("JOB-002")

    assert result["industry_candidate"] is None
    assert result["industry_accident_count"] is None
    assert result["risk_score"] is None


def test_unknown_job_raises_error(sample_mapping):
    with pytest.raises(LookupError):
        service.get_risk_evidence("UNKNOWN-ID")


def test_blank_job_id_raises_error(sample_mapping):
    with pytest.raises(ValueError):
        service.get_risk_evidence("")

def test_real_csv_integration():
    """실제 20,000건 CSV에서 직무 조회를 검증한다."""
    service.load_mapping.cache_clear()

    try:
        df = service.load_mapping()

        assert len(df) == 20000
        assert df.index.is_unique

        # 실제 CSV 첫 번째 직무로 조회
        job_id = str(df.iloc[0]["job_id"])
        result = service.get_risk_evidence(job_id)

        assert result["feature_id"] == "AI-F-002"
        assert result["job_id"] == job_id
        assert result["risk_score"] is None
        assert result["evidence_usable"] is False

    finally:
        service.load_mapping.cache_clear()
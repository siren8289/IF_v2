from fastapi.testclient import TestClient

from src.api.main import app
from src.features.f002_risk.service import load_mapping

client = TestClient(app)


def test_f002_api_success():
    """실제 직무 ID로 API 호출."""
    df = load_mapping()
    job_id = str(df.iloc[0]["job_id"])

    response = client.get(
        f"/api/v1/jobs/{job_id}/risk-evidence"
    )

    assert response.status_code == 200, response.text

    data = response.json()

    assert data["feature_id"] == "AI-F-002"
    assert data["job_id"] == job_id
    assert data["risk_score"] is None
    assert data["evidence_usable"] is False


def test_f002_api_not_found():
    """존재하지 않는 직무 ID."""
    response = client.get(
        "/api/v1/jobs/NOT-EXIST-999/risk-evidence"
    )

    assert response.status_code == 404



def test_age_statistics_success():
    """2025년 연령별 재해 통계 조회."""
    response = client.get(
        "/api/v1/risk/age-statistics?year=2025"
    )

    assert response.status_code == 200, response.text

    data = response.json()

    assert data["feature_id"] == "AI-F-002"
    assert data["statistic_year"] == 2025
    assert data["metric_name"] == "재해자수"
    assert data["risk_score"] is None
    assert data["risk_probability"] is None

    assert len(data["age_statistics"]) > 0
    assert all(
        item["accident_count"] >= 0
        for item in data["age_statistics"]
    )


def test_age_statistics_not_found():
    """통계가 없는 연도는 404."""
    response = client.get(
        "/api/v1/risk/age-statistics?year=1900"
    )

    assert response.status_code == 404


def test_age_statistics_missing_year():
    """필수 연도 누락 시 422."""
    response = client.get(
        "/api/v1/risk/age-statistics"
    )

    assert response.status_code == 422


def test_combined_risk_summary_success():
    """실제 직무 ID로 산업·연령 통합 조회."""
    df = load_mapping()
    job_id = str(df.iloc[0]["job_id"])

    response = client.get(
        f"/api/v1/jobs/{job_id}/risk-summary?year=2025"
    )

    assert response.status_code == 200, response.text

    data = response.json()

    assert data["feature_id"] == "AI-F-002"
    assert data["job"]["job_id"] == job_id
    assert data["age_reference"]["statistic_year"] == 2025
    assert data["risk_score"] is None
    assert data["risk_probability"] is None
    assert data["assessment_status"] == "EVIDENCE_ONLY"


def test_combined_risk_summary_not_found():
    """존재하지 않는 직무 ID는 404."""
    response = client.get(
        "/api/v1/jobs/NOT-EXIST-999/risk-summary"
    )

    assert response.status_code == 404


def test_combined_risk_summary_invalid_year():
    """연령 통계가 없는 연도는 404."""
    df = load_mapping()
    job_id = str(df.iloc[0]["job_id"])

    response = client.get(
        f"/api/v1/jobs/{job_id}/risk-summary?year=1900"
    )

    assert response.status_code == 404
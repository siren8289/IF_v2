
"""AI-F-003 FastAPI 통합 테스트."""

from fastapi.testclient import TestClient

from src.api.main import app
from src.features.f002_risk.service import load_mapping


client = TestClient(app)


def test_f003_api_success():
    """실제 F-001 직무 ID를 사용한다."""
    df = load_mapping()
    job_id = str(df.iloc[0]["job_id"])

    response = client.get(
        f"/api/v1/jobs/{job_id}/risk-explanation?year=2025"
    )

    assert response.status_code == 200, response.text

    result = response.json()
    assert result["feature_id"] == "AI-F-003"
    assert result["job_id"] == job_id
    assert result["risk_score"] is None
    assert result["risk_probability"] is None
    assert result["explanation_method"] == "RULE_BASED"


def test_f003_api_unknown_job():
    response = client.get(
        "/api/v1/jobs/NOT-EXIST-999/risk-explanation"
    )

    assert response.status_code == 404


def test_f003_api_unknown_year():
    df = load_mapping()
    job_id = str(df.iloc[0]["job_id"])

    response = client.get(
        f"/api/v1/jobs/{job_id}/risk-explanation?year=1900"
    )

    assert response.status_code == 404


def test_f003_api_invalid_year():
    response = client.get(
        "/api/v1/jobs/JOB-001/risk-explanation?year=abc"
    )

    assert response.status_code == 422

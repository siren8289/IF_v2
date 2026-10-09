from fastapi.testclient import TestClient

from src.main import app
from src.risk_score import calculate_score, grade_of

client = TestClient(app)


def test_grade_boundaries():
    assert grade_of(40) == "LOW"
    assert grade_of(41) == "MID"
    assert grade_of(60) == "MID"
    assert grade_of(61) == "HIGH"


def test_young_healthy_person_gets_zero_without_task_points():
    result = calculate_score(
        age=50, physical_level=1, chronic_disease=False, work_hour_limit=8,
        ml_scores={}, dl_scores={},
    )
    assert result["risk_score"] == 0
    assert result["risk_grade"] == "LOW"


def test_worst_inputs_reach_100():
    all_one = {"DRIVING": 1, "NIGHT_SHIFT": 1, "WALKING": 1,
               "CLEANING_TASK": 1, "CARE_TASK": 1, "FACILITY_MAINTENANCE": 1}
    result = calculate_score(
        age=95, physical_level=5, chronic_disease=True, work_hour_limit=1,
        ml_scores=all_one, dl_scores=all_one,
    )
    assert result["risk_score"] == 100
    assert result["risk_grade"] == "HIGH"


def test_analyze_api_uses_ml_dl_and_explanation(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    response = client.post("/api/v1/risk/analyze", json={
        "title": "아파트 경비원 모집",
        "age": 70,
        "physical_level": 3,
        "chronic_disease": True,
        "work_hour_limit": 6,
    })
    assert response.status_code == 200
    body = response.json()
    assert 0 <= body["risk_score"] <= 100
    assert body["risk_grade"] in ("LOW", "MID", "HIGH")
    assert len(body["task_scores"]) == 6
    assert body["explanation_source"] == "basic"
    assert body["explanation"]


def test_analyze_api_rejects_bad_age():
    response = client.post("/api/v1/risk/analyze", json={
        "title": "경비원", "age": 0, "physical_level": 3,
        "chronic_disease": False, "work_hour_limit": 6,
    })
    assert response.status_code == 422

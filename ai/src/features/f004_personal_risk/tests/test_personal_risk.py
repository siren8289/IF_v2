import math

import pytest
from fastapi.testclient import TestClient

from src.api.main import app
from src.features.f004_personal_risk import service

PAYLOAD = {"job_id": "KJ21062610080016", "title": "야간 배송기사 모집", "age": 70,
           "physical_level": 3, "chronic_disease": False, "work_hour_limit": 8}
client = TestClient(app)


@pytest.fixture
def models(monkeypatch):
    def fake(title, task_model):
        return {"task_analysis": {"task_characteristics": [
            {"label": label, "score": 0.0} for label in service.TASK_WEIGHTS]}}
    monkeypatch.setattr(service, "predict_f001", fake)
    monkeypatch.setattr(service, "get_combined_risk_evidence", lambda job_id: {"risk_score": None})
    monkeypatch.setattr(service, "explain_risk", lambda job_id: {"summary": "기존 통계 설명"})


def test_transparent_components(models):
    result = service.calculate_personal_risk(service.PersonalRiskRequest(**PAYLOAD))
    assert result["risk_score"] == 19  # 연령 6.6667 + 건강 12.5, 반올림
    assert result["risk_probability"] is None
    assert result["score_type"] == "REFERENCE_INDEX"
    assert result["evidence_status"] == "REFERENCE_ONLY"
    assert {f["code"] for f in result["factors"]} == {"AGE", "PHYSICAL", "CHRONIC", "CAPACITY", "TASK"}
    assert result["review_required"] is True


@pytest.mark.parametrize("score,grade", [(0,"LOW"),(40,"LOW"),(41,"MID"),(60,"MID"),(61,"HIGH"),(100,"HIGH")])
def test_grade_boundaries(score, grade):
    assert service.grade_of(score) == grade


def test_minimum_zero_and_maximum_100(models, monkeypatch):
    low = {**PAYLOAD, "age": 20, "physical_level": 1}
    assert service.calculate_personal_risk(service.PersonalRiskRequest(**low))["risk_score"] == 0
    def maximum(title, task_model):
        return {"task_analysis": {"task_characteristics": [
            {"label": label, "score": 1.0} for label in service.TASK_WEIGHTS]}}
    monkeypatch.setattr(service, "predict_f001", maximum)
    high = {**PAYLOAD, "age": 120, "physical_level": 5, "chronic_disease": True, "work_hour_limit": 1}
    assert service.calculate_personal_risk(service.PersonalRiskRequest(**high))["risk_score"] == 100


def test_ml_dl_average(models, monkeypatch):
    calls = []
    def fake(title, task_model):
        calls.append(task_model)
        return {"task_analysis": {"task_characteristics": [
            {"label": label, "score": (1 if task_model == "ml" else 0) if label == "DRIVING" else 0}
            for label in service.TASK_WEIGHTS]}}
    monkeypatch.setattr(service, "predict_f001", fake)
    result = service.calculate_personal_risk(service.PersonalRiskRequest(**PAYLOAD))
    assert calls == ["ml", "dl"]
    assert result["factors"][-1]["points"] == 5


def test_statistics_do_not_change_score(models, monkeypatch):
    first = service.calculate_personal_risk(service.PersonalRiskRequest(**PAYLOAD))
    monkeypatch.setattr(service, "get_combined_risk_evidence", lambda job_id: {"industry_accident_count": 999999999})
    second = service.calculate_personal_risk(service.PersonalRiskRequest(**PAYLOAD))
    assert first["risk_score"] == second["risk_score"]


def test_unknown_evidence_is_disclosed(models, monkeypatch):
    def missing(job_id): raise LookupError("not found")
    monkeypatch.setattr(service, "get_combined_risk_evidence", missing)
    result = service.calculate_personal_risk(service.PersonalRiskRequest(**PAYLOAD))
    assert result["evidence"] is None
    assert result["evidence_status"] == "UNAVAILABLE"
    assert "없어" in result["limitations"][-1]


@pytest.mark.parametrize("field,value", [("age",0),("age",121),("age",70.5),("age","70"),
    ("physical_level",0),("physical_level",6),("chronic_disease","false"),
    ("work_hour_limit",0),("work_hour_limit",25),("title","   ")])
def test_invalid_input(field, value):
    response = client.post("/api/v1/risk/personal-score", json={**PAYLOAD,field:value})
    assert response.status_code == 422


def test_missing_health_is_not_defaulted():
    payload = {key:value for key,value in PAYLOAD.items() if key != "chronic_disease"}
    assert client.post("/api/v1/risk/personal-score", json=payload).status_code == 422


@pytest.mark.parametrize("score", [math.nan, math.inf, -0.1, 1.1])
def test_invalid_model_outputs(models, monkeypatch, score):
    def invalid(title, task_model):
        return {"task_analysis": {"task_characteristics": [
            {"label": label, "score": score} for label in service.TASK_WEIGHTS]}}
    monkeypatch.setattr(service, "predict_f001", invalid)
    assert client.post("/api/v1/risk/personal-score", json=PAYLOAD).status_code == 502


def test_model_missing_fails_without_fake_score(models, monkeypatch):
    def missing(*args, **kwargs): raise FileNotFoundError("private path")
    monkeypatch.setattr(service, "predict_f001", missing)
    response = client.post("/api/v1/risk/personal-score", json=PAYLOAD)
    assert response.status_code == 503
    assert "private path" not in response.text


def test_real_models_and_existing_statistics():
    response = client.post("/api/v1/risk/personal-score", json=PAYLOAD)
    assert response.status_code == 200, response.text
    result = response.json()
    assert 0 <= result["risk_score"] <= 100
    assert result["evidence"]["assessment_status"] == "EVIDENCE_ONLY"
    assert result["explanation"]["feature_id"] == "AI-F-003"
    assert result["job_analysis"]["ml"]["task_analysis"]["selected_model"] == "ml"
    assert result["job_analysis"]["dl"]["task_analysis"]["selected_model"] == "dl"


import pytest
from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)

URL = "/api/v1/jobs/analyze-integrated"


@pytest.mark.parametrize(
    "model_type",
    ["ml", "dl"],
)
def test_integrated_api(model_type):
    response = client.post(
        URL,
        json={
            "title": "야간 배송기사 모집",
            "task_model": model_type,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["feature_id"] == "AI-F-001"
    assert data["job_classification"]["category"] == "DRIVING"

    assert (
        data["task_analysis"]["selected_model"]
        == model_type
    )

    candidates = {
        item["label"]
        for item in data["task_analysis"]["task_characteristics"]
        if item["candidate"]
    }

    assert {"DRIVING", "NIGHT_SHIFT"} <= candidates


def test_default_model():
    response = client.post(
        URL,
        json={"title": "야간 배송기사 모집"},
    )

    assert response.status_code == 200
    assert (
        response.json()["task_analysis"]["selected_model"]
        == "ml"
    )


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "", "task_model": "ml"},
        {"title": "   ", "task_model": "ml"},
        {"title": "배송기사", "task_model": "invalid"},
        {"task_model": "dl"},
    ],
)
def test_invalid_input(payload):
    response = client.post(URL, json=payload)
    assert response.status_code == 422


def test_integrated_model_missing_returns_503(monkeypatch):
    def raise_missing(**kwargs):
        raise FileNotFoundError("model missing")

    monkeypatch.setattr(
        "src.api.routes.predict_f001", raise_missing
    )

    response = client.post(URL, json={"title": "야간 배송기사 모집"})

    assert response.status_code == 503
    assert "model missing" not in response.text


def test_integrated_unexpected_error_returns_500(monkeypatch):
    def raise_error(**kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(
        "src.api.routes.predict_f001", raise_error
    )

    response = client.post(URL, json={"title": "야간 배송기사 모집"})

    assert response.status_code == 500
    assert "boom" not in response.text

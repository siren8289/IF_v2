"""
AI-F-001 ML 예측 API 테스트.

실행:
python -m pytest tests/test_f001_api.py -v
"""

from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)

API_URL = "/api/v1/jobs/predict"


def test_f001_prediction():
    response = client.post(
        API_URL,
        json={"title": "아파트 경비원 모집"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "아파트 경비원 모집"
    assert data["category"] == "SECURITY"
    assert data["review_required"] is True
    assert data["experimental"] is True

    assert "model_score" in data
    assert "score_margin" in data
    assert len(data["alternatives"]) == 3


def test_f001_empty_title():
    response = client.post(API_URL, json={"title": ""})

    assert response.status_code == 422


def test_f001_missing_title():
    response = client.post(API_URL, json={})

    assert response.status_code == 422

# IF-0153~IF-0177. FastAPI TestClient만 사용한다. DB에는 연결하지 않는다.
import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

BASE = {
    "title": "운전기사",
    "age": 60,
    "physical_level": 3,
    "chronic_disease": False,
    "work_hour_limit": 8,
}

# 시트 셀의 a 반복은 닫는 따옴표 없이 잘려 있었다.
# 첫 칸은 79자, 둘째 칸은 99자다. 둘 다 max_length 300 미만이다.
TITLE_79 = "a" * 79
TITLE_99 = "a" * 99


@pytest.fixture(autouse=True)
def no_gemini(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)


def post(overrides):
    body = dict(BASE)
    body.update(overrides)
    return client.post("/api/v1/risk/analyze", json=body)


def assert_result(response):
    assert response.status_code == 200, response.text
    payload = response.json()
    assert isinstance(payload.get("risk_score"), int)
    assert payload.get("risk_grade") in {"LOW", "MID", "HIGH"}
    assert payload.get("explanation")
    assert payload.get("model_version") == "SIMPLE_V1"


def assert_rejected(response):
    assert response.status_code == 422, response.text
    detail = response.json().get("detail")
    assert detail


def test_IF_0153_empty_title():
    assert_rejected(post({"title": ""}))


def test_IF_0154_blank_title():
    assert_rejected(post({"title": "   "}))


def test_IF_0155_driver_title():
    assert_result(post({"title": "운전기사"}))


def test_IF_0156_title_79():
    assert_result(post({"title": TITLE_79}))


def test_IF_0157_title_99():
    assert_result(post({"title": TITLE_99}))


def test_IF_0158_age_0():
    assert_rejected(post({"age": 0}))


def test_IF_0159_age_1():
    assert_result(post({"age": 1}))


def test_IF_0160_age_60():
    assert_result(post({"age": 60}))


def test_IF_0161_age_90():
    assert_result(post({"age": 90}))


def test_IF_0162_age_120():
    assert_result(post({"age": 120}))


def test_IF_0163_age_121():
    assert_rejected(post({"age": 121}))


def test_IF_0164_physical_0():
    assert_rejected(post({"physical_level": 0}))


def test_IF_0165_physical_1():
    assert_result(post({"physical_level": 1}))


def test_IF_0166_physical_3():
    assert_result(post({"physical_level": 3}))


def test_IF_0167_physical_5():
    assert_result(post({"physical_level": 5}))


def test_IF_0168_physical_6():
    assert_rejected(post({"physical_level": 6}))


def test_IF_0169_chronic_true():
    assert_result(post({"chronic_disease": True}))


def test_IF_0170_chronic_false():
    assert_result(post({"chronic_disease": False}))


def test_IF_0171_chronic_abc():
    assert_rejected(post({"chronic_disease": "abc"}))


def test_IF_0172_hours_0():
    assert_rejected(post({"work_hour_limit": 0}))


def test_IF_0173_hours_1():
    assert_result(post({"work_hour_limit": 1}))


def test_IF_0174_hours_7():
    assert_result(post({"work_hour_limit": 7}))


def test_IF_0175_hours_8():
    assert_result(post({"work_hour_limit": 8}))


def test_IF_0176_hours_24():
    assert_result(post({"work_hour_limit": 24}))


def test_IF_0177_hours_25():
    assert_rejected(post({"work_hour_limit": 25}))

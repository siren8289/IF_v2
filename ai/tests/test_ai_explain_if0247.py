# IF-0247~IF-0255. explain은 mock만 사용한다. Gemini 실호출과 DB는 없다.
import sys
import types

from src.ai_explain import explain


def result(grade, score=24, factors=None):
    if factors is None:
        factors = [{"name": "나이", "points": score, "max": 20}]
    return {"risk_score": score, "risk_grade": grade, "factors": factors}


def install_genai(monkeypatch, generate):
    """explain 안의 google.genai import가 이 가짜 모듈을 쓰게 한다."""
    calls = []
    google = types.ModuleType("google")
    genai = types.ModuleType("google.genai")
    genai_types = types.ModuleType("google.genai.types")

    class HttpOptions:
        def __init__(self, timeout=None):
            self.timeout = timeout

    class Models:
        def generate_content(self, **kwargs):
            calls.append(kwargs)
            return generate()

    class Client:
        def __init__(self, api_key=None, http_options=None):
            self.models = Models()
            calls.append({"api_key": api_key, "timeout": http_options.timeout})

    genai_types.HttpOptions = HttpOptions
    genai.Client = Client
    google.genai = genai
    monkeypatch.setitem(sys.modules, "google", google)
    monkeypatch.setitem(sys.modules, "google.genai", genai)
    monkeypatch.setitem(sys.modules, "google.genai.types", genai_types)
    return calls


def test_IF_0247_no_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    text, source = explain("운전기사", result("LOW"))
    assert source == "basic"
    assert "참고 지수" in text
    assert "낮음" in text


def test_IF_0248_gemini_text_is_trimmed(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    class Response:
        text = "  생성된 설명입니다.  \n"

    calls = install_genai(monkeypatch, lambda: Response())
    text, source = explain("운전기사", result("LOW"))
    assert calls
    assert source == "gemini"
    assert text == "생성된 설명입니다."


def test_IF_0249_empty_gemini_text_uses_basic(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    class Response:
        text = None

    calls = install_genai(monkeypatch, lambda: Response())
    text, source = explain("운전기사", result("MID", score=50))
    assert calls
    assert source == "basic"
    assert "참고 지수" in text
    assert "보통" in text


def test_IF_0250_gemini_exception_uses_basic(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    def raise_error():
        raise RuntimeError("mock failure")

    calls = install_genai(monkeypatch, raise_error)
    text, source = explain("운전기사", result("HIGH", score=80))
    assert calls
    assert source == "basic"
    assert "참고 지수" in text
    assert "높음" in text


def test_IF_0251_tie_keeps_first_factor(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    tied = result(
        "LOW",
        score=20,
        factors=[
            {"name": "나이", "points": 10, "max": 20},
            {"name": "건강 상태", "points": 10, "max": 25},
        ],
    )
    text, source = explain("운전기사", tied)
    assert source == "basic"
    assert "가장 크게 반영된 항목은 '나이'입니다." in text


def test_IF_0252_low_grade_name(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    text, source = explain("운전기사", result("LOW", score=10))
    assert source == "basic"
    assert "낮음" in text


def test_IF_0253_mid_grade_name(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    text, source = explain("운전기사", result("MID", score=50))
    assert source == "basic"
    assert "보통" in text


def test_IF_0254_high_grade_name(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    text, source = explain("운전기사", result("HIGH", score=80))
    assert source == "basic"
    assert "높음" in text


def test_IF_0255_warning_does_not_claim_probability(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    text, source = explain("운전기사", result("LOW", score=10))
    assert source == "basic"
    assert "이 점수는 사고 확률이 아니므로" in text

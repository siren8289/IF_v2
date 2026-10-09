
"""AI-F-003 설명 생성 단위 테스트."""

import pytest

from src.features.f003_explanation import service


@pytest.fixture
def sample_evidence(monkeypatch):
    """F-002 응답 형태를 사용한 테스트 데이터."""
    result = {
        "job": {
            "job_id": "JOB-001",
            "title": "건설현장 경비원",
            "industry_candidate": "기타의사업",
            "industry_accident_count": 49471.0,
            "evidence_year": 2025,
            "mapping_audit": "POSSIBLE_MISMATCH",
        },
        "age_reference": {
            "statistic_year": 2025,
            "metric_name": "재해자수",
            "age_statistics": [
                {
                    "age_group": "60세 ~ 64세",
                    "accident_count": 22938,
                },
            ],
        },
    }

    monkeypatch.setattr(
        f"{service.__name__}.get_combined_risk_evidence",
        lambda job_id, year=None: result,
    )


def test_explanation_has_grounded_count(sample_evidence):
    result = service.explain_risk("JOB-001", 2025)

    assert result["feature_id"] == "AI-F-003"
    assert "49,471명" in result["summary"]
    assert result["explanation_method"] == "RULE_BASED"
    assert len(result["evidence"]) == 2


def test_explanation_detects_mapping_conflict(sample_evidence):
    result = service.explain_risk("JOB-001")

    assert result["mapping_audit"] == "POSSIBLE_MISMATCH"
    assert any(
        "충돌" in item
        for item in result["limitations"]
    )


def test_explanation_never_invents_risk_score(sample_evidence):
    result = service.explain_risk("JOB-001")

    assert result["risk_score"] is None
    assert result["risk_probability"] is None
    assert result["explanation_status"] == "EVIDENCE_ONLY"


def test_explanation_handles_missing_industry(monkeypatch):
    """업종 통계가 없는 경우에도 허위 근거를 만들지 않는다."""
    result = {
        "job": {
            "job_id": "JOB-002",
            "title": "사무직",
            "industry_candidate": None,
            "industry_accident_count": None,
            "evidence_year": None,
            "mapping_audit": "NO_INDUSTRY_SIGNAL",
        },
        "age_reference": {
            "statistic_year": 2025,
            "metric_name": "재해자수",
            "age_statistics": [],
        },
    }

    monkeypatch.setattr(
        f"{service.__name__}.get_combined_risk_evidence",
        lambda job_id, year=None: result,
    )

    explained = service.explain_risk("JOB-002")

    assert "산업별 통계 근거가 아직 없습니다" in explained["summary"]
    assert all(
        item["type"] != "INDUSTRY_ACCIDENT_COUNT"
        for item in explained["evidence"]
    )


def test_hybrid_api_error_fallback(
    monkeypatch, sample_evidence
):
    """Gemini API 오류 발생 시 규칙 기반 설명 반환."""

    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    monkeypatch.setattr(
        service,
        "_reserve_llm_request",
        lambda: True,
    )

    def broken_gemini(_job):
        raise RuntimeError("429 simulated")

    monkeypatch.setattr(
        service,
        "_gemini_extra_explanation",
        broken_gemini,
    )

    result = service.explain_risk_hybrid("JOB-001")

    assert result["llm_used"] is False
    assert result["llm_status"] == "FALLBACK"
    assert result["explanation_method"] == "RULE_BASED"
    assert result["risk_score"] is None
    assert "extra_explanation" not in result
    assert result["summary"]



def test_hybrid_gemini_success(monkeypatch, sample_evidence):
    """Gemini 정상 응답이면 HYBRID로 반환한다."""
    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    monkeypatch.setattr(
        service,
        "_reserve_llm_request",
        lambda: True,
    )
    monkeypatch.setattr(
        service,
        "_gemini_extra_explanation",
        lambda job: (
            "산업분류 후보는 검토가 필요하며 "
            "실제 사업장의 업종을 추가로 확인해야 합니다."
        ),
    )

    result = service.explain_risk_hybrid("JOB-001", 2025)

    assert result["llm_used"] is True
    assert result["llm_status"] == "SUCCESS"
    assert result["explanation_method"] == "HYBRID"
    assert result["risk_score"] is None
    assert result["risk_probability"] is None
    assert "extra_explanation" in result


def test_hybrid_rejects_generated_numbers(
    monkeypatch, sample_evidence
):
    """Gemini가 임의의 위험 확률을 만들면 차단한다."""
    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    monkeypatch.setattr(
        service,
        "_reserve_llm_request",
        lambda: True,
    )
    monkeypatch.setattr(
        service,
        "_gemini_extra_explanation",
        lambda job: "이 직무의 사고 확률은 35%입니다.",
    )

    result = service.explain_risk_hybrid("JOB-001")

    assert result["llm_used"] is False
    assert result["llm_status"] == "VALIDATION_FAILED"
    assert result["explanation_method"] == "RULE_BASED"
    assert "extra_explanation" not in result
    assert result["risk_score"] is None


def test_hybrid_quota_fallback(monkeypatch, sample_evidence):
    """호출 한도 도달 시 Gemini를 호출하지 않는다."""
    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    monkeypatch.setattr(
        service,
        "_reserve_llm_request",
        lambda: False,
    )

    def should_not_call_gemini(job):
        raise AssertionError("Gemini를 호출하면 안 됩니다.")

    monkeypatch.setattr(
        service,
        "_gemini_extra_explanation",
        should_not_call_gemini,
    )

    result = service.explain_risk_hybrid("JOB-001")

    assert result["llm_used"] is False
    assert result["llm_status"] == "LOCAL_LIMIT"
    assert result["explanation_method"] == "RULE_BASED"
    assert result["risk_score"] is None



def test_hybrid_cache_hit(monkeypatch, sample_evidence):
    """캐시 HIT면 Gemini를 호출하지 않는다."""

    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    monkeypatch.setattr(
        service,
        "_get_cached_extra",
        lambda key: (
            "산업분류 후보는 실제 사업장의 "
            "업종을 확인한 뒤 검토해야 합니다."
        ),
    )

    def should_not_call():
        raise AssertionError("캐시 HIT에서 한도 차감 금지")

    monkeypatch.setattr(
        service,
        "_reserve_llm_request",
        should_not_call,
    )

    result = service.explain_risk_hybrid("JOB-001", 2025)

    assert result["llm_status"] == "CACHE_HIT"
    assert result["llm_used"] is True
    assert result["explanation_method"] == "HYBRID"
    assert result["risk_score"] is None


def test_hybrid_cache_miss_calls_gemini(
    monkeypatch, sample_evidence
):
    """캐시 MISS에서는 한도를 확인하고 Gemini를 호출한다."""

    monkeypatch.setenv("F003_LLM_ENABLED", "true")
    monkeypatch.setenv("GEMINI_API_KEY", "test-only")

    called = {"quota": 0, "gemini": 0, "saved": 0}

    monkeypatch.setattr(
        service,
        "_get_cached_extra",
        lambda key: None,
    )

    def reserve():
        called["quota"] += 1
        return True

    def generate(job):
        called["gemini"] += 1
        return (
            "실제 사업장 업종 확인이 필요하며 "
            "통계 해석에는 주의가 필요합니다."
        )

    def save(key, value):
        called["saved"] += 1

    monkeypatch.setattr(
        service, "_reserve_llm_request", reserve
    )
    monkeypatch.setattr(
        service, "_gemini_extra_explanation", generate
    )
    monkeypatch.setattr(
        service, "_save_cached_extra", save
    )

    result = service.explain_risk_hybrid("JOB-001", 2025)

    assert called == {
        "quota": 1,
        "gemini": 1,
        "saved": 1,
    }
    assert result["llm_status"] == "SUCCESS"
    assert result["risk_score"] is None

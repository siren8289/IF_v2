"""
AI-F-001 직무 작업 특성 분석 API 통합 테스트

관련 명세:
- AI-FR-001: 직무 작업 특성 자동 분류
- AI-FR-002: 입력값 검증
- AI-FR-004: JSON 응답 구조
- AI-FR-005: 검토 필요 상태
- AI-FR-006: 원문 근거 검증
- AI-FR-007: 예외 처리

인수 테스트:
- AT-001: 정상 분석
- AT-002: 설명 누락
- AT-004: 원문 근거 일치

경계 조건:
- EC-001: 입력 데이터 누락
- EC-003: 자동 확정 방지
- EC-006: 근거 검증 실패
"""

import importlib

import pytest
from fastapi.testclient import TestClient

from src.api.main import app
from src.services.job_analysis_service import JobAnalysisError


# ============================================================
# 1. 테스트 환경
# ============================================================

# 실제 서버 실행 없이 FastAPI 요청 테스트
client = TestClient(app)

# src.api.routes 모듈을 명확하게 import
# monkeypatch 대상 함수가 있는 모듈
routes_module = importlib.import_module("src.api.routes")


# ============================================================
# 2. 테스트용 입력 데이터
# ============================================================

def sample_request() -> dict:
    """
    정상적인 직무 분석 요청 데이터를 반환한다.

    실제 운영 DB가 아니라 테스트용 고정 데이터다.
    """

    return {
        "jobId": 1,
        "jobTitle": "공원 환경관리",
        "description": (
            "공원에서 걸어 다니며 "
            "쓰레기를 수거하고 청소한다."
        ),
        "workHours": 4,
    }


# ============================================================
# 3. Health Check
# ============================================================

def test_health():
    """FastAPI 서버 상태 조회 테스트."""

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ============================================================
# 4. AT-001: 정상 직무 분석
# ============================================================

def test_normal_analysis():
    """
    정상 입력 시 작업 특성 태그를 반환하는지 검증한다.
    """

    response = client.post(
        "/api/v1/jobs/analyze",
        json=sample_request(),
    )

    assert response.status_code == 200

    data = response.json()

    assert data["jobId"] == 1

    assert set(data["taskTags"]) == {
        "OUTDOOR",
        "WALKING",
        "CLEANING",
    }

    assert data["modelVersion"] == "keyword-baseline-v0.1"


# ============================================================
# 5. AI-FR-004: 응답 JSON 구조
# ============================================================

def test_response_schema():
    """
    API 응답에 필수 필드가 모두 포함되는지 확인한다.
    """

    response = client.post(
        "/api/v1/jobs/analyze",
        json=sample_request(),
    )

    assert response.status_code == 200

    data = response.json()

    required_fields = {
        "jobId",
        "taskTags",
        "confidence",
        "evidence",
        "reviewRequired",
        "modelVersion",
        "status",
    }

    assert required_fields.issubset(data.keys())

    assert isinstance(data["taskTags"], list)
    assert isinstance(data["confidence"], dict)
    assert isinstance(data["evidence"], list)
    assert isinstance(data["reviewRequired"], bool)


# ============================================================
# 6. AT-002: 업무 설명 누락
# ============================================================

def test_missing_description():
    """
    업무 설명 필드가 없으면 HTTP 422를 반환해야 한다.
    """

    payload = sample_request()

    del payload["description"]

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        "description" in error["loc"]
        for error in errors
    )


# ============================================================
# 7. EC-001: 공백 문자열
# ============================================================

@pytest.mark.parametrize(
    "description",
    [
        "",
        " ",
        "   ",
        "\n\t",
    ],
)
def test_blank_description(description):
    """
    비어 있거나 공백만 있는 설명은 거부해야 한다.
    """

    payload = sample_request()

    payload["description"] = description

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 422


# ============================================================
# 8. AI-FR-002: 근무시간 검증
# ============================================================

@pytest.mark.parametrize(
    "work_hours",
    [
        0,
        -1,
        25,
        "four",
        None,
    ],
)
def test_invalid_work_hours(work_hours):
    """
    1~24 범위를 벗어나거나 잘못된 타입이면 422.
    """

    payload = sample_request()

    payload["workHours"] = work_hours

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 422


# ============================================================
# 9. AI-FR-002: 잘못된 직무 ID
# ============================================================

def test_invalid_job_id():
    """직무 ID는 양의 정수여야 한다."""

    payload = sample_request()

    payload["jobId"] = -1

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 422


# ============================================================
# 10. AI-FR-002: 예상하지 않은 입력 필드
# ============================================================

def test_extra_field():
    """계약에 없는 추가 입력 필드를 거부한다."""

    payload = sample_request()

    payload["unknownField"] = "unexpected"

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 422


# ============================================================
# 11. AT-004: 원문 근거 검증
# ============================================================

def test_evidence_matches_description():
    """
    모든 근거의 시작·끝 위치가 실제 원문과 일치하는지 검사.
    """

    payload = sample_request()

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    evidence_list = data["evidence"]

    # 정상 샘플에는 근거가 하나 이상 있어야 한다.
    assert len(evidence_list) > 0

    for evidence in evidence_list:

        start = evidence["start"]
        end = evidence["end"]
        text = evidence["text"]

        assert 0 <= start < end <= len(payload["description"])

        assert payload["description"][start:end] == text

        assert evidence["tag"] in data["taskTags"]


# ============================================================
# 12. AI-FR-005: 검토 필요 상태
# ============================================================

def test_review_required():
    """
    검증되지 않은 Baseline 결과를 자동 확정하지 않는다.
    """

    response = client.post(
        "/api/v1/jobs/analyze",
        json=sample_request(),
    )

    assert response.status_code == 200

    data = response.json()

    assert data["reviewRequired"] is True
    assert data["status"] == "REVIEW_REQUIRED"

    # 아직 학습된 모델의 신뢰도가 없으므로 빈 객체
    assert data["confidence"] == {}


# ============================================================
# 13. EC-002: 작업 특성 미탐지
# ============================================================

def test_no_tags():
    """
    키워드가 탐지되지 않아도 안전한 직무로 확정하지 않는다.
    """

    payload = sample_request()

    payload["description"] = (
        "서류를 정리하고 컴퓨터로 자료를 입력한다."
    )

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["taskTags"] == []
    assert data["evidence"] == []
    assert data["reviewRequired"] is True
    assert data["status"] == "REVIEW_REQUIRED"


# ============================================================
# 14. AI-FR-007: 분석 결과 검증 실패
# ============================================================

def test_analysis_failure(monkeypatch):
    """
    Service에서 JobAnalysisError 발생 시 HTTP 502를 반환한다.
    """

    # 실제 Service 대신 테스트용 실패 함수 정의
    def fail_analysis(job):
        raise JobAnalysisError("테스트용 분석 실패")

    # routes.py가 참조하는 함수를 임시 교체
    monkeypatch.setattr(
        routes_module,
        "analyze_job_service",
        fail_analysis,
    )

    response = client.post(
        "/api/v1/jobs/analyze",
        json=sample_request(),
    )

    assert response.status_code == 502

    data = response.json()

    assert "검증에 실패" in data["detail"]


# ============================================================
# 15. AI-FR-007: 예상하지 못한 내부 오류
# ============================================================

def test_unexpected_failure(monkeypatch):
    """
    예상하지 못한 오류가 발생해도
    내부 예외 메시지가 사용자에게 노출되지 않아야 한다.
    """

    def fail_analysis(job):
        raise RuntimeError("내부 테스트 오류")

    monkeypatch.setattr(
        routes_module,
        "analyze_job_service",
        fail_analysis,
    )

    response = client.post(
        "/api/v1/jobs/analyze",
        json=sample_request(),
    )

    assert response.status_code == 502

    assert "내부 테스트 오류" not in response.text


# ============================================================
# 16. 다중 라벨 분류 검증
# ============================================================

@pytest.mark.parametrize(
    "description,expected_tags",
    [
        (
            "공원에서 청소한다.",
            {"OUTDOOR", "CLEANING"},
        ),
        (
            "창고에서 무거운 물건을 운반한다.",
            {"HEAVY_LIFTING"},
        ),
        (
            "제품을 반복적으로 포장한다.",
            {"REPETITIVE_MOTION"},
        ),
        (
            "거리에서 도보로 이동하며 청소한다.",
            {"OUTDOOR", "WALKING", "CLEANING"},
        ),
    ],
)
def test_multiple_job_types(description, expected_tags):
    """
    다양한 직무 설명에 대해
    규칙 기반 다중 라벨 분류가 정상 작동하는지 확인한다.
    """

    payload = sample_request()

    payload["description"] = description

    response = client.post(
        "/api/v1/jobs/analyze",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert set(data["taskTags"]) == expected_tags
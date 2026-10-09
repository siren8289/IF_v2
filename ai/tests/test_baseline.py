"""
AI-F-001 Baseline 단위 테스트.

AT-001: 정상 분석
AT-002: 입력값 검증
AT-004: 근거 원문 일치
EC-003: 자동 확정 방지
"""

import pytest

from pydantic import ValidationError

from src.models.baseline import (
    JobInput,
    analyze_job,
    verify_evidence,
)


def make_job(
    description="공원에서 걸어 다니며 쓰레기를 수거하고 청소한다.",
):
    return JobInput(
        jobId=1,
        jobTitle="공원 환경관리",
        description=description,
        workHours=4,
    )


def test_normal_analysis():
    """AT-001: 정상 입력에서 작업 특성 태그를 반환한다."""

    result = analyze_job(make_job())

    assert set(result["taskTags"]) == {
        "OUTDOOR",
        "WALKING",
        "CLEANING",
    }

    assert result["modelVersion"] == "keyword-baseline-v0.1"


def test_missing_description():
    """AT-002: 빈 직무 설명을 거부한다."""

    with pytest.raises(ValidationError):
        make_job(description="")


def test_whitespace_description():
    """AT-002: 공백만 있는 직무 설명을 거부한다."""

    with pytest.raises(ValidationError):
        make_job(description="   ")


def test_evidence_matches_original():
    """AT-004: 반환된 모든 근거가 원문에 존재한다."""

    job = make_job()
    result = analyze_job(job)

    assert len(result["evidence"]) > 0

    assert verify_evidence(
        job.description,
        result["evidence"],
    )


def test_invalid_evidence():
    """AT-004: 조작된 근거는 검증에 실패한다."""

    assert not verify_evidence(
        "공원에서 청소한다.",
        [{
            "text": "중량물",
            "start": 0,
            "end": 3,
        }],
    )


def test_review_required():
    """EC-003: Baseline 결과는 자동 확정하지 않는다."""

    result = analyze_job(make_job())

    assert result["reviewRequired"] is True
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["confidence"] == {}


def test_invalid_work_hours():
    """AI-FR-002: 잘못된 근무시간을 거부한다."""

    with pytest.raises(ValidationError):
        JobInput(
            jobId=1,
            jobTitle="공원 환경관리",
            description="공원에서 청소한다.",
            workHours=0,
        )


def test_no_tags():
    """태그가 없어도 안전한 직무로 자동 확정하지 않는다."""

    result = analyze_job(
        make_job("서류를 정리하고 자료를 입력한다.")
    )

    assert result["taskTags"] == []
    assert result["evidence"] == []
    assert result["reviewRequired"] is True
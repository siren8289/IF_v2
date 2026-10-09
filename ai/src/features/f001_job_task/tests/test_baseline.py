
"""
AI-F-001 Baseline 단위 테스트.
"""

import pytest
from pydantic import ValidationError

from src.features.f001_job_task.model import (
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
    result = analyze_job(make_job())

    assert set(result["taskTags"]) == {
        "OUTDOOR",
        "WALKING",
        "CLEANING",
    }

    assert result["modelVersion"] == "keyword-baseline-v0.1"


def test_missing_description():
    with pytest.raises(ValidationError):
        make_job(description="")


def test_whitespace_description():
    with pytest.raises(ValidationError):
        make_job(description="   ")


def test_evidence_matches_original():
    job = make_job()
    result = analyze_job(job)

    assert len(result["evidence"]) > 0
    assert verify_evidence(
        job.description,
        result["evidence"],
    )


def test_invalid_evidence():
    assert not verify_evidence(
        "공원에서 청소한다.",
        [{
            "text": "중량물",
            "start": 0,
            "end": 3,
        }],
    )


def test_review_required():
    result = analyze_job(make_job())

    assert result["reviewRequired"] is True
    assert result["status"] == "REVIEW_REQUIRED"
    assert result["confidence"] == {}


def test_invalid_work_hours():
    with pytest.raises(ValidationError):
        JobInput(
            jobId=1,
            jobTitle="공원 환경관리",
            description="공원에서 청소한다.",
            workHours=0,
        )


def test_no_tags():
    result = analyze_job(
        make_job("서류를 정리하고 자료를 입력한다.")
    )

    assert result["taskTags"] == []
    assert result["evidence"] == []
    assert result["reviewRequired"] is True

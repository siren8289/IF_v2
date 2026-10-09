"""
AI-F-001 직무 분석 Service 계층.

API와 분류 엔진 사이의 비즈니스 로직을 담당한다.
"""

from src.models.baseline import (
    JobInput,
    analyze_job,
    verify_evidence,
)


class JobAnalysisError(Exception):
    """직무 분석 또는 근거 검증에 실패했을 때 발생한다."""


def analyze_job_service(job: JobInput) -> dict:
    """직무 분석 결과를 검증하고 API 응답으로 반환한다."""

    # 1. 규칙 기반 작업 특성 분류
    result = analyze_job(job)

    # 2. 분류 결과의 원문 근거 검증
    if not verify_evidence(
        job.description,
        result["evidence"],
    ):
        raise JobAnalysisError("원문 근거 검증 실패")

    # 3. 태그가 있는 경우 해당 태그에 대한 근거가 있는지 확인
    evidence_tags = {
        item["tag"]
        for item in result["evidence"]
    }

    for tag in result["taskTags"]:
        if tag not in evidence_tags:
            raise JobAnalysisError(
                f"태그 {tag}의 근거가 없습니다."
            )

    # 4. 학습·평가되지 않은 Baseline 결과는 자동 확정하지 않는다.
    result["reviewRequired"] = True
    result["status"] = "REVIEW_REQUIRED"

    return result
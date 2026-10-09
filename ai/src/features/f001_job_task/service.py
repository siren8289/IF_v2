
"""
AI-F-001 분석 서비스.

모델 실행과 결과 검증을 담당한다.
"""

from .model import JobInput, analyze_job, verify_evidence


class JobAnalysisError(Exception):
    """직무 분석 결과 검증 실패."""


def analyze_job_service(job: JobInput) -> dict:
    """직무 분석 실행 및 근거 검증."""

    result = analyze_job(job)

    if not verify_evidence(
        job.description,
        result["evidence"],
    ):
        raise JobAnalysisError(
            "분석 근거가 원문과 일치하지 않습니다."
        )

    if not result["reviewRequired"]:
        raise JobAnalysisError(
            "검증되지 않은 Baseline 결과를 자동 확정할 수 없습니다."
        )

    return result

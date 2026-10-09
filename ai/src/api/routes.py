"""
AI-F-001 FastAPI 라우터.

POST /api/v1/jobs/analyze
"""

import logging

from fastapi import APIRouter, HTTPException

from src.api.schemas import (
    JobAnalysisRequest,
    JobAnalysisResponse,
)
from src.models.baseline import JobInput
from src.services.job_analysis_service import (
    JobAnalysisError,
    analyze_job_service,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1",
    tags=["AI-F-001 Job Task Analysis"],
)


@router.post(
    "/jobs/analyze",
    response_model=JobAnalysisResponse,
    summary="직무 작업 특성 분석",
    description=(
        "직무 설명을 규칙 기반으로 분석하고 "
        "작업 특성 태그와 원문 근거를 반환한다."
    ),
)
def analyze_job_endpoint(
    request: JobAnalysisRequest,
):
    """
    AI-F-001 분석 요청 처리.

    1. Pydantic 입력 검증
    2. JobInput 변환
    3. Service 호출
    4. 분석 결과 반환

    입력 검증 실패: 422
    분석 결과 검증 실패: 502
    """

    try:
        job = JobInput(**request.model_dump())

        result = analyze_job_service(job)

        return result

    except JobAnalysisError as exc:
        logger.warning(
            "AI-F-001 결과 검증 실패: jobId=%s",
            request.jobId,
        )

        raise HTTPException(
            status_code=502,
            detail="직무 분석 결과 검증에 실패했습니다.",
        ) from exc

    except Exception as exc:
        logger.exception(
            "AI-F-001 예상하지 못한 오류: jobId=%s",
            request.jobId,
        )

        raise HTTPException(
            status_code=502,
            detail="직무 분석을 처리할 수 없습니다.",
        ) from exc
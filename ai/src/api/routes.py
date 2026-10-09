
"""
AI-F-001 FastAPI 라우터.

POST /api/v1/jobs/analyze
    규칙 기반 직무 작업 특성 분석

POST /api/v1/jobs/predict
    ML 기반 직무군 예측 (Weak Label 실험용)
"""

import logging
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from src.api.schemas import (
    JobAnalysisRequest,
    JobAnalysisResponse,
)
from src.features.f001_job_task.model import JobInput
from src.features.f001_job_task.service import (
    JobAnalysisError,
    analyze_job_service,
)
from src.features.f001_job_task.predict import predict_job
from src.features.f001_job_task.predict_f001 import predict_f001


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1",
    tags=["AI-F-001 Job Task Analysis"],
)


# ============================================================
# 1. 요청 스키마
# ============================================================

class F001PredictRequest(BaseModel):
    """직무군 예측 요청 데이터."""

    title: str = Field(
        min_length=1,
        max_length=300,
        description="직무 또는 구인공고 제목",
        examples=["아파트 경비원 모집"],
    )


class F001IntegratedRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    task_model: Literal["ml", "dl"] = "ml"

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("직무 제목은 비어 있을 수 없습니다.")
        return value


@router.post("/jobs/analyze-integrated")
def analyze_job_integrated(
    request: F001IntegratedRequest,
):
    """
    AI-F-001 통합 추론:
    LinearSVC 직무군 + ML/DL 작업 특성.
    """
    return predict_f001(
        title=request.title,
        task_model=request.task_model,
    )

# ============================================================
# 2. 규칙 기반 직무 작업 특성 분석 API
# ============================================================

@router.post(
    "/jobs/analyze",
    response_model=JobAnalysisResponse,
    summary="직무 작업 특성 분석",
)
def analyze_job_endpoint(request: JobAnalysisRequest):
    """
    직무 작업 특성을 규칙 기반으로 분석한다.

    처리:
    1. 요청 데이터 검증
    2. JobInput 변환
    3. Baseline 분석
    4. 근거 검증
    5. 분석 결과 반환
    """

    try:
        job = JobInput(**request.model_dump())

        return analyze_job_service(job)

    except JobAnalysisError as exc:
        logger.warning(
            "직무 분석 검증 실패: jobId=%s",
            request.jobId,
        )

        raise HTTPException(
            status_code=502,
            detail="직무 분석 결과 검증에 실패했습니다.",
        ) from exc

    except Exception as exc:
        logger.exception(
            "직무 분석 내부 오류: jobId=%s",
            request.jobId,
        )

        raise HTTPException(
            status_code=502,
            detail="직무 분석을 처리할 수 없습니다.",
        ) from exc


# ============================================================
# 3. ML 기반 직무군 예측 API
# ============================================================

@router.post(
    "/jobs/predict",
    summary="ML 기반 직무군 예측",
    tags=["AI-F-001 ML Prediction"],
)
def predict_job_endpoint(request: F001PredictRequest):
    """
    직무 제목을 기반으로 직무군을 예측한다.

    처리:
    1. 직무 제목 검증
    2. Weak Label 모델 로드
    3. 직무군 예측
    4. 모델 점수 및 점수 차이 계산
    5. 검토 상태 반환

    주의:
    - 실험용 모델이다.
    - 모델 점수는 위험도가 아니다.
    - 모든 결과는 담당자 검토가 필요하다.
    """

    try:
        return predict_job(request.title)

    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc

    except FileNotFoundError as exc:
        logger.error(
            "AI-F-001 모델 파일 없음: %s",
            exc,
        )

        raise HTTPException(
            status_code=503,
            detail="직무 분류 모델을 사용할 수 없습니다.",
        ) from exc

    except Exception as exc:
        logger.exception(
            "AI-F-001 직무군 예측 실패"
        )

        raise HTTPException(
            status_code=500,
            detail="직무군 예측 중 오류가 발생했습니다.",
        ) from exc

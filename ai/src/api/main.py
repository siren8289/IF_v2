"""
IF AI FastAPI 애플리케이션.

AI-F-001 직무 작업 특성 분석 기능을 제공한다.
"""

from fastapi import FastAPI

from src.api.routes import router
from src.api.schemas import HealthResponse


app = FastAPI(
    title="IF AI Service",
    version="0.1.0",
    description=(
        "고령자 일자리 직무 작업 특성 분석 서비스. "
        "현재 규칙 기반 Baseline PoC를 제공한다."
    ),
)

# API 라우터 등록
app.include_router(router)


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["Health"],
)
def health():
    """FastAPI 서버의 실행 상태를 반환한다."""
    return {"status": "ok"}
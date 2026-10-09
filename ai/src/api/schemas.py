"""
AI-F-001 FastAPI 요청 및 응답 스키마.

AI-FR-002: 입력값 유효성 검증
AI-FR-004: JSON 출력 계약 검증
"""

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)


class JobAnalysisRequest(BaseModel):
    """직무 작업 특성 분석 요청."""

    model_config = ConfigDict(extra="forbid", strict=True)

    jobId: int = Field(gt=0)
    jobTitle: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=10000)
    workHours: int = Field(gt=0, le=24)

    @field_validator("jobTitle", "description")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("빈 문자열은 허용하지 않습니다.")

        return value


class JobEvidence(BaseModel):
    """직무 설명에서 추출한 원문 근거."""

    model_config = ConfigDict(extra="forbid")

    tag: str
    text: str
    start: int = Field(ge=0)
    end: int = Field(gt=0)


class JobAnalysisResponse(BaseModel):
    """AI-F-001 분석 결과."""

    model_config = ConfigDict(extra="forbid")

    jobId: int
    taskTags: list[str]
    confidence: dict[str, float]
    evidence: list[JobEvidence]
    reviewRequired: bool
    modelVersion: str
    status: str


class HealthResponse(BaseModel):
    """API 서버 상태."""

    status: str
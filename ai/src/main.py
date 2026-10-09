"""IF AI 서버 (FastAPI).

API는 하나다: POST /api/v1/risk/analyze
  1. ML 모델(scikit-learn)로 작업 특성 점수 예측
  2. DL 모델(PyTorch)로 작업 특성 점수 예측
  3. 개인 입력과 합쳐 0~100점 참고 지수 계산
  4. 생성형 AI(Gemini)로 설명 문장 생성
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.ai_explain import explain
from src.dl_model import predict_dl
from src.ml_model import predict_ml
from src.risk_score import calculate_score

app = FastAPI(title="IF AI Service", version="1.0.0")


class AnalyzeRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300, examples=["아파트 경비원 모집"])
    age: int = Field(ge=1, le=120)
    physical_level: int = Field(ge=1, le=5, description="1=좋음 ~ 5=나쁨")
    chronic_disease: bool
    work_hour_limit: int = Field(ge=1, le=24)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/risk/analyze")
def analyze(request: AnalyzeRequest):
    title = request.title.strip()
    if not title:
        raise HTTPException(status_code=422, detail="직무 제목을 입력하세요.")

    ml_scores = predict_ml(title)
    dl_scores = predict_dl(title)

    result = calculate_score(
        age=request.age,
        physical_level=request.physical_level,
        chronic_disease=request.chronic_disease,
        work_hour_limit=request.work_hour_limit,
        ml_scores=ml_scores,
        dl_scores=dl_scores,
    )

    explanation, source = explain(title, result)
    result["explanation"] = explanation
    result["explanation_source"] = source
    result["model_version"] = "SIMPLE_V1"
    return result

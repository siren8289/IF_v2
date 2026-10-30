"""IF AI 서버 (FastAPI).

이 파일이 서버의 입구다. 화면(React)은 Spring을 부르고, Spring이 이 서버를 부른다.
하는 일은 하나다. POST /api/v1/risk/analyze

  1. ML 모델(scikit-learn)로 직무 제목에서 작업 특성 점수를 예측한다.
  2. DL 모델(PyTorch)로 같은 제목을 다시 예측한다.
  3. 나이·건강 같은 개인 입력과 합쳐 0~100점 참고 지수를 계산한다.
  4. 생성형 AI(Gemini)로 담당자가 읽을 설명 문장을 만든다.

점수는 사고 확률이 아니다. 정해 둔 규칙으로 더한 참고 숫자다.
"""
# FastAPI: 파이썬으로 웹 API(주소로 데이터를 주고받는 창구)를 만드는 도구.
# HTTPException: 입력이 잘못됐을 때 422 같은 오류 코드를 돌려주는 예외.
from fastapi import FastAPI, HTTPException
# BaseModel: 요청 JSON이 어떤 칸으로 이루어졌는지 적어 두는 틀.
# Field: 칸마다 "최소 1글자", "1~120" 같은 제한을 건다.
from pydantic import BaseModel, Field

from src.ai_explain import explain
from src.dl_model import predict_dl
from src.ml_model import predict_ml
from src.risk_score import calculate_score

# 서버 객체. uvicorn이 이 app을 실행한다.
app = FastAPI(title="IF AI Service", version="1.0.0")


class AnalyzeRequest(BaseModel):
    """Spring이 보내는 분석 요청. JSON 키 이름과 같아야 한다."""

    # 직무 제목. 예: "아파트 경비원 모집". 이 문장으로 작업 특성을 맞춘다.
    title: str = Field(min_length=1, max_length=300, examples=["아파트 경비원 모집"])
    # 신청자 나이. 1~120만 받는다.
    age: int = Field(ge=1, le=120)
    # 체력. 1이 좋음, 5가 나쁨이다. 숫자가 클수록 점수가 올라간다.
    physical_level: int = Field(ge=1, le=5, description="1=좋음 ~ 5=나쁨")
    # 만성질환이 있으면 True. 있으면 점수가 더해진다.
    chronic_disease: bool
    # 하루에 일할 수 있는 시간. 짧을수록 부담이 크다고 보고 점수를 올린다.
    work_hour_limit: int = Field(ge=1, le=24)


@app.get("/health")
def health():
    """서버가 살아 있는지 확인하는 주소. 배포 스크립트가 이 응답을 본다."""
    return {"status": "ok"}


@app.post("/api/v1/risk/analyze")
def analyze(request: AnalyzeRequest):
    """위험도 분석 본 작업. 성공하면 점수, 등급, 항목, 설명 문장을 돌려준다."""
    # 앞뒤 공백을 지운다. "  경비원  " 처럼 오면 모델이 헷갈릴 수 있다.
    title = request.title.strip()
    # 공백만 있는 제목은 분석할 내용이 없으므로 거절한다.
    # 422는 "요청 형식은 맞지만 내용이 잘못됐다"는 뜻이다.
    if not title:
        raise HTTPException(status_code=422, detail="직무 제목을 입력하세요.")

    # 같은 제목을 두 모델에 넣는다. 둘 다 {특성 이름: 0~1 점수} 딕셔너리를 돌려준다.
    # 예: {"DRIVING": 0.12, "NIGHT_SHIFT": 0.81, ...}
    ml_scores = predict_ml(title)
    dl_scores = predict_dl(title)

    # 개인 정보 + 두 모델 점수를 규칙에 넣어 0~100점으로 만든다.
    result = calculate_score(
        age=request.age,
        physical_level=request.physical_level,
        chronic_disease=request.chronic_disease,
        work_hour_limit=request.work_hour_limit,
        ml_scores=ml_scores,
        dl_scores=dl_scores,
    )

    # 설명 문장과 그 출처("gemini" 또는 "basic")를 붙인다.
    explanation, source = explain(title, result)
    result["explanation"] = explanation
    result["explanation_source"] = source
    # 어떤 계산 규칙으로 만들었는지 나중에 구분하려고 버전 이름을 남긴다.
    result["model_version"] = "SIMPLE_V1"
    return result

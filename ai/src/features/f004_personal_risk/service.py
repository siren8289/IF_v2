"""버전이 고정된 설명 가능한 정책 지수. 사고 확률/의학적 예측 모델이 아니다."""
from math import floor, isfinite

from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.features.f001_job_task.inference import predict_f001
from src.features.f002_risk.service import get_combined_risk_evidence
from src.features.f003_explanation.service import explain_risk

MODEL_VERSION = "PERSONAL_INDEX_V1"
# 학습된 위험 가중치가 아닌 공개된 정책 가중치. 작업 항목 합계는 30점으로 제한.
TASK_WEIGHTS = {"DRIVING": 10, "NIGHT_SHIFT": 8, "WALKING": 8,
                "CLEANING_TASK": 8, "CARE_TASK": 6, "FACILITY_MAINTENANCE": 8}
LIMITATIONS = [
    "0~100점 참고 지수이며 사고 확률(%)이나 의학적 진단이 아닙니다.",
    "가중치와 등급 경계는 실증 검증 전 정책값이며 개인 사고 결과로 학습·보정되지 않았습니다.",
    "F-001 ML/DL은 제목의 약한 라벨로 학습한 실험 모델이며 실제 작업 조건 확인이 필요합니다.",
    "F-002 산업 매핑 미검수 및 노출인구 분모 부재로 재해 건수는 점수에 가산하지 않습니다.",
    "연령과 건강 입력은 자기보고이며 담당자 검토 없이 채용·배제·안전 판정에 사용할 수 없습니다.",
    "근무 가능 시간은 실제 근무시간이 아닙니다. 8시간 기준 입력 제약 정책만 반영합니다.",
]


class PersonalRiskRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    job_id: str | None = Field(default=None, pattern=r"^[A-Za-z0-9_-]+$", max_length=100)
    title: str = Field(min_length=1, max_length=300)
    age: int = Field(ge=1, le=120)
    physical_level: int = Field(ge=1, le=5)
    chronic_disease: bool
    work_hour_limit: int = Field(ge=1, le=24)

    @field_validator("title")
    @classmethod
    def clean_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("직무 제목은 비어 있을 수 없습니다.")
        return value.strip()


def grade_of(score: int) -> str:
    return "LOW" if score <= 40 else "MID" if score <= 60 else "HIGH"


def calculate_personal_risk(request: PersonalRiskRequest) -> dict:
    analyses = {model: predict_f001(request.title, task_model=model) for model in ("ml", "dl")}
    factors = []

    def add(code, label, points, maximum, basis):
        factors.append({"code": code, "label": label, "points": round(points, 4),
                        "maximum": maximum, "basis": basis})

    add("AGE", "연령 정책", min(20, max(0, request.age - 60) * 20 / 30), 20,
        f"입력 {request.age}세, 60세 이하 0점·90세 이상 20점(선형 정책)")
    add("PHYSICAL", "건강 상태 입력", (request.physical_level - 1) * 25 / 4, 25,
        f"입력 단계 {request.physical_level}/5, 1=좋음·5=나쁨")
    add("CHRONIC", "만성질환 입력", 15 if request.chronic_disease else 0, 15,
        f"자기보고 만성질환 여부: {request.chronic_disease}")
    add("CAPACITY", "근무 가능 시간 제약", max(0, 8 - request.work_hour_limit) * 10 / 7, 10,
        f"입력 {request.work_hour_limit}시간, 8시간 이상 0점·1시간 10점")

    task_basis = []
    task_points = 0.0
    for label, weight in TASK_WEIGHTS.items():
        scores = []
        for model, analysis in analyses.items():
            items = analysis["task_analysis"]["task_characteristics"]
            item = next((item for item in items if item["label"] == label), None)
            if item is None:
                raise ValueError("필수 작업 특성 라벨 누락")
            score = float(item["score"])
            if not isfinite(score) or not 0 <= score <= 1:
                raise ValueError("작업 특성 모델 점수 범위 오류")
            scores.append(score)
        if len(scores) == 2:
            mean = sum(scores) / 2
            task_points += mean * weight
            task_basis.append({"label": label, "ml_score": scores[0], "dl_score": scores[1],
                               "weight": weight, "weighted_points": round(mean * weight, 4)})
    if not task_basis:
        raise ValueError("공통 작업 특성 라벨이 없어 점수를 산출할 수 없습니다.")
    add("TASK", "ML/DL 작업 특성", min(30, task_points), 30,
        "공통 라벨별 ML/DL 평균 모델 점수 × 정책 가중치 합계, 최대 30점")

    # 알려지지 않은 공고는 개인 지수를 막지 않고 통계 부재를 명시한다.
    evidence = None
    explanation = None
    evidence_status = "UNAVAILABLE"
    evidence_note = "외부 공고 ID가 없어 직무 통계 근거를 조회하지 않았습니다."
    if request.job_id:
        try:
            evidence = get_combined_risk_evidence(request.job_id)
            explanation = explain_risk(request.job_id)
            evidence_status = "REFERENCE_ONLY"
            evidence_note = "F-002/F-003 참고 근거 제공, 재해 건수의 점수 기여는 0점입니다."
        except (LookupError, FileNotFoundError, ValueError):
            evidence_note = "해당 공고의 검증 가능한 통계 근거가 없어 통계를 점수에 반영하지 않았습니다."

    score = min(100, max(0, floor(sum(f["points"] for f in factors) + 0.5)))
    grade = grade_of(score)
    return {
        "feature_id": "AI-F-004", "inputs": request.model_dump(),
        "risk_score": score, "risk_grade": grade, "risk_probability": None,
        "score_type": "REFERENCE_INDEX", "model_version": MODEL_VERSION,
        "assessment_status": "SCORED_REVIEW_REQUIRED", "review_required": True,
        "grade_thresholds": {"LOW": "0~40", "MID": "41~60", "HIGH": "61~100"},
        "factors": factors, "task_basis": task_basis, "job_analysis": analyses,
        "evidence": evidence, "explanation": explanation, "evidence_status": evidence_status,
        "summary": f"개인 참고 위험 지수 {score}/100점 ({grade}). 담당자 검토가 필요합니다.",
        "guidance": "점수는 입력 제약과 작업 특성을 요약한 지수입니다. 실제 작업 환경과 입력을 확인하세요.",
        "limitations": LIMITATIONS + [evidence_note],
    }

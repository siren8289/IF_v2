
"""
AI-F-001 통합 추론.

직무 제목 입력
→ 직무군 분류
→ 작업 특성 멀티라벨 예측

실행:
python -m src.features.f001_job_task.predict_f001 "야간 배송기사 모집"
"""

import json
import sys
from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np

from src.features.f001_job_task.predict_task import predict_task
from src.features.f001_job_task.predict_task_dl import predict_task_dl


ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = (
    ROOT / "artifacts" / "f001"
    / "models" / "f001_best_weak.joblib"
)


@lru_cache(maxsize=1)
def load_job_classifier():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"직무군 분류 모델이 없습니다: {MODEL_PATH}"
        )

    # 프로젝트에서 직접 학습한 모델만 로드
    model = joblib.load(MODEL_PATH)

    if not hasattr(model, "predict"):
        raise ValueError("모델에 predict 함수가 없습니다.")

    return model


def predict_job_category(title: str) -> dict:
    model = load_job_classifier()

    category = str(model.predict([title])[0])

    # LinearSVC는 predict_proba를 지원하지 않는다.
    # decision_function 값은 확률이 아니다.
    scores = np.asarray(
        model.decision_function([title])
    )[0]

    classes = model.classes_

    ranked = sorted(
        zip(classes, scores),
        key=lambda item: float(item[1]),
        reverse=True,
    )

    alternatives = [
        {
            "category": str(label),
            "decision_score": round(float(score), 4),
        }
        for label, score in ranked[:3]
    ]

    return {
        "category": category,
        "model_type": "LinearSVC",
        "score_type": "decision_function",
        "alternatives": alternatives,
        "experimental": True,
        "review_required": True,
    }



def predict_f001(title: str, task_model: str = "ml") -> dict:
    """
    AI-F-001 통합 추론.

    task_model:
        ml - Logistic Regression
        dl - PyTorch CharCNN
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("직무 제목을 입력해야 합니다.")

    if task_model not in {"ml", "dl"}:
        raise ValueError(
            "task_model은 'ml' 또는 'dl'이어야 합니다."
        )

    title = title.strip()

    # 직무군 분류는 기존 LinearSVC 유지
    job = predict_job_category(title)

    # 작업 특성 모델만 선택
    if task_model == "ml":
        tasks = predict_task(title)
    else:
        tasks = predict_task_dl(title)

    return {
        "feature_id": "AI-F-001",
        "title": title,
        "job_classification": job,
        "task_analysis": {
            "selected_model": task_model,
            "model_type": tasks["model_type"],
            "task_characteristics": tasks[
                "task_characteristics"
            ],
        },
        "experimental": True,
        "review_required": True,
        "limitations": [
            "키워드 후보 라벨 기반 학습 모델",
            "독립 검수 데이터로 정확도 미검증",
            "제목만으로 실제 작업 조건 확정 불가",
            "위험도 점수는 AI-F-002에서 별도 산정",
        ],
    }




def main():
    args = sys.argv[1:]

    task_model = "ml"

    if args and args[0] in {"ml", "dl"}:
        task_model = args.pop(0)

    title = (
        " ".join(args)
        if args
        else "야간 배송기사 모집"
    )

    result = predict_f001(
        title,
        task_model=task_model,
    )

    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()

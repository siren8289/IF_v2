
"""AI-F-001: 실험용 직무군 예측 및 불확실성 표시."""

from functools import lru_cache
from pathlib import Path

import joblib

ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = (
    ROOT / "artifacts/f001/models/job_classifier_weak.joblib"
)

# 실험용 기준. 검수 데이터로 조정하기 전에는
# 실제 신뢰도나 정확도 기준으로 사용하지 않는다.
REVIEW_SCORE_THRESHOLD = 0.50
REVIEW_MARGIN_THRESHOLD = 0.15


@lru_cache(maxsize=1)
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"모델 파일이 없습니다: {MODEL_PATH}"
        )
    return joblib.load(MODEL_PATH)


def predict_job(title: str) -> dict:
    if not isinstance(title, str) or not title.strip():
        raise ValueError("직무 제목을 입력해야 합니다.")

    title = title.strip()
    model = load_model()

    probabilities = model.predict_proba([title])[0]
    classes = model.classes_

    ranking = sorted(
        zip(classes, probabilities),
        key=lambda item: item[1],
        reverse=True,
    )

    top1 = ranking[0]
    top2 = ranking[1] if len(ranking) > 1 else None

    score = float(top1[1])
    margin = (
        score - float(top2[1])
        if top2 is not None else 1.0
    )

    low_score = score < REVIEW_SCORE_THRESHOLD
    ambiguous = margin < REVIEW_MARGIN_THRESHOLD

    if low_score:
        status = "LOW_SCORE"
    elif ambiguous:
        status = "AMBIGUOUS"
    else:
        status = "CANDIDATE"

    return {
        "title": title,
        "category": str(top1[0]),
        "model_score": round(score, 4),
        "score_margin": round(margin, 4),
        "alternatives": [
            {
                "category": str(category),
                "score": round(float(probability), 4),
            }
            for category, probability in ranking[:3]
        ],
        "model_type": "WEAK_SUPERVISION",
        "review_required": True,
        "status": status,
        "experimental": True,
    }


if __name__ == "__main__":
    titles = [
        "아파트 경비원 모집",
        "의류수거 기사 모집",
        "전기설비 관리기사",
    ]

    for title in titles:
        print(predict_job(title))

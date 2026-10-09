
"""
AI-F-001 작업 특성 멀티라벨 추론.

실행:
python -m src.features.f001_job_task.predict_task

특정 제목:
python -m src.features.f001_job_task.predict_task "야간 배송기사 모집"
"""

import sys
from functools import lru_cache
from pathlib import Path

import joblib


ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = (
    ROOT / "artifacts" / "f001"
    / "models" / "task_multilabel_weak.joblib"
)

# 아직 실제 정답으로 검증되지 않은 모델이므로
# 결과를 확정 판정이 아닌 검토 대상으로 표시한다.
THRESHOLD = 0.5


@lru_cache(maxsize=1)
def load_task_models():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"학습 모델 없음: {MODEL_PATH}"
        )

    # 프로젝트에서 직접 학습해 생성한 신뢰 가능한
    # joblib 파일만 로드해야 한다.
    bundle = joblib.load(MODEL_PATH)

    if not isinstance(bundle, dict):
        raise ValueError("모델 파일 형식이 잘못됐습니다.")

    models = bundle.get("models")

    if not isinstance(models, dict) or not models:
        raise ValueError("학습된 모델이 없습니다.")

    return bundle


def predict_task(title: str) -> dict:
    title = title.strip()

    if not title:
        raise ValueError("직무 제목을 입력하세요.")

    bundle = load_task_models()
    models = bundle["models"]

    results = []

    for label, model in models.items():
        # 학습 시 사용한 LogisticRegression은
        # predict_proba를 지원한다.
        score = float(
            model.predict_proba([title])[0][1]
        )

        results.append({
            "label": label,
            "score": round(score, 4),
            "candidate": score >= THRESHOLD,
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return {
        "title": title,
        "model_type": "WEAK_SUPERVISION",
        "experimental": True,
        "review_required": True,
        "threshold": THRESHOLD,
        "task_characteristics": results,
        "limitations": (
            "제목 기반 키워드 후보 라벨로 학습한 "
            "실험 모델입니다. 점수는 실제 작업 특성의 "
            "확률이나 위험도가 아닙니다."
        ),
    }


def main():
    titles = (
        [" ".join(sys.argv[1:])]
        if len(sys.argv) > 1
        else [
            "아파트 미화원 모집",
            "야간 배송기사 모집",
            "요양보호사 채용",
            "전기설비 관리기사",
            "일반 사무직 모집",
            "의류수거 기사 모집",
        ]
    )

    for title in titles:
        result = predict_task(title)

        print("\n" + "=" * 55)
        print("직무:", result["title"])
        print("실험 모델:", result["model_type"])

        for item in result["task_characteristics"]:
            if item["candidate"]:
                status = "후보"
            else:
                status = "미확정"

            print(
                f"{item['label']:<24} "
                f"{item['score']:.4f}  {status}"
            )

        print("검토 필요:", result["review_required"])


if __name__ == "__main__":
    main()

"""ML 모델: scikit-learn으로 직무 제목에서 작업 특성 점수를 예측한다."""
from pathlib import Path

import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "task_ml.joblib"

# 서버가 켜질 때 한 번만 불러오기 위해 전역 변수에 저장한다.
_models = None


def load_ml_models():
    global _models
    if _models is None:
        bundle = joblib.load(MODEL_PATH)
        _models = bundle["models"]  # {라벨: 학습된 모델}
    return _models


def predict_ml(title):
    """라벨별 점수(0~1)를 딕셔너리로 돌려준다. 예: {"DRIVING": 0.12, ...}"""
    models = load_ml_models()
    scores = {}
    for label, model in models.items():
        probability = model.predict_proba([title])[0][1]
        scores[label] = round(float(probability), 4)
    return scores

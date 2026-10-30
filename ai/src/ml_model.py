"""ML 모델: scikit-learn으로 직무 제목에서 작업 특성 점수를 예측한다.

ML은 Machine Learning, 즉 예전에 사람 손으로 답을 달아 둔 데이터로
규칙을 익힌 모델이다. 여기서는 제목 문장을 보고
"운전이 들어갈 가능성", "야간 근무일 가능성" 같은 점수를 0~1로 낸다.

학습된 파일은 ai/models/task_ml.joblib 이다. 이 파일은 예측만 하고 다시 학습하지 않는다.
"""
from pathlib import Path

# joblib: 학습이 끝난 파이썬 객체를 파일로 저장하고 다시 읽는 도구.
import joblib

# 이 파일(src/ml_model.py) 기준으로 두 칸 위(ai/)의 models 폴더를 가리킨다.
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "task_ml.joblib"

# 서버가 켜질 때 한 번만 불러오기 위해 전역 변수에 저장한다.
# 요청마다 파일을 다시 읽으면 느리다.
_models = None


def load_ml_models():
    """모델 묶음을 메모리에 올린다. 이미 올렸으면 그대로 돌려준다."""
    global _models
    if _models is None:
        # 파일 안에는 {"models": {라벨: 학습된 분류기}} 형태로 들어 있다.
        bundle = joblib.load(MODEL_PATH)
        _models = bundle["models"]  # {라벨: 학습된 모델}
    return _models


def predict_ml(title):
    """라벨별 점수(0~1)를 딕셔너리로 돌려준다. 예: {"DRIVING": 0.12, ...}

    1에 가까울수록 그 직무에 그 작업이 들어 있다고 본 것이다.
    """
    models = load_ml_models()
    scores = {}
    for label, model in models.items():
        # predict_proba는 [그 특성이 아님, 그 특성임] 두 확률을 준다.
        # [0]은 이번 제목 한 건, [1]은 "맞다" 쪽 확률이다.
        probability = model.predict_proba([title])[0][1]
        # 소수점 넷째 자리까지만 남겨 응답을 짧게 한다.
        scores[label] = round(float(probability), 4)
    return scores

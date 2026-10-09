"""AI-F-001 직무군 및 작업 특성 ML/DL 통합 추론.

노트북은 실험, training.py는 학습, 이 파일은 API에서 사용하는 추론만 담당.
모델은 이 기능의 artifacts/ 폴더에서 읽는다.
"""
from functools import lru_cache
from pathlib import Path
import joblib
import numpy as np
import torch
from .train_task_dl import TaskCNN, encode_title

FEATURE_DIR = Path(__file__).resolve().parent
REVIEW_SCORE_THRESHOLD = 0.50
REVIEW_MARGIN_THRESHOLD = 0.15
THRESHOLD = 0.5

JOB_WEAK_PATH = FEATURE_DIR / "artifacts/models/job_classifier_weak.joblib"
JOB_BEST_PATH = FEATURE_DIR / "artifacts/models/f001_best_weak.joblib"
TASK_ML_PATH = FEATURE_DIR / "artifacts/models/task_multilabel_weak.joblib"
TASK_DL_PATH = FEATURE_DIR / "artifacts/comparison/task_cnn_best.pt"

@lru_cache(maxsize=1)
def load_model():
    if not JOB_WEAK_PATH.exists():
        raise FileNotFoundError(
            f"모델 파일이 없습니다: {JOB_WEAK_PATH}"
        )
    return joblib.load(JOB_WEAK_PATH)


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

@lru_cache(maxsize=1)
def load_task_models():
    if not TASK_ML_PATH.exists():
        raise FileNotFoundError(
            f"학습 모델 없음: {TASK_ML_PATH}"
        )

    # 프로젝트에서 직접 학습해 생성한 신뢰 가능한
    # joblib 파일만 로드해야 한다.
    bundle = joblib.load(TASK_ML_PATH)

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


@lru_cache(maxsize=1)
def load_dl_model():
    if not TASK_DL_PATH.exists():
        raise FileNotFoundError(
            f"DL 모델 파일 없음: {TASK_DL_PATH}"
        )

    # 프로젝트에서 직접 생성한 체크포인트만 사용
    checkpoint = torch.load(
        TASK_DL_PATH,
        map_location="cpu",
        weights_only=True,
    )

    vocab = checkpoint["vocab"]
    labels = checkpoint["labels"]
    max_length = checkpoint["max_length"]

    model = TaskCNN(
        vocab_size=len(vocab) + 2,
        num_labels=len(labels),
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.eval()

    return model, vocab, labels, max_length


def predict_task_dl(title: str) -> dict:
    if not isinstance(title, str) or not title.strip():
        raise ValueError("직무 제목을 입력하세요.")

    title = title.strip()

    model, vocab, labels, max_length = load_dl_model()

    # 기존 encode_title 함수는 MAX_LENGTH=100 사용
    if max_length != 100:
        raise ValueError(
            f"지원하지 않는 max_length: {max_length}"
        )

    encoded = encode_title(title, vocab)

    x = torch.tensor(
        [encoded],
        dtype=torch.long,
    )

    with torch.inference_mode():
        logits = model(x)
        scores = torch.sigmoid(logits)[0].tolist()

    characteristics = []

    for label, score in zip(labels, scores):
        characteristics.append({
            "label": label,
            "score": round(float(score), 4),
            "candidate": score >= 0.5,
        })

    characteristics.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return {
        "title": title,
        "model_type": "PyTorch_CharCNN",
        "label_source": "KEYWORD_CANDIDATE_WEAK",
        "experimental": True,
        "review_required": True,
        "task_characteristics": characteristics,
        "limitations": (
            "키워드 후보 라벨 기반 실험 모델이며 "
            "점수는 실제 작업 특성의 확률이나 "
            "위험도를 의미하지 않습니다."
        ),
    }

@lru_cache(maxsize=1)
def load_job_classifier():
    if not JOB_BEST_PATH.exists():
        raise FileNotFoundError(
            f"직무군 분류 모델이 없습니다: {JOB_BEST_PATH}"
        )

    # 프로젝트에서 직접 학습한 모델만 로드
    model = joblib.load(JOB_BEST_PATH)

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





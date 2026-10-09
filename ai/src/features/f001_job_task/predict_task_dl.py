
"""
AI-F-001 PyTorch CharCNN 추론.

실행:
python -m src.features.f001_job_task.predict_task_dl "야간 배송기사 모집"
"""

import json
import sys
from functools import lru_cache
from pathlib import Path

import torch

from src.features.f001_job_task.train_task_dl import (
    TaskCNN,
    encode_title,
)


ROOT = Path(__file__).resolve().parents[3]

MODEL_PATH = (
    ROOT
    / "artifacts"
    / "f001"
    / "comparison"
    / "task_cnn_best.pt"
)


@lru_cache(maxsize=1)
def load_dl_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"DL 모델 파일 없음: {MODEL_PATH}"
        )

    # 프로젝트에서 직접 생성한 체크포인트만 사용
    checkpoint = torch.load(
        MODEL_PATH,
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


if __name__ == "__main__":
    title = (
        " ".join(sys.argv[1:])
        if len(sys.argv) > 1
        else "야간 배송기사 모집"
    )

    result = predict_task_dl(title)

    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
    ))


"""
AI-F-001 PyTorch 문자 CNN 멀티라벨 학습.

실행:
python -m src.features.f001_job_task.train_task_dl

출력:
artifacts/f001/models/task_cnn_weak.pt
artifacts/f001/models/task_cnn_metrics.csv
artifacts/f001/models/task_cnn_history.csv

주의:
키워드 후보 라벨을 이용한 실험용 모델.
미탐지 라벨을 비교용 0으로 사용하므로
실제 작업 특성 부재를 의미하지 않는다.
"""

import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from torch import nn
from torch.utils.data import Dataset, DataLoader
from .model import TaskCNN, encode_title
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score,
)


FEATURE_DIR = Path(__file__).resolve().parent
DATA_DIR = FEATURE_DIR / "artifacts"
MODEL_DIR = DATA_DIR / "models"

LABELS = [
    "CLEANING_TASK",
    "CARE_TASK",
    "DRIVING",
    "FACILITY_MAINTENANCE",
    "NIGHT_SHIFT",
    "OFFICE_TASK",
    "WALKING",
]

MAX_LENGTH = 100
BATCH_SIZE = 64
EPOCHS = 12
SEED = 42


def set_seed():
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)


def parse_labels(value):
    try:
        labels = json.loads(value)
        return labels if isinstance(labels, list) else []
    except (TypeError, ValueError):
        return []


def load_data():
    path = DATA_DIR / "task_label_candidates.csv"

    df = pd.read_csv(path, dtype=str).fillna("")

    required = {"title", "candidate_labels"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"컬럼 누락: {sorted(missing)}")

    df["title"] = df["title"].str.strip()
    df["labels"] = df["candidate_labels"].apply(parse_labels)

    # 기존 ML 실험과 동일하게 후보가 있는 제목만 사용
    df = df[
        df["title"].ne("")
        & df["labels"].apply(bool)
    ].copy()

    # 동일 제목의 후보 라벨 통합
    df = (
        df.groupby("title", as_index=False)["labels"]
        .agg(lambda groups: sorted({
            label
            for group in groups
            for label in group
        }))
    )

    return df


def build_vocab(titles):
    chars = sorted(set("".join(titles)))

    # 0=PAD, 1=UNK
    return {
        char: idx + 2
        for idx, char in enumerate(chars)
    }


class TaskDataset(Dataset):
    def __init__(self, frame, vocab):
        self.x = torch.tensor(
            [
                encode_title(title, vocab)
                for title in frame["title"]
            ],
            dtype=torch.long,
        )

        self.y = torch.tensor(
            [
                [
                    int(label in labels)
                    for label in LABELS
                ]
                for labels in frame["labels"]
            ],
            dtype=torch.float32,
        )

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        return self.x[index], self.y[index]


def evaluate(model, loader, device):
    model.eval()

    true_batches = []
    prob_batches = []

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            logits = model(x)
            probs = torch.sigmoid(logits)

            true_batches.append(y.numpy())
            prob_batches.append(probs.cpu().numpy())

    true = np.vstack(true_batches)
    probs = np.vstack(prob_batches)
    predicted = (probs >= 0.5).astype(int)

    return true, predicted


def main():
    set_seed()
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    df = load_data()

    # 제목 기준 중복 제거 후 분리
    train_df, test_df = train_test_split(
        df,
        test_size=0.25,
        random_state=SEED,
        shuffle=True,
    )

    # 어휘는 학습 데이터에서만 구성
    vocab = build_vocab(train_df["title"])

    train_loader = DataLoader(
        TaskDataset(train_df, vocab),
        batch_size=BATCH_SIZE,
        shuffle=True,
    )

    test_loader = DataLoader(
        TaskDataset(test_df, vocab),
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    device = torch.device(
        "mps" if torch.backends.mps.is_available()
        else "cpu"
    )

    model = TaskCNN(
        vocab_size=len(vocab) + 2,
        num_labels=len(LABELS),
    ).to(device)

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=0.001,
    )

    # 후보 라벨 기준 불균형 보정
    train_targets = TaskDataset(train_df, vocab).y

    positive = train_targets.sum(dim=0)
    negative = len(train_targets) - positive

    pos_weight = (
        negative / positive.clamp(min=1)
    ).clamp(max=30).to(device)

    criterion = nn.BCEWithLogitsLoss(
        pos_weight=pos_weight
    )

    history = []

    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0.0

        for x, y in train_loader:
            x = x.to(device)
            y = y.to(device)

            optimizer.zero_grad()

            logits = model(x)
            loss = criterion(logits, y)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(
            f"Epoch {epoch:02d}/{EPOCHS} "
            f"Loss={total_loss / len(train_loader):.4f}"
        )

        history.append({
            "epoch": epoch,
            "train_loss": total_loss / len(train_loader),
        })

    true, predicted = evaluate(
        model, test_loader, device
    )

    metrics = []

    for index, label in enumerate(LABELS):
        metrics.append({
            "label": label,
            "precision_weak": precision_score(
                true[:, index],
                predicted[:, index],
                zero_division=0,
            ),
            "recall_weak": recall_score(
                true[:, index],
                predicted[:, index],
                zero_division=0,
            ),
            "f1_weak": f1_score(
                true[:, index],
                predicted[:, index],
                zero_division=0,
            ),
        })

    torch.save({
        "model_state_dict": model.cpu().state_dict(),
        "vocab": vocab,
        "labels": LABELS,
        "max_length": MAX_LENGTH,
        "model_type": "CHAR_CNN_WEAK",
        "experimental": True,
    }, MODEL_DIR / "task_cnn_weak.pt")

    pd.DataFrame(metrics).to_csv(
        MODEL_DIR / "task_cnn_metrics.csv",
        index=False,
        encoding="utf-8-sig",
    )

    pd.DataFrame(history).to_csv(
        MODEL_DIR / "task_cnn_history.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("\nAI-F-001 PyTorch 학습 완료")
    print("학습 제목:", len(train_df))
    print("평가 제목:", len(test_df))
    print("장치:", device)
    print(pd.DataFrame(metrics).to_string(index=False))


if __name__ == "__main__":
    main()

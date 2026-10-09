
"""
AI-F-001 ML vs DL 공통 데이터 비교.

실행:
python -m src.features.f001_job_task.compare_task_models

결과:
artifacts/f001/comparison/
  split.csv
  metrics.csv
  predictions.csv
  errors.csv
  dl_history.csv

기존 모델 파일은 덮어쓰지 않는다.
Weak Label 실험이며 실제 정확도 검증이 아니다.
"""

import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from torch import nn
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    multilabel_confusion_matrix,
)

from src.features.f001_job_task.train_task_dl import (
    LABELS,
    MAX_LENGTH,
    TaskCNN,
    TaskDataset,
    build_vocab,
    parse_labels,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "artifacts/f001/task_label_candidates.csv"
OUT = ROOT / "artifacts/f001/comparison"

SEED = 42
EPOCHS = 12
BATCH_SIZE = 64


def seed_everything():
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)


def load_data():
    df = pd.read_csv(SOURCE, dtype=str).fillna("")

    required = {"title", "candidate_labels"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"컬럼 누락: {sorted(missing)}")

    df["title"] = df["title"].str.strip()
    df["labels"] = df["candidate_labels"].apply(parse_labels)

    # 기존 ML·DL 실험과 같은 후보 데이터 범위
    df = df[
        df["title"].ne("")
        & df["labels"].apply(bool)
    ].copy()

    # 같은 제목은 하나의 데이터로 통합
    df = (
        df.groupby("title", as_index=False)["labels"]
        .agg(
            lambda groups: sorted({
                label
                for group in groups
                for label in group
            })
        )
    )

    if len(df) < 100:
        raise ValueError("비교할 데이터가 부족합니다.")

    return df


def targets(df):
    return np.asarray(
        [
            [int(label in labels) for label in LABELS]
            for labels in df["labels"]
        ],
        dtype=np.int64,
    )


def split_data(df):
    # 동일 제목 중복 제거 후 한 번만 분할
    train_val, test = train_test_split(
        df,
        test_size=0.20,
        random_state=SEED,
        shuffle=True,
    )

    train, val = train_test_split(
        train_val,
        test_size=0.125,
        random_state=SEED,
        shuffle=True,
    )

    # Train 70%, Validation 10%, Test 20%
    return train, val, test


def train_ml(train, val, test):
    """
    라벨별 이진 분류기.
    모든 라벨이 같은 Train/Test 제목을 사용한다.
    """

    y_train = targets(train)
    y_val = targets(val)
    y_test = targets(test)

    val_probs = np.zeros_like(y_val, dtype=float)
    test_probs = np.zeros_like(y_test, dtype=float)

    for i, label in enumerate(LABELS):
        if len(np.unique(y_train[:, i])) < 2:
            raise ValueError(
                f"{label}: 학습 데이터에 한 클래스만 존재"
            )

        model = Pipeline([
            ("tfidf", TfidfVectorizer(
                analyzer="char",
                ngram_range=(2, 4),
                max_features=30000,
                sublinear_tf=True,
            )),
            ("classifier", LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=SEED,
            )),
        ])

        model.fit(train["title"], y_train[:, i])

        val_probs[:, i] = model.predict_proba(
            val["title"]
        )[:, 1]

        test_probs[:, i] = model.predict_proba(
            test["title"]
        )[:, 1]

    return val_probs, test_probs


def predict_dl(model, loader, device):
    model.eval()
    outputs = []

    with torch.no_grad():
        for x, _ in loader:
            logits = model(x.to(device))
            outputs.append(
                torch.sigmoid(logits).cpu().numpy()
            )

    return np.vstack(outputs)


def train_dl(train, val, test):
    # 어휘는 Train 데이터에서만 학습
    vocab = build_vocab(train["title"])

    train_data = TaskDataset(train, vocab)
    val_data = TaskDataset(val, vocab)
    test_data = TaskDataset(test, vocab)

    train_loader = DataLoader(
        train_data,
        batch_size=BATCH_SIZE,
        shuffle=True,
    )
    val_loader = DataLoader(
        val_data,
        batch_size=BATCH_SIZE,
        shuffle=False,
    )
    test_loader = DataLoader(
        test_data,
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

    positive = train_data.y.sum(dim=0)
    negative = len(train_data) - positive

    pos_weight = (
        negative / positive.clamp(min=1)
    ).clamp(max=30).to(device)

    criterion = nn.BCEWithLogitsLoss(
        pos_weight=pos_weight
    )

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=0.001,
    )

    history = []
    best_loss = float("inf")
    best_state = None

    for epoch in range(1, EPOCHS + 1):
        model.train()
        losses = []

        for x, y in train_loader:
            x = x.to(device)
            y = y.to(device)

            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)

            loss.backward()
            optimizer.step()

            losses.append(float(loss.item()))

        model.eval()
        val_losses = []

        with torch.no_grad():
            for x, y in val_loader:
                x = x.to(device)
                y = y.to(device)

                loss = criterion(model(x), y)
                val_losses.append(float(loss.item()))

        train_loss = float(np.mean(losses))
        val_loss = float(np.mean(val_losses))

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
        })

        print(
            f"DL Epoch {epoch:02d}/{EPOCHS} "
            f"train={train_loss:.4f} "
            f"val={val_loss:.4f}"
        )

        # 최적 Epoch 선택에는 Validation만 사용
        if val_loss < best_loss:
            best_loss = val_loss
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }

    if best_state is None:
        raise RuntimeError("DL 학습 실패")

    model.load_state_dict(best_state)

    # Validation Loss 기준 최적 모델 저장
    torch.save(
        {
            "model_state_dict": {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            },
            "vocab": vocab,
            "labels": LABELS,
            "max_length": MAX_LENGTH,
            "model_type": "CHAR_CNN_WEAK",
            "selection_metric": "validation_loss",
            "experimental": True,
            "label_source": "KEYWORD_CANDIDATE_WEAK",
        },
        OUT / "task_cnn_best.pt",
    )

    val_probs = predict_dl(model, val_loader, device)
    test_probs = predict_dl(model, test_loader, device)

    return val_probs, test_probs, history


def choose_thresholds(y_val, probs):
    """
    Validation에서만 라벨별 임계값 결정.
    Test 결과를 보고 임계값을 변경하지 않는다.
    """

    thresholds = []

    for i in range(len(LABELS)):
        best_threshold = 0.5
        best_f1 = -1.0

        for threshold in np.arange(0.2, 0.81, 0.05):
            predicted = (
                probs[:, i] >= threshold
            ).astype(int)

            score = f1_score(
                y_val[:, i],
                predicted,
                zero_division=0,
            )

            if score > best_f1:
                best_f1 = score
                best_threshold = float(threshold)

        thresholds.append(best_threshold)

    return np.asarray(thresholds)


def evaluate(name, test, probabilities, thresholds):
    y_true = targets(test)
    y_pred = (
        probabilities >= thresholds[None, :]
    ).astype(int)

    rows = []
    predictions = []

    matrices = multilabel_confusion_matrix(
        y_true, y_pred
    )

    for i, label in enumerate(LABELS):
        tn, fp, fn, tp = matrices[i].ravel()

        rows.append({
            "model": name,
            "label": label,
            "precision_weak": precision_score(
                y_true[:, i], y_pred[:, i],
                zero_division=0,
            ),
            "recall_weak": recall_score(
                y_true[:, i], y_pred[:, i],
                zero_division=0,
            ),
            "f1_weak": f1_score(
                y_true[:, i], y_pred[:, i],
                zero_division=0,
            ),
            "threshold": thresholds[i],
            "tp": int(tp),
            "fp": int(fp),
            "fn": int(fn),
            "tn": int(tn),
        })

    for idx, title in enumerate(test["title"]):
        for i, label in enumerate(LABELS):
            predictions.append({
                "model": name,
                "title": title,
                "label": label,
                "weak_label": int(y_true[idx, i]),
                "predicted": int(y_pred[idx, i]),
                "score": float(probabilities[idx, i]),
                "correct_vs_weak": bool(
                    y_true[idx, i] == y_pred[idx, i]
                ),
            })

    return rows, predictions


def main():
    seed_everything()
    OUT.mkdir(parents=True, exist_ok=True)

    df = load_data()
    train, val, test = split_data(df)

    split = pd.concat([
        train.assign(split="train"),
        val.assign(split="validation"),
        test.assign(split="test"),
    ])

    split["labels"] = split["labels"].apply(
        lambda x: json.dumps(x, ensure_ascii=False)
    )

    split.to_csv(
        OUT / "split.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print(
        f"Train={len(train)}, "
        f"Validation={len(val)}, "
        f"Test={len(test)}"
    )

    ml_val, ml_test = train_ml(train, val, test)
    dl_val, dl_test, history = train_dl(
        train, val, test
    )

    y_val = targets(val)

    ml_thresholds = choose_thresholds(
        y_val, ml_val
    )
    dl_thresholds = choose_thresholds(
        y_val, dl_val
    )

    ml_metrics, ml_predictions = evaluate(
        "LogisticRegression",
        test,
        ml_test,
        ml_thresholds,
    )

    dl_metrics, dl_predictions = evaluate(
        "PyTorch_CharCNN",
        test,
        dl_test,
        dl_thresholds,
    )

    metrics = pd.DataFrame(
        ml_metrics + dl_metrics
    )
    predictions = pd.DataFrame(
        ml_predictions + dl_predictions
    )

    metrics.to_csv(
        OUT / "metrics.csv",
        index=False,
        encoding="utf-8-sig",
    )

    predictions.to_csv(
        OUT / "predictions.csv",
        index=False,
        encoding="utf-8-sig",
    )

    predictions[
        ~predictions["correct_vs_weak"]
    ].to_csv(
        OUT / "errors.csv",
        index=False,
        encoding="utf-8-sig",
    )

    pd.DataFrame(history).to_csv(
        OUT / "dl_history.csv",
        index=False,
        encoding="utf-8-sig",
    )

    summary = (
        metrics.groupby("model")["f1_weak"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nAI-F-001 ML vs DL 비교 완료")
    print("-" * 45)
    print("Macro Weak F1:")
    print(summary.to_string())
    print("\n라벨별 F1:")
    print(
        metrics.pivot(
            index="label",
            columns="model",
            values="f1_weak",
        ).round(4).to_string()
    )
    print("\n결과:", OUT)
    print(
        "주의: 키워드 후보 라벨과의 일치도이며 "
        "실제 작업 특성 정확도가 아닙니다."
    )


if __name__ == "__main__":
    main()

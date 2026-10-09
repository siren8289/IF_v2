
import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"
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


def parse_labels(value):
    try:
        labels = json.loads(value)
        return labels if isinstance(labels, list) else []
    except (ValueError, TypeError):
        return []


def make_model():
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="char",
            ngram_range=(2, 4),
            max_features=30000,
            sublinear_tf=True,
        )),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        )),
    ])


def main():
    path = DATA_DIR / "task_label_candidates.csv"

    df = pd.read_csv(path, dtype=str).fillna("")

    df["labels"] = df["candidate_labels"].apply(parse_labels)
    df["title"] = df["title"].str.strip()

    df = df[
        df["title"].ne("")
        & df["labels"].apply(bool)
    ].copy()

    # 동일 제목에 서로 다른 후보가 있으면 합집합으로 통합
    df = (
        df.groupby("title", as_index=False)["labels"]
        .agg(lambda groups: sorted({
            label
            for group in groups
            for label in group
        }))
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    models = {}
    metrics = []

    for label in LABELS:
        # 다른 라벨 후보를 가진 제목을 비교용 음성으로 사용.
        # 실제 음성 정답은 아니므로 실험용으로만 활용.
        y = df["labels"].apply(
            lambda labels: int(label in labels)
        )

        positives = int(y.sum())
        negatives = int((y == 0).sum())

        if min(positives, negatives) < 20:
            print(f"SKIP {label}: 후보 부족")
            continue

        X_train, X_test, y_train, y_test = train_test_split(
            df["title"],
            y,
            test_size=0.25,
            random_state=42,
            stratify=y,
        )

        evaluation_model = make_model()
        evaluation_model.fit(X_train, y_train)
        predicted = evaluation_model.predict(X_test)

        row = {
            "label": label,
            "positive_candidates": positives,
            "comparison_candidates": negatives,
            "precision_weak": precision_score(
                y_test, predicted, zero_division=0
            ),
            "recall_weak": recall_score(
                y_test, predicted, zero_division=0
            ),
            "f1_weak": f1_score(
                y_test, predicted, zero_division=0
            ),
        }

        metrics.append(row)

        final_model = make_model()
        final_model.fit(df["title"], y)
        models[label] = final_model

        print(
            f"{label}: "
            f"F1(weak)={row['f1_weak']:.4f}"
        )

    if not models:
        print("학습 가능한 라벨이 없습니다.")
        return

    joblib.dump({
        "models": models,
        "labels": list(models),
        "model_type": "WEAK_SUPERVISION",
        "experimental": True,
        "label_source": "KEYWORD_CANDIDATE_WEAK",
    }, MODEL_DIR / "task_multilabel_weak.joblib")

    pd.DataFrame(metrics).to_csv(
        MODEL_DIR / "task_weak_metrics.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("\n실험용 작업 특성 모델 학습 완료")
    print("학습 라벨:", list(models))
    print("모델:", MODEL_DIR / "task_multilabel_weak.joblib")


if __name__ == "__main__":
    main()

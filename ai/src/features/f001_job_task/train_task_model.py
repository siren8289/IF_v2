
"""
AI-F-001 작업 특성 멀티라벨 ML 학습.

입력:
artifacts/f001/task_review_sample.csv

출력:
artifacts/f001/models/task_multilabel.joblib
artifacts/f001/models/task_model_metrics.csv

주의:
review_* 컬럼의 1/0만 학습.
? 는 미확인으로 간주하며 학습에서 제외.
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"
MODEL_DIR = DATA_DIR / "models"

INPUT_FILE = DATA_DIR / "task_review_queue.csv"

MIN_POSITIVE = 5
MIN_NEGATIVE = 5


def build_model():
    """직무 제목 기반 작업 특성 이진 분류기."""
    return Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                analyzer="char",
                ngram_range=(2, 4),
                max_features=30000,
                sublinear_tf=True,
            ),
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ])


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(INPUT_FILE)

    df = pd.read_csv(
        INPUT_FILE, dtype=str
    ).fillna("")

    if "title" not in df.columns:
        raise ValueError("title 컬럼이 없습니다.")

    review_columns = [
        col for col in df.columns
        if col.startswith("review_")
        and col != "review_status"
        and col != "review_note"
    ]

    if not review_columns:
        raise ValueError("review_* 라벨 컬럼이 없습니다.")

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    trained_models = {}
    results = []

    for column in review_columns:
        label = column.removeprefix("review_")

        # 검수된 1/0만 학습 대상으로 사용
        subset = df[
            df[column].isin(["0", "1"])
            & df["title"].str.strip().ne("")
        ].copy()

        # 동일 제목의 라벨이 충돌하면 제외
        conflicts = (
            subset.groupby("title")[column].nunique()
        )
        conflict_titles = conflicts[
            conflicts > 1
        ].index

        subset = subset[
            ~subset["title"].isin(conflict_titles)
        ].drop_duplicates(subset=["title"])

        counts = subset[column].value_counts()

        positive = int(counts.get("1", 0))
        negative = int(counts.get("0", 0))

        print(f"\n[{label}]")
        print(
            f"검수 데이터={len(subset)}, "
            f"양성={positive}, 음성={negative}"
        )

        if (
            positive < MIN_POSITIVE
            or negative < MIN_NEGATIVE
        ):
            print("SKIP: 검수된 양성/음성 데이터 부족")

            results.append({
                "label": label,
                "status": "SKIPPED",
                "positive": positive,
                "negative": negative,
                "accuracy": None,
                "precision": None,
                "recall": None,
                "f1": None,
            })
            continue

        X = subset["title"]
        y = subset[column].astype(int)

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.25,
                random_state=42,
                stratify=y,
            )
        )

        evaluation_model = build_model()
        evaluation_model.fit(X_train, y_train)

        predicted = evaluation_model.predict(X_test)

        metrics = {
            "label": label,
            "status": "TRAINED",
            "positive": positive,
            "negative": negative,
            "accuracy": accuracy_score(
                y_test, predicted
            ),
            "precision": precision_score(
                y_test, predicted,
                zero_division=0,
            ),
            "recall": recall_score(
                y_test, predicted,
                zero_division=0,
            ),
            "f1": f1_score(
                y_test, predicted,
                zero_division=0,
            ),
        }

        results.append(metrics)

        # 배포 후보 모델은 전체 검수 데이터로 재학습
        final_model = build_model()
        final_model.fit(X, y)

        trained_models[label] = final_model

        print(
            f"Accuracy={metrics['accuracy']:.4f} "
            f"F1={metrics['f1']:.4f}"
        )

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        MODEL_DIR / "task_model_metrics.csv",
        index=False,
        encoding="utf-8-sig",
    )

    if not trained_models:
        print("\n학습된 모델 없음")
        print("검수 CSV에서 1/0 라벨을 먼저 입력하세요.")
        return

    joblib.dump(
        {
            "models": trained_models,
            "labels": list(trained_models.keys()),
            "model_type": "MULTILABEL_BINARY_RELEVANCE",
            "input": "job_title",
            "label_source": "HUMAN_REVIEW",
            "experimental": True,
        },
        MODEL_DIR / "task_multilabel.joblib",
    )

    print("\nAI-F-001 작업 특성 모델 학습 완료")
    print("-" * 45)
    print("학습된 라벨:", len(trained_models))
    print("저장 경로:", MODEL_DIR)
    print(results_df.to_string(index=False))


if __name__ == "__main__":
    main()

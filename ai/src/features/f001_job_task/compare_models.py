
"""
AI-F-001 ML 모델 비교 학습.

실행:
python -m src.features.f001_job_task.compare_models

입력:
artifacts/f001/job_label_review.csv

출력:
artifacts/f001/models/f001_best_weak.joblib
artifacts/f001/models/model_comparison.csv
artifacts/f001/models/error_analysis.csv
artifacts/f001/models/confusion_matrix.csv

주의:
후보 라벨은 정답이 아니며, 평가 결과는
규칙 기반 후보와의 일치 정도만 나타낸다.
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"
MODEL_DIR = DATA_DIR / "models"

VALID_LABELS = {
    "CLEANING", "SECURITY", "CARE",
    "OFFICE", "MANUFACTURING", "FACILITY",
    "DRIVING", "KITCHEN", "SALES",
    "AGRICULTURE",
}


def load_data():
    path = DATA_DIR / "job_label_review.csv"

    if not path.exists():
        raise FileNotFoundError(path)

    df = pd.read_csv(path, dtype=str).fillna("")

    required = {"title", "candidate_category"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"필수 컬럼 누락: {sorted(missing)}"
        )

    df["title"] = df["title"].str.strip()
    df["candidate_category"] = (
        df["candidate_category"].str.strip().str.upper()
    )

    df = df[
        df["title"].ne("")
        & df["candidate_category"].isin(VALID_LABELS)
    ].copy()

    # 동일 제목에 서로 다른 라벨이 붙은 경우 제외
    conflicts = (
        df.groupby("title")["candidate_category"].nunique()
    )
    conflict_titles = conflicts[conflicts > 1].index

    df = df[
        ~df["title"].isin(conflict_titles)
    ].drop_duplicates(subset=["title"])

    # 학습과 평가가 가능한 클래스만 사용
    counts = df["candidate_category"].value_counts()
    eligible = counts[counts >= 5].index

    df = df[
        df["candidate_category"].isin(eligible)
    ].copy()

    if len(df) < 30 or df["candidate_category"].nunique() < 2:
        raise ValueError(
            "학습 가능한 데이터가 부족합니다."
        )

    return df


def build_models():
    def vectorizer():
        return TfidfVectorizer(
            analyzer="char",
            ngram_range=(2, 4),
            max_features=30000,
            sublinear_tf=True,
        )

    return {
        "LogisticRegression": Pipeline([
            ("tfidf", vectorizer()),
            ("classifier", LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            )),
        ]),
        "LinearSVC": Pipeline([
            ("tfidf", vectorizer()),
            ("classifier", LinearSVC(
                class_weight="balanced",
                random_state=42,
            )),
        ]),
    }


def main():
    df = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        df["title"],
        df["candidate_category"],
        test_size=0.25,
        random_state=42,
        stratify=df["candidate_category"],
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    trained_models = {}

    for name, model in build_models().items():
        model.fit(X_train, y_train)
        predicted = model.predict(X_test)

        accuracy = accuracy_score(y_test, predicted)
        macro_f1 = f1_score(
            y_test, predicted,
            average="macro",
            zero_division=0,
        )

        results.append({
            "model": name,
            "accuracy": accuracy,
            "macro_f1": macro_f1,
            "train_rows": len(X_train),
            "test_rows": len(X_test),
            "label_source": "KEYWORD_CANDIDATE_WEAK",
        })

        trained_models[name] = model

        print(f"\n{name}")
        print(classification_report(
            y_test, predicted, zero_division=0
        ))

    comparison = pd.DataFrame(results)
    comparison = comparison.sort_values(
        "macro_f1", ascending=False
    )

    best_name = comparison.iloc[0]["model"]
    best_model = trained_models[best_name]

    # 최종 모델은 전체 후보 데이터로 재학습.
    # 평가 점수는 위의 분리된 테스트셋 결과.
    best_model.fit(
        df["title"],
        df["candidate_category"],
    )

    joblib.dump(
        best_model,
        MODEL_DIR / "f001_best_weak.joblib",
    )

    # 오분류 분석은 테스트셋에서만 수행
    evaluation_model = trained_models[best_name]

    # 위에서 전체 데이터 재학습했으므로
    # 독립 평가를 위해 동일 구조를 새로 학습
    evaluation_model = build_models()[best_name]
    evaluation_model.fit(X_train, y_train)
    predictions = evaluation_model.predict(X_test)

    errors = pd.DataFrame({
        "title": X_test.to_numpy(),
        "actual_candidate": y_test.to_numpy(),
        "predicted": predictions,
    })
    errors["is_error"] = (
        errors["actual_candidate"] != errors["predicted"]
    )

    labels = sorted(df["candidate_category"].unique())
    matrix = confusion_matrix(
        y_test, predictions, labels=labels
    )

    comparison.to_csv(
        MODEL_DIR / "model_comparison.csv",
        index=False,
        encoding="utf-8-sig",
    )

    errors[errors["is_error"]].to_csv(
        MODEL_DIR / "error_analysis.csv",
        index=False,
        encoding="utf-8-sig",
    )

    pd.DataFrame(
        matrix, index=labels, columns=labels
    ).to_csv(
        MODEL_DIR / "confusion_matrix.csv",
        encoding="utf-8-sig",
    )

    print("\nAI-F-001 모델 비교 완료")
    print("-" * 45)
    print(comparison.to_string(index=False))
    print("\n선택 모델:", best_name)
    print("학습 후보 고유 제목:", len(df))
    print("저장 경로:", MODEL_DIR)
    print("주의: 실제 정답 라벨 기반 성능이 아님")


if __name__ == "__main__":
    main()

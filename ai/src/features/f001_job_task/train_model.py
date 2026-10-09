
"""
AI-F-001: 검수된 직무 제목으로 ML 모델 학습.

실행:
python -m src.features.f001_job_task.train_model
python -m src.features.f001_job_task.train_model --use-candidate-labels

--use-candidate-labels는 검수 전 파이프라인 점검용이다.
approved_label이 없는 행에 키워드 후보(candidate_category)를
약한 라벨로 사용하며, 평가 결과는 실제 성능이 아니다.

입력:
artifacts/f001/job_label_review.csv

출력:
artifacts/f001/models/job_classifier.joblib
artifacts/f001/models/evaluation.json
"""

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"
MODEL_DIR = DATA_DIR / "models"

VALID_LABELS = {
    "CLEANING", "SECURITY", "CARE",
    "OFFICE", "MANUFACTURING", "FACILITY",
    "DRIVING", "KITCHEN", "SALES",
    "AGRICULTURE",
}


def load_reviewed_data(use_candidate_labels=False):
    path = DATA_DIR / "job_label_review.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"검수 파일이 없습니다: {path}"
        )

    df = pd.read_csv(path, dtype=str).fillna("")

    required = {"job_id", "title", "approved_label"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"필수 컬럼 누락: {missing}")

    # 사람이 확정한 라벨만 학습에 사용한다.
    df["approved_label"] = (
        df["approved_label"].str.strip().str.upper()
    )

    if use_candidate_labels and "candidate_category" in df.columns:
        candidate = df["candidate_category"].str.strip().str.upper()
        df["approved_label"] = df["approved_label"].where(
            df["approved_label"].ne(""), candidate
        )

    df = df[
        df["approved_label"].isin(VALID_LABELS)
        & df["title"].str.strip().ne("")
    ].copy()

    # 동일 제목이 학습/평가 양쪽에 들어가는 누수 방지.
    conflicts = (
        df.groupby("title")["approved_label"].nunique()
    )
    ambiguous_titles = conflicts[conflicts > 1].index

    df = df[
        ~df["title"].isin(ambiguous_titles)
    ].drop_duplicates(subset=["title"])

    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--use-candidate-labels",
        action="store_true",
        help="검수 전 키워드 후보 라벨로 파이프라인 점검",
    )
    args = parser.parse_args()
    weak = args.use_candidate_labels

    df = load_reviewed_data(weak)

    print("검수된 고유 제목:", len(df))

    counts = df["approved_label"].value_counts()
    print("\n라벨 분포:")
    print(counts.to_string())

    # 너무 적은 클래스는 분할과 평가가 불안정하다.
    eligible = counts[counts >= 5].index
    df = df[df["approved_label"].isin(eligible)].copy()

    if len(df) < 30 or df["approved_label"].nunique() < 2:
        raise RuntimeError(
            "학습 가능한 검수 데이터가 부족합니다. "
            "job_label_review.csv의 approved_label을 채우거나 "
            "--use-candidate-labels로 점검 학습을 하세요. "
            "최소 30개 고유 제목과 2개 이상 직무군, "
            "각 직무군 5개 이상의 검수 라벨이 필요합니다."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        df["title"],
        df["approved_label"],
        test_size=0.25,
        random_state=42,
        stratify=df["approved_label"],
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                analyzer="char",
                ngram_range=(2, 4),
                min_df=1,
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

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    report = classification_report(
        y_test,
        predictions,
        output_dict=True,
        zero_division=0,
    )

    accuracy = accuracy_score(y_test, predictions)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        model,
        MODEL_DIR / (
            "job_classifier_weak.joblib" if weak
            else "job_classifier.joblib"
        ),
    )

    result = {
        "model": "TFIDF_CHAR_NGRAM_LOGISTIC_REGRESSION",
        "label_source": (
            "KEYWORD_CANDIDATE_WEAK" if weak else "HUMAN_REVIEWED"
        ),
        "training_rows": len(X_train),
        "test_rows": len(X_test),
        "accuracy": accuracy,
        "classification_report": report,
        "limitations": [
            "후보 라벨 사용 시 키워드 규칙 재현율일 뿐 실제 성능 아님"
            if weak
            else "검수된 소규모 표본 기준 평가",
            "제목 기반 직무군 분류만 수행",
            "작업 위험 특성은 예측하지 않음",
        ],
    }

    with open(
        MODEL_DIR / "evaluation.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("\nAI-F-001 ML 학습 완료")
    print("--------------------------")
    print("학습:", len(X_train))
    print("평가:", len(X_test))
    print(f"Accuracy: {accuracy:.4f}")
    print(
        "Macro F1:",
        round(report["macro avg"]["f1-score"], 4)
    )
    print("라벨 출처:", result["label_source"])


if __name__ == "__main__":
    main()

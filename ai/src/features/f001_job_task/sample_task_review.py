
"""
AI-F-001 작업 특성 검수 샘플 생성.

입력:
artifacts/f001/task_label_candidates.csv

출력:
artifacts/f001/task_review_sample.csv

실행:
python -m src.features.f001_job_task.sample_task_review
"""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"

INPUT_FILE = DATA_DIR / "task_label_candidates.csv"
OUTPUT_FILE = DATA_DIR / "task_review_sample.csv"

TARGET_LABELS = [
    "CLEANING_TASK",
    "CARE_TASK",
    "DRIVING",
    "FACILITY_MAINTENANCE",
    "NIGHT_SHIFT",
    "OFFICE_TASK",
    "WALKING",
]

SAMPLE_PER_LABEL = 30
UNKNOWN_SAMPLE = 100
RANDOM_STATE = 42


def parse_labels(value):
    """JSON 문자열을 라벨 목록으로 변환."""
    if isinstance(value, list):
        return value

    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else []
    except (TypeError, ValueError):
        return []


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(INPUT_FILE)

    if OUTPUT_FILE.exists():
        raise FileExistsError(
            f"기존 검수 결과 보호: {OUTPUT_FILE}"
        )

    df = pd.read_csv(INPUT_FILE, dtype=str).fillna("")

    required = {"job_id", "title", "candidate_labels"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"필수 컬럼 누락: {sorted(missing)}"
        )

    df["labels"] = df["candidate_labels"].apply(parse_labels)
    df["title"] = df["title"].str.strip()

    df = df[df["title"].ne("")].copy()

    # 동일 제목은 검수 샘플에서 한 번만 등장하도록 구성
    df = df.drop_duplicates(subset=["title"])

    selected = []

    # 라벨별 양성 후보 균형 샘플링
    for label in TARGET_LABELS:
        subset = df[
            df["labels"].apply(lambda x: label in x)
        ]

        if subset.empty:
            print(f"후보 없음: {label}")
            continue

        sample = subset.sample(
            n=min(SAMPLE_PER_LABEL, len(subset)),
            random_state=RANDOM_STATE,
        )

        selected.append(sample)

    # 라벨을 탐지하지 못한 제목도 별도 검수
    unknown = df[
        df["labels"].apply(lambda x: len(x) == 0)
    ]

    if not unknown.empty:
        selected.append(
            unknown.sample(
                n=min(UNKNOWN_SAMPLE, len(unknown)),
                random_state=RANDOM_STATE,
            )
        )

    if not selected:
        raise ValueError("검수할 샘플이 없습니다.")

    review = pd.concat(selected, ignore_index=True)

    # 여러 라벨이 있는 제목은 하나의 행으로 통합
    review = review.drop_duplicates(subset=["title"])

    review = review[
        ["job_id", "title", "candidate_labels"]
    ].copy()

    # 각 작업 특성별로 독립 검수
    # 1 = 있음, 0 = 없음, ? = 판단 불가
    for label in TARGET_LABELS:
        review[f"review_{label}"] = "?"

    review["review_status"] = "PENDING"
    review["review_note"] = ""

    review.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print("\nAI-F-001 검수 샘플 생성 완료")
    print("-" * 45)
    print("전체 검수 샘플:", len(review))
    print("검수 대상 라벨:", len(TARGET_LABELS))
    print("출력:", OUTPUT_FILE)
    print("\n라벨 검수 기준")
    print("1 = 해당 작업 특성이 확인됨")
    print("0 = 해당 작업 특성이 없다고 확인됨")
    print("? = 제목만으로 판단 불가")


if __name__ == "__main__":
    main()


"""
AI-F-001 작업 특성 검수 큐 생성.

입력:
artifacts/f001/task_review_sample.csv

출력:
artifacts/f001/task_review_queue.csv

원본 검수 파일은 수정하지 않는다.
"""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "artifacts" / "f001"

INPUT = DATA_DIR / "task_review_sample.csv"
OUTPUT = DATA_DIR / "task_review_queue.csv"

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
        result = json.loads(value)
        return result if isinstance(result, list) else []
    except (TypeError, ValueError):
        return []


def main():
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)

    if OUTPUT.exists():
        raise FileExistsError(
            f"기존 파일 보호: {OUTPUT}"
        )

    df = pd.read_csv(INPUT, dtype=str).fillna("")

    required = {"job_id", "title", "candidate_labels"}
    required.update(f"review_{label}" for label in LABELS)

    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"필수 컬럼 누락: {sorted(missing)}"
        )

    df["parsed_labels"] = (
        df["candidate_labels"].apply(parse_labels)
    )

    # 어떤 라벨을 검수해야 하는지 표시
    for label in LABELS:
        df[f"candidate_{label}"] = (
            df["parsed_labels"].apply(
                lambda labels: (
                    "POSITIVE_CANDIDATE"
                    if label in labels
                    else "UNKNOWN"
                )
            )
        )

    # 같은 라벨만 연속해서 나오지 않도록
    # 후보 라벨 기준으로 정렬 후 라운드로빈 배치
    groups = {}

    for label in LABELS:
        groups[label] = df[
            df["parsed_labels"].apply(
                lambda values: label in values
            )
        ].copy()

    groups["NO_CANDIDATE"] = df[
        df["parsed_labels"].apply(
            lambda values: len(values) == 0
        )
    ].copy()

    ordered_indices = []
    seen = set()

    max_rows = max(
        (len(group) for group in groups.values()),
        default=0,
    )

    for i in range(max_rows):
        for group in groups.values():
            if i >= len(group):
                continue

            idx = group.index[i]

            if idx not in seen:
                ordered_indices.append(idx)
                seen.add(idx)

    # 복수 라벨 등의 이유로 남은 행도 보존
    ordered_indices.extend(
        idx for idx in df.index if idx not in seen
    )

    result = df.loc[ordered_indices].copy()
    result = result.drop(columns=["parsed_labels"])

    result.to_csv(
        OUTPUT,
        index=False,
        encoding="utf-8-sig",
    )

    print("검수 큐 생성 완료")
    print("원본 행 수:", len(df))
    print("출력 행 수:", len(result))
    print("출력 파일:", OUTPUT)


if __name__ == "__main__":
    main()

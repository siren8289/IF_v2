
"""
AI-F-001 작업 특성 멀티라벨 학습 후보 생성.

원본: staging.public_api_raw (PUB-012)
출력: artifacts/f001/task_label_candidates.csv
      artifacts/f001/task_label_review.csv
      artifacts/f001/task_label_summary.csv

실행:
python -m src.features.f001_job_task.prepare_task_labels
"""

import json
import re
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from src.core.database import get_engine


ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = ROOT / "artifacts" / "f001"

# 작업 특성별 직접적인 텍스트 단서
# 직무군만으로 작업 특성을 확정하지 않는다.
TASK_RULES = {
    "STANDING": [
        r"입식", r"서서\s*근무", r"서서\s*작업",
    ],
    "WALKING": [
        r"순찰", r"도보", r"보행", r"걸어서",
    ],
    "LIFTING": [
        r"중량물", r"상하차", r"짐\s*운반",
        r"물품\s*운반", r"하역",
    ],
    "REPETITIVE": [
        r"반복\s*작업", r"반복\s*동작",
        r"반복\s*포장",
    ],
    "NIGHT_SHIFT": [
        r"야간", r"심야", r"밤\s*근무",
    ],
    "DRIVING": [
        r"운전", r"운송", r"배송", r"배달",
    ],
    "CLEANING_TASK": [
        r"청소", r"미화", r"환경미화",
    ],
    "FACILITY_MAINTENANCE": [
        r"설비\s*관리", r"시설\s*관리",
        r"시설관리", r"전기\s*점검",
    ],
    "CARE_TASK": [
        r"요양보호", r"돌봄", r"간병",
    ],
    "OFFICE_TASK": [
        r"사무보조", r"문서\s*작성",
        r"행정\s*보조", r"자료\s*입력",
    ],
}


def extract_labels(title: str):
    """제목에 직접 등장하는 작업 특성 단서를 추출한다."""
    labels = []
    evidence = {}

    for label, patterns in TASK_RULES.items():
        matches = []

        for pattern in patterns:
            found = re.search(pattern, title, re.IGNORECASE)

            if found:
                matches.append(found.group(0))

        if matches:
            labels.append(label)
            evidence[label] = sorted(set(matches))

    return labels, evidence


def load_jobs():
    """PUB-012 원본 JSON에서 공고 ID와 제목을 조회한다."""
    query = text("""
        SELECT payload
        FROM staging.public_api_raw
        WHERE dataset_code = 'PUB-012'
    """)

    with get_engine().connect() as conn:
        rows = conn.execute(query).fetchall()

    records = []

    for row in rows:
        payload = row[0]

        if isinstance(payload, str):
            payload = json.loads(payload)

        if not isinstance(payload, dict):
            continue

        job_id = str(payload.get("jobId") or "").strip()
        title = str(payload.get("recrtTitle") or "").strip()

        if not job_id or not title:
            continue

        records.append({
            "job_id": job_id,
            "title": title,
        })

    return pd.DataFrame(
        records, columns=["job_id", "title"]
    )


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_jobs()

    if df.empty:
        raise ValueError("PUB-012 직무 데이터가 없습니다.")

    duplicate_count = df["job_id"].duplicated().sum()

    if duplicate_count:
        raise ValueError(
            f"중복 job_id 발견: {duplicate_count}"
        )

    rows = []

    for record in df.itertuples(index=False):
        labels, evidence = extract_labels(record.title)

        rows.append({
            "job_id": record.job_id,
            "title": record.title,
            "candidate_labels": json.dumps(
                labels, ensure_ascii=False
            ),
            "evidence": json.dumps(
                evidence, ensure_ascii=False
            ),
            "label_count": len(labels),
            "label_source": "KEYWORD_CANDIDATE_WEAK",
            "review_status": "PENDING",
        })

    result = pd.DataFrame(rows)

    # 원본 후보 데이터 저장
    result.to_csv(
        OUTPUT_DIR / "task_label_candidates.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # 검수용 CSV는 기존 작업을 덮어쓰지 않는다.
    review_path = OUTPUT_DIR / "task_label_review.csv"

    if not review_path.exists():
        review = result.copy()
        review["approved_labels"] = ""
        review["review_note"] = ""

        review.to_csv(
            review_path,
            index=False,
            encoding="utf-8-sig",
        )

    # 작업 특성별 빈도
    counts = {
        label: 0 for label in TASK_RULES
    }

    for raw in result["candidate_labels"]:
        for label in json.loads(raw):
            counts[label] += 1

    summary = pd.DataFrame([
        {"label": label, "count": count}
        for label, count in counts.items()
    ]).sort_values("count", ascending=False)

    summary.to_csv(
        OUTPUT_DIR / "task_label_summary.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("\nAI-F-001 작업 특성 후보 생성")
    print("-" * 45)
    print("전체 공고:", len(result))
    print("고유 제목:", result["title"].nunique())
    print("라벨 후보 존재:", int(
        (result["label_count"] > 0).sum()
    ))
    print("라벨 후보 없음:", int(
        (result["label_count"] == 0).sum()
    ))
    print("복수 라벨:", int(
        (result["label_count"] > 1).sum()
    ))
    print("\n작업 특성별 분포")
    print(summary.to_string(index=False))
    print("\n저장 경로:", OUTPUT_DIR)


if __name__ == "__main__":
    main()

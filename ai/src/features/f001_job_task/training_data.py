
"""
AI-F-001: PUB-012 제목 기반 직무 분류 후보 생성.

입력:
    staging.public_api_raw (PUB-012)

출력:
    artifacts/f001/job_label_candidates.csv
    artifacts/f001/training_data_report.json

주의:
    자동 분류 결과는 정답 라벨이 아니다.
    DB 원본은 수정하지 않는다.

실행:
    python -m src.features.f001_job_task.training_data
"""

import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from src.core.database import get_engine


ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = ROOT / "artifacts" / "f001"

# 규칙은 구체적인 직무 표현을 우선한다.
# 단독 '기사', '관리원' 등은 직무 구분이 모호하므로 제외.
CATEGORY_RULES = {
    "FACILITY": [
        r"시설관리", r"시설기사", r"설비기사",
        r"설비관리", r"전기기사", r"전기관리",
        r"기계설비", r"관리소장", r"영선",
    ],
    "DRIVING": [
        r"택시기사", r"버스기사", r"운전기사",
        r"배송기사", r"배달기사", r"화물기사",
        r"운전원", r"운전직", r"승무원",
        r"배송", r"배달",
    ],
    "CARE": [
        r"요양보호", r"간병", r"돌봄",
        r"사회복지사", r"생활재활",
        r"생활지원사", r"활동지원사",
    ],
    "CLEANING": [
        r"미화", r"청소", r"환경미화",
        r"환경정비", r"청소원",
    ],
    "SECURITY": [
        r"경비", r"보안", r"방호",
        r"경비원", r"보안요원",
    ],
    "OFFICE": [
        r"사무", r"행정", r"원무",
        r"전산", r"회계", r"총무",
        r"서무", r"문서관리",
    ],
    "MANUFACTURING": [
        r"생산", r"제조", r"조립",
        r"포장", r"검수", r"생산직",
    ],
    "KITCHEN": [
        r"조리", r"주방", r"급식",
        r"조리원", r"주방보조",
    ],
    "SALES": [
        r"판매", r"매장", r"영업",
        r"판매원", r"계산원",
    ],
    "AGRICULTURE": [
        r"농업", r"농장", r"재배",
        r"농작물", r"원예",
    ],
}

COMPILED_RULES = {
    category: [
        re.compile(pattern, re.IGNORECASE)
        for pattern in patterns
    ]
    for category, patterns in CATEGORY_RULES.items()
}


def classify_title(title: str) -> dict:
    """
    제목에서 직무군 후보를 찾는다.

    여러 카테고리가 동시에 발견되면
    MULTI_MATCH로 표시하고 검수를 요청한다.
    """

    title = str(title or "").strip()

    matches = {}

    for category, patterns in COMPILED_RULES.items():
        keywords = []

        for pattern in patterns:
            for match in pattern.finditer(title):
                keywords.append(match.group())

        if keywords:
            matches[category] = sorted(set(keywords))

    if not matches:
        return {
            "category": "UNKNOWN",
            "matched_categories": [],
            "matched_keywords": [],
            "review_status": "UNCLASSIFIED",
        }

    if len(matches) > 1:
        return {
            "category": "MULTI_MATCH",
            "matched_categories": list(matches),
            "matched_keywords": sorted({
                keyword
                for values in matches.values()
                for keyword in values
            }),
            "review_status": "AMBIGUOUS",
        }

    category = next(iter(matches))

    return {
        "category": category,
        "matched_categories": [category],
        "matched_keywords": matches[category],
        "review_status": "PENDING",
    }


def load_postings(engine) -> pd.DataFrame:
    """PUB-012의 구인공고를 조회한다."""

    sql = text("""
        SELECT
            raw_id,
            NULLIF(TRIM(payload ->> 'jobId'), '') AS job_id,
            NULLIF(TRIM(payload ->> 'recrtTitle'), '') AS title,
            NULLIF(TRIM(payload ->> 'jobcls'), '') AS job_code,
            NULLIF(TRIM(payload ->> 'jobclsNm'), '') AS job_class,
            NULLIF(TRIM(payload ->> 'oranNm'), '') AS organization
        FROM staging.public_api_raw
        WHERE dataset_code = 'PUB-012'
        ORDER BY raw_id
    """)

    with engine.connect() as conn:
        return pd.read_sql_query(sql, conn)


def build_candidates(df: pd.DataFrame) -> pd.DataFrame:
    """제목 기반 후보 라벨 데이터셋 생성."""

    rows = []

    for record in df.itertuples(index=False):
        title = record.title or ""
        result = classify_title(title)

        rows.append({
            "source_dataset": "PUB-012",
            "raw_id": record.raw_id,
            "job_id": record.job_id,
            "title": title,
            "organization": record.organization,
            "source_job_code": record.job_code,
            "source_job_class": record.job_class,
            "candidate_category": result["category"],
            "matched_categories": json.dumps(
                result["matched_categories"],
                ensure_ascii=False,
            ),
            "matched_keywords": json.dumps(
                result["matched_keywords"],
                ensure_ascii=False,
            ),
            "label_source": "TITLE_KEYWORD_RULE_V2",
            "review_status": result["review_status"],
            "approved_label": "",
        })

    return pd.DataFrame(rows)


def create_report(df: pd.DataFrame, candidates: pd.DataFrame):
    """분류 결과와 데이터 품질 요약."""

    counts = Counter(
        candidates["candidate_category"]
    )

    total = len(candidates)

    return {
        "source_dataset": "PUB-012",
        "total_rows": total,
        "unique_jobs": int(df["job_id"].nunique()),
        "duplicate_job_ids": int(
            df["job_id"].duplicated().sum()
        ),
        "missing_titles": int(
            df["title"].isna().sum()
        ),
        "category_distribution": dict(counts),
        "unknown_rows": counts.get("UNKNOWN", 0),
        "multi_match_rows": counts.get("MULTI_MATCH", 0),
        "classified_rows": total
            - counts.get("UNKNOWN", 0)
            - counts.get("MULTI_MATCH", 0),
        "approved_labels": 0,
        "label_version": "TITLE_KEYWORD_RULE_V2",
    }


def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    engine = get_engine()

    try:
        df = load_postings(engine)
    finally:
        engine.dispose()

    if df.empty:
        raise RuntimeError(
            "PUB-012 데이터가 없습니다."
        )

    candidates = build_candidates(df)
    report = create_report(df, candidates)

    candidates.to_csv(
        OUTPUT_DIR / "job_label_candidates.csv",
        index=False,
        encoding="utf-8-sig",
    )

    with open(
        OUTPUT_DIR / "training_data_report.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            report,
            file,
            ensure_ascii=False,
            indent=2,
        )

    print("\nAI-F-001 PUB-012 직무 분류 결과")
    print("--------------------------------")
    print("전체:", report["total_rows"])
    print("고유 공고:", report["unique_jobs"])
    print("중복 ID:", report["duplicate_job_ids"])
    print("제목 누락:", report["missing_titles"])
    print("분류 후보:", report["classified_rows"])
    print("UNKNOWN:", report["unknown_rows"])
    print("MULTI_MATCH:", report["multi_match_rows"])

    print("\n카테고리 분포")
    for category, count in sorted(
        report["category_distribution"].items(),
        key=lambda item: -item[1],
    ):
        print(f"{category}: {count}")

    print("\n저장 경로:", OUTPUT_DIR)


if __name__ == "__main__":
    main()

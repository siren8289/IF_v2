
"""
AI-F-001 공공데이터 전처리 실행.

python -m src.features.f001_job_task
"""

import json
from pathlib import Path

from src.core.database import (
    get_engine,
    check_connection,
)

from .data import (
    EXPECTED_COUNTS,
    load_job_context,
    prepare_job_context,
    build_quality_report,
)


ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = ROOT / "artifacts" / "f001"


def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("DB 연결:", check_connection())

    engine = get_engine()

    try:
        raw_df = load_job_context(engine)
    finally:
        engine.dispose()

    clean_df = prepare_job_context(raw_df)

    report = build_quality_report(clean_df)

    clean_df.to_csv(
        OUTPUT_DIR / "job_context_clean.csv",
        index=False,
        encoding="utf-8-sig",
    )

    with open(
        OUTPUT_DIR / "quality_report.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            report,
            f,
            ensure_ascii=False,
            indent=2,
        )

    print("\nAI-F-001 전처리 결과")
    print("--------------------------")
    print("전체 건수:", report["total_rows"])
    print("원천별 건수:", report["counts_by_source"])
    print("중복 원천 키:", report["duplicate_source_keys"])
    print("누락 원천 키:", report["missing_source_keys"])
    print("출력 경로:", OUTPUT_DIR)

    if report["total_rows"] != sum(
        EXPECTED_COUNTS.values()
    ):
        raise RuntimeError(
            "예상 데이터 건수와 실제 건수가 다릅니다."
        )

    if not all(
        report["count_matches_expected"].values()
    ):
        raise RuntimeError(
            "원천별 데이터 건수 검증에 실패했습니다."
        )

    if report["duplicate_source_keys"] > 0:
        raise RuntimeError(
            "중복 원천 키가 발견되었습니다."
        )

    print("기본 건수·키 검증 완료")


if __name__ == "__main__":
    main()

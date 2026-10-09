
"""
AI-F-001 전처리 실행 스크립트.

실행:
python -m scripts.prepare_f001
"""

import json
from pathlib import Path

from src.data.database import (
    get_engine,
    check_connection,
)
from src.data.job_context import (
    load_job_context,
    prepare_job_context,
    build_quality_report,
)


OUTPUT_DIR = Path("artifacts/f001")


def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("DB:", check_connection())

    engine = get_engine()

    try:
        raw_df = load_job_context(engine)
    finally:
        engine.dispose()

    print("원본 레코드:", len(raw_df))

    processed_df = prepare_job_context(
        raw_df
    )

    report = build_quality_report(
        processed_df
    )

    processed_df.to_csv(
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

    print("전처리 레코드:", len(processed_df))
    print("품질 보고서:", report)
    print("저장 완료:", OUTPUT_DIR)


if __name__ == "__main__":
    main()

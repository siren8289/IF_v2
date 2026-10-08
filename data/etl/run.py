import argparse

from data.etl.config import get_source
from data.etl.fetch import fetch_data
from data.etl.transform import parse_data, normalize_rows
from data.etl.load import (
    start_run,
    finish_run,
    load_records,
)


def run_pipeline(source_id: str):
    source = get_source(source_id)

    run_id = start_run(source_id)

    try:
        print(f"[1/3] {source_id} API 수집")
        payload = fetch_data(source)

        print("[2/3] 파싱·전처리·검증")
        parsed = parse_data(payload, source)
        records = normalize_rows(parsed, source)

        print("[3/3] PostgreSQL 적재")
        count = load_records(source_id, records)

        finish_run(run_id, "SUCCESS", count)

        print(f"완료: {source_id}, {count}건")

    except Exception as exc:
        finish_run(
            run_id,
            "FAILED",
            error=type(exc).__name__,
        )
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source",
        required=True,
        help="예: PUB-004",
    )

    args = parser.parse_args()

    run_pipeline(args.source)
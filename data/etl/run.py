# 공공데이터 한 종류를 받아 DB에 넣는 실행 파일.
#
# 사용법: python -m data.etl.run --source PUB-004
# 순서: 수집(fetch) → 파싱·정리(transform) → 저장(load)
# 시작과 끝에 etl_run 테이블에 성공/실패를 남긴다.
#
# config.py 와 fetch.py 는 지금 비어 있다.
# get_source, fetch_data 를 채우기 전에는 이 파일만으로는 실행되지 않는다.
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
    """source_id 하나에 대해 수집부터 적재까지 한 번 돌린다."""
    # sources 설정에서 이 데이터의 주소, 형식, 필수 칸을 찾는다.
    source = get_source(source_id)

    # 실행 기록을 먼저 RUNNING으로 만든다. 중간에 죽어도 "돌다가 멈춤"을 알 수 있다.
    run_id = start_run(source_id)

    try:
        print(f"[1/3] {source_id} API 수집")
        payload = fetch_data(source)

        print("[2/3] 파싱·전처리·검증")
        # 원본 문자열(JSON/XML/CSV)을 행 목록으로 바꾸고, 빈 값·중복을 뺀다.
        parsed = parse_data(payload, source)
        records = normalize_rows(parsed, source)

        print("[3/3] PostgreSQL 적재")
        count = load_records(source_id, records)

        finish_run(run_id, "SUCCESS", count)

        print(f"완료: {source_id}, {count}건")

    except Exception as exc:
        # 실패 원인 클래스 이름만 남기고, 예외는 다시 올려 호출자가 로그로 보게 한다.
        finish_run(
            run_id,
            "FAILED",
            error=type(exc).__name__,
        )
        raise


if __name__ == "__main__":
    # 이 파일을 직접 실행할 때만 명령줄 인자를 읽는다. 다른 곳에서 import 하면 여기로 안 온다.
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source",
        required=True,
        help="예: PUB-004",
    )

    args = parser.parse_args()

    run_pipeline(args.source)

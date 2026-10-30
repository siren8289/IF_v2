# 정리된 행을 PostgreSQL에 넣고, 이번 실행의 성공/실패를 기록한다.
# 접속 정보(호스트, 계정, 비밀번호)는 data.etl.config.get_db_config()가 준다.
import json

import psycopg

from data.etl.config import get_db_config


def connect_db():
    """설정 딕셔너리를 풀어서 PostgreSQL에 연결한다. with 문에서 쓰면 자동으로 닫힌다."""
    return psycopg.connect(**get_db_config())


def start_run(source_id: str) -> int:
    """실행 시작 행을 넣고, 방금 생긴 run_id를 돌려준다."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO external_ref.etl_run
                    (source_id, status)
                VALUES (%s, 'RUNNING')
                RETURNING run_id
                """,
                (source_id,),
            )
            return cur.fetchone()[0]


def finish_run(run_id: int, status: str,
               count: int = 0, error: str | None = None):
    """시작 때 만든 행을 SUCCESS 또는 FAILED로 닫고, 건수와 오류 이름을 적는다."""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE external_ref.etl_run
                SET status = %s,
                    record_count = %s,
                    error_message = %s,
                    finished_at = NOW()
                WHERE run_id = %s
                """,
                (status, count, error, run_id),
            )


def load_records(source_id: str, rows: list[dict]) -> int:
    """행을 public_record에 넣는다. 같은 source_id + record_key가 있으면 내용만 갱신한다.

    payload는 JSON 문자열로 넣어 jsonb 컬럼에 캐스팅한다.
    ensure_ascii=False 라서 한글이 \\uXXXX로 바뀌지 않는다.
    """
    with connect_db() as conn:
        with conn.cursor() as cur:
            for row in rows:
                cur.execute(
                    """
                    INSERT INTO external_ref.public_record
                        (source_id, record_key, payload)
                    VALUES (%s, %s, %s::jsonb)
                    ON CONFLICT (source_id, record_key)
                    DO UPDATE SET
                        payload = EXCLUDED.payload,
                        updated_at = NOW()
                    """,
                    (
                        source_id,
                        row["record_key"],
                        json.dumps(
                            row["payload"],
                            ensure_ascii=False,
                            default=str,
                        ),
                    ),
                )

    return len(rows)

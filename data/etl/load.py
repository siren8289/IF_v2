import json

import psycopg

from data.etl.config import get_db_config


def connect_db():
    return psycopg.connect(**get_db_config())


def start_run(source_id: str) -> int:
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
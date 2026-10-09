
"""
AI 공통 PostgreSQL 연결 모듈.
기존 Spring Boot DB의 ai 스키마를 읽는다.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

AI_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(AI_ROOT / ".env")


def get_engine():
    """환경변수에 지정된 PostgreSQL Engine 생성."""
    url = os.getenv("DATABASE_URL")

    if not url:
        raise RuntimeError(
            "ai/.env에 DATABASE_URL을 설정하세요."
        )

    return create_engine(
        url,
        pool_pre_ping=True,
        connect_args={"connect_timeout": 10},
    )


def check_connection():
    """DB 연결 및 현재 DB 이름 확인."""
    engine = get_engine()

    try:
        with engine.connect() as conn:
            return conn.execute(
                text("SELECT current_database()")
            ).scalar_one()
    finally:
        engine.dispose()

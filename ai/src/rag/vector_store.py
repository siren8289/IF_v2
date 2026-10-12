"""PostgreSQL + pgvector 벡터 검색 및 인메모리 저장소 모듈.

고령자 안전 지침 청크와 임베딩 벡터를 저장하고 유사도 검색을 수행합니다.
PostgreSQL 및 pgvector 환경이 연결되어 있으면 실제 DB를 사용하고,
DB 연결이 없거나 테스트 환경일 때는 자체 인메모리(In-Memory) 저장소를 사용합니다.
"""
import json
import os
from typing import Optional

import numpy as np

from src.rag.embedder import cosine_similarity, embed_text


# PostgreSQL 테이블 및 인덱스 생성 DDL SQL문
PGVECTOR_SCHEMA_SQL = """
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS safety_guideline_vectors (
    id SERIAL PRIMARY KEY,
    doc_name VARCHAR(255) NOT NULL,
    page INT NOT NULL,
    source VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    embedding vector(768) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_safety_vectors_cosine 
ON safety_guideline_vectors USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
"""


class InMemoryVectorStore:
    """DB 없이 메모리 상에서 안전 지침 벡터 검색을 수행하는 간결한 저장소입니다."""

    def __init__(self):
        # [{"chunk_id": ..., "doc_name": ..., "page": ..., "source": ..., "content": ..., "embedding": [...]}]
        self.records: list[dict] = []

    def add_chunks(self, chunks: list[dict]) -> int:
        """청크 목록을 받아서 임베딩을 계산하고 저장합니다."""
        added_count = 0
        for chunk in chunks:
            content = chunk.get("content", "")
            if not content.strip():
                continue

            # 이미 임베딩이 있으면 재사용, 없으면 생성
            embedding = chunk.get("embedding")
            if not embedding:
                embedding = embed_text(content)

            record = {
                "chunk_id": chunk.get("chunk_id", f"c_{len(self.records)+1}"),
                "doc_name": chunk.get("doc_name", "미상 문서"),
                "page": chunk.get("page", 1),
                "source": chunk.get("source", "출처 미상"),
                "content": content,
                "embedding": embedding,
            }
            self.records.append(record)
            added_count += 1
        return added_count

    def search(self, query: str, top_k: int = 5, min_similarity: float = 0.0) -> list[dict]:
        """질의와 유사한 지침 청크를 코사인 유사도 순서로 검색합니다."""
        if not self.records or not query.strip():
            return []

        query_vector = embed_text(query)
        scored_results = []

        for record in self.records:
            sim = cosine_similarity(query_vector, record["embedding"])
            if sim >= min_similarity:
                item = {
                    "chunk_id": record["chunk_id"],
                    "doc_name": record["doc_name"],
                    "page": record["page"],
                    "source": record["source"],
                    "content": record["content"],
                    "similarity": round(float(sim), 4),
                }
                scored_results.append(item)

        # 유사도 높은 순으로 정렬 후 상위 top_k개 반환
        scored_results.sort(key=lambda x: x["similarity"], reverse=True)
        return scored_results[:top_k]

    def clear(self):
        """저장된 모든 데이터를 비웁니다."""
        self.records.clear()


class PgVectorStore:
    """PostgreSQL + pgvector 확장을 사용하는 영구 벡터 저장소입니다."""

    def __init__(
        self,
        dbname: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[str] = None,
    ):
        self.dbname = dbname or os.getenv("POSTGRES_DB", "if_spring")
        self.user = user or os.getenv("POSTGRES_USER", "if_user")
        self.password = password or os.getenv("IF_DB_PASSWORD", "")
        self.host = host or os.getenv("POSTGRES_HOST", "localhost")
        self.port = port or os.getenv("POSTGRES_PORT", "5432")

    def _get_connection(self):
        """PostgreSQL 연결 객체를 반환합니다 (psycopg 라이브러리 사용)."""
        import psycopg

        return psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def init_db(self):
        """pgvector 확장 및 테이블 스키마를 초기화합니다."""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(PGVECTOR_SCHEMA_SQL)
            conn.commit()

    def add_chunks(self, chunks: list[dict]) -> int:
        """청크와 임베딩을 PostgreSQL에 저장합니다."""
        records = []
        for chunk in chunks:
            content = chunk.get("content", "")
            if not content.strip():
                continue
            embedding = chunk.get("embedding") or embed_text(content)
            # pgvector 문자열 형식: "[0.12, 0.34, ...]"
            vector_str = f"[{','.join(str(x) for x in embedding)}]"
            records.append((
                chunk.get("doc_name", "미상"),
                chunk.get("page", 1),
                chunk.get("source", "출처 미상"),
                content,
                vector_str,
            ))

        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO safety_guideline_vectors (doc_name, page, source, content, embedding)
                    VALUES (%s, %s, %s, %s, %s::vector);
                    """,
                    records,
                )
            conn.commit()
        return len(records)

    def search(self, query: str, top_k: int = 5, min_similarity: float = 0.0) -> list[dict]:
        """pgvector의 코사인 거리 연산자(<=>)를 사용하여 가장 유사한 지침을 검색합니다."""
        query_vector = embed_text(query)
        vector_str = f"[{','.join(str(x) for x in query_vector)}]"

        sql = """
            SELECT id, doc_name, page, source, content,
                   1 - (embedding <=> %s::vector) AS similarity
            FROM safety_guideline_vectors
            WHERE 1 - (embedding <=> %s::vector) >= %s
            ORDER BY similarity DESC
            LIMIT %s;
        """

        results = []
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vector_str, vector_str, min_similarity, top_k))
                rows = cur.fetchall()
                for row in rows:
                    results.append({
                        "id": row[0],
                        "doc_name": row[1],
                        "page": row[2],
                        "source": row[3],
                        "content": row[4],
                        "similarity": round(float(row[5]), 4),
                    })
        return results


def get_vector_store(force_memory: bool = False):
    """사용 가능한 벡터 저장소를 돌려줍니다.
    
    기본적으로 PostgreSQL 접속을 시도하고, 접속 불가 시 인메모리 저장소로 자동 전환합니다.
    """
    if force_memory:
        return InMemoryVectorStore()

    # DB 환경변수 또는 접속 가능 여부 점검
    try:
        store = PgVectorStore()
        # 간단한 연결 테스트
        conn = store._get_connection()
        conn.close()
        return store
    except Exception:
        # DB 연결이 안 되면 안전하게 InMemory 저장소 사용
        return InMemoryVectorStore()

"""고령자 직무 안전 지침 검색 및 근거 생성 RAG 패키지.

주요 기능:
- extract_text_from_pdf: PDF 파일에서 페이지별 텍스트 추출
- split_text_into_chunks, chunk_documents: 텍스트 및 문서 청킹
- embed_text, embed_texts: 텍스트 벡터 임베딩 변환
- InMemoryVectorStore, PgVectorStore, get_vector_store: 벡터 저장 및 검색
- rerank_chunks: 키워드 및 안전 가중치 기반 재순위화
- generate_rag_explanation: 근거 기반 설명, 인용 및 답변 보류
- build_safety_rag_graph: LangGraph 상태 기반 흐름 제어
- run_safety_rag: RAG 파이프라인 통합 실행
"""
from src.rag.chunker import chunk_documents, split_text_into_chunks
from src.rag.embedder import cosine_similarity, embed_text, embed_texts
from src.rag.evidence_explainer import (
    format_citations,
    generate_rag_explanation,
)
from src.rag.graph import build_safety_rag_graph
from src.rag.harness import (
    ValidationError,
    execute_with_harness,
    retry_with_backoff,
    validate_rag_input,
)
from src.rag.pdf_reader import (
    extract_text_from_pdf,
    get_default_safety_guidelines,
)
from src.rag.pipeline import run_safety_rag
from src.rag.reranker import calculate_keyword_score, rerank_chunks
from src.rag.vector_store import (
    InMemoryVectorStore,
    PgVectorStore,
    get_vector_store,
)

__all__ = [
    "extract_text_from_pdf",
    "get_default_safety_guidelines",
    "split_text_into_chunks",
    "chunk_documents",
    "embed_text",
    "embed_texts",
    "cosine_similarity",
    "InMemoryVectorStore",
    "PgVectorStore",
    "get_vector_store",
    "calculate_keyword_score",
    "rerank_chunks",
    "generate_rag_explanation",
    "format_citations",
    "build_safety_rag_graph",
    "validate_rag_input",
    "retry_with_backoff",
    "execute_with_harness",
    "ValidationError",
    "run_safety_rag",
]

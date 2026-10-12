"""통합 고령자 직무 안전 RAG 파이프라인.

입력 검증 -> LangGraph 실행 흐름 -> 하네스 오류 격리 -> 근거 기반 설명 및 인용 생성을
단 하나의 함수로 간결하게 실행할 수 있는 메인 진입점 모듈입니다.
"""
from typing import Optional

from src.rag.chunker import chunk_documents
from src.rag.graph import build_safety_rag_graph
from src.rag.harness import (
    ValidationError,
    execute_with_harness,
    logger,
    validate_rag_input,
)
from src.rag.pdf_reader import get_default_safety_guidelines
from src.rag.vector_store import InMemoryVectorStore, get_vector_store

# RAG 파이프라인 싱글톤 저장소 (기본 가이드라인 미리 적재)
_default_store: Optional[InMemoryVectorStore] = None


def get_initialized_vector_store() -> InMemoryVectorStore:
    """기본 안전 지침 가이드라인이 미리 적재된 벡터 저장소를 반환합니다."""
    global _default_store
    if _default_store is None:
        _default_store = InMemoryVectorStore()
        guidelines = get_default_safety_guidelines()
        chunks = chunk_documents(guidelines, chunk_size=300, chunk_overlap=50)
        _default_store.add_chunks(chunks)
        logger.info(f"기본 안전 지침 {len(chunks)}개 청크가 벡터 저장소에 적재되었습니다.")
    return _default_store


def run_safety_rag(
    title: str,
    risk_info: dict,
    vector_store=None,
) -> dict:
    """고령자 직무에 대한 RAG 기반 안전 지침 검색 및 위험도 판단 근거 생성을 실행합니다.
    
    매개변수:
        title: 직무 제목 (예: "아파트 경비원", "건물 청소원")
        risk_info: risk_score.py에서 계산된 점수 및 위험 요소 정보
        vector_store: 사용할 벡터 저장소 (None이면 기본 내장 저장소 사용)
        
    반환값:
        {
            "explanation": "근거 기반 설명 문장",
            "explanation_source": "gemini" | "fallback" | "abstained",
            "is_abstained": False,
            "citations": [{"doc_name": "...", "page": 1, ...}],
            "status": "COMPLETED" | "ABSTAINED" | "ERROR",
            "model_version": "RAG_V1"
        }
    """
    # 1. 하네스 입력 검증
    clean_title, validated_risk = validate_rag_input(title, risk_info)

    # 2. 벡터 저장소 준비
    active_store = vector_store or get_initialized_vector_store()

    # 3. LangGraph 워크플로우 구성 및 초기 상태 준비
    rag_graph = build_safety_rag_graph()
    initial_state = {
        "query": clean_title,
        "risk_info": validated_risk,
        "vector_store": active_store,
        "retrieve_top_k": 5,
        "rerank_top_k": 3,
    }

    # 4. 하네스 오류 격리 실행
    def run_workflow():
        return rag_graph.invoke(initial_state)

    def error_fallback(error: Exception):
        logger.error(f"RAG 파이프라인 실행 실패: {error}")
        return {
            "explanation": "안전 지침 검색 중 일시적 오류가 발생하여 기본 위험도 분석 결과를 안내합니다.",
            "source": "fallback",
            "is_abstained": False,
            "citations": [],
            "status": "ERROR",
        }

    final_state = execute_with_harness(
        run_workflow,
        error_fallback,
        step_name=f"RAG Pipeline ({clean_title})",
    )

    return {
        "explanation": final_state.get("explanation", ""),
        "explanation_source": final_state.get("source", "fallback"),
        "is_abstained": final_state.get("is_abstained", False),
        "citations": final_state.get("citations", []),
        "status": final_state.get("status", "COMPLETED"),
        "model_version": "RAG_V1",
    }

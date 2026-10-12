"""고령자 직무 안전 RAG 기능별 독립 테스트 모듈.

다음 기능들을 철저히 검증합니다:
1. PDF 문서 읽기 & 기본 지침 로더
2. Chunking (텍스트 분할 및 메타데이터 보존)
3. Embedding (벡터 생성, 일관성, 코사인 유사도)
4. PostgreSQL + pgvector 및 InMemoryVectorStore 검색
5. Reranking (키워드 및 고령자 위험 가중치 반영)
6. 근거 부족 시 답변 보류 (Abstain) 정책
7. 근거 기반 설명 생성 및 문서명·페이지·출처 인용
8. LangGraph 실행 흐름 (StateGraph 상태 전이 및 조건부 분기)
9. Harness (입력 검증, 재시도, 로깅, 오류 격리)
10. 통합 파이프라인 (End-to-End)
"""
import pytest

from src.rag import (
    InMemoryVectorStore,
    PgVectorStore,
    ValidationError,
    build_safety_rag_graph,
    calculate_keyword_score,
    chunk_documents,
    cosine_similarity,
    embed_text,
    embed_texts,
    execute_with_harness,
    extract_text_from_pdf,
    format_citations,
    generate_rag_explanation,
    get_default_safety_guidelines,
    rerank_chunks,
    retry_with_backoff,
    run_safety_rag,
    split_text_into_chunks,
    validate_rag_input,
)
from src.rag.vector_store import PGVECTOR_SCHEMA_SQL


# 1. PDF 문서 읽기 및 기본 지침 로더 테스트
def test_pdf_reader_default_guidelines():
    guidelines = get_default_safety_guidelines()
    assert len(guidelines) >= 5
    for item in guidelines:
        assert "doc_name" in item
        assert "page" in item
        assert "source" in item
        assert "content" in item
        assert len(item["content"]) > 10


def test_pdf_reader_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf("non_existing_file.pdf")


# 2. Chunking 테스트
def test_chunking_splits_and_overlaps():
    sample_text = "안녕하세요. " * 50  # 약 350자
    chunks = split_text_into_chunks(sample_text, chunk_size=100, chunk_overlap=20)
    assert len(chunks) > 1
    for chunk in chunks:
        assert len(chunk) <= 100


def test_chunk_documents_preserves_metadata():
    docs = [
        {"doc_name": "안전가이드.pdf", "page": 3, "source": "공단", "content": "A" * 300}
    ]
    chunks = chunk_documents(docs, chunk_size=100, chunk_overlap=20)
    assert len(chunks) >= 3
    for chunk in chunks:
        assert chunk["doc_name"] == "안전가이드.pdf"
        assert chunk["page"] == 3
        assert chunk["source"] == "공단"
        assert "chunk_id" in chunk


# 3. Embedding 테스트
def test_embedding_dimension_and_consistency():
    text = "야간 순찰 시 랜턴을 휴대하고 미끄럼 방지 신발을 착용한다."
    vector1 = embed_text(text)
    vector2 = embed_text(text)

    # 768차원 확인
    assert len(vector1) == 768
    # 동일한 입력은 동일한 임베딩 생성 (결정론적 일관성)
    assert vector1 == vector2

    # 코사인 유사도 자기 자신은 1.0에 근접
    sim = cosine_similarity(vector1, vector2)
    assert pytest.approx(sim, abs=1e-4) == 1.0


def test_cosine_similarity_difference():
    v1 = embed_text("어두운 계단 순찰 낙상 위험")
    v2 = embed_text("어두운 계단 순찰 낙상 위험")
    v3 = embed_text("완전히 무관한 주식 시장 환율 분석")

    sim_same = cosine_similarity(v1, v2)
    sim_diff = cosine_similarity(v1, v3)
    assert sim_same > sim_diff


# 4. PostgreSQL + pgvector 및 InMemoryVectorStore 테스트
def test_vector_store_add_and_search():
    store = InMemoryVectorStore()
    docs = [
        {"chunk_id": "c1", "doc_name": "지침.pdf", "page": 1, "source": "공단", "content": "야간 경비원 순찰 중 낙상 위험"},
        {"chunk_id": "c2", "doc_name": "지침.pdf", "page": 2, "source": "공단", "content": "건물 화장실 청소 물기 미끄러짐 주의"},
    ]
    added = store.add_chunks(docs)
    assert added == 2

    # 경비 관련 검색 시 c1이 상위 결과로 나와야 함
    results = store.search("야간 경비 순찰", top_k=1)
    assert len(results) == 1
    assert results[0]["chunk_id"] == "c1"
    assert results[0]["similarity"] > 0


def test_pgvector_sql_schema():
    assert "CREATE EXTENSION IF NOT EXISTS vector;" in PGVECTOR_SCHEMA_SQL
    assert "vector(768)" in PGVECTOR_SCHEMA_SQL
    assert "ivfflat" in PGVECTOR_SCHEMA_SQL


# 5. Reranking 테스트
def test_reranker_promotes_relevant_and_high_risk_chunks():
    chunks = [
        {"content": "일반 사무 작업용 컴퓨터 배치", "similarity": 0.4},
        {"content": "야간 아파트 경비원 어두운 계단 순찰 중 미끄러짐 낙상 위험", "similarity": 0.38},
    ]
    query = "야간 경비원 낙상"
    reranked = rerank_chunks(query, chunks, top_k=2)

    # 2번째 청크가 키워드 및 고령자 위험 가중치로 인해 1위로 재순위화되어야 함
    assert "낙상" in reranked[0]["content"]
    assert reranked[0]["rerank_score"] > reranked[1]["rerank_score"]


# 6. 근거 부족 시 답변 보류 (Abstain) 정책 테스트
def test_abstain_when_chunks_empty():
    result = generate_rag_explanation("정체불명의 직무", {"risk_score": 50}, [])
    assert result["is_abstained"] is True
    assert result["source"] == "abstained"
    assert "답변을 보류합니다" in result["explanation"]


def test_abstain_when_similarity_is_too_low():
    low_chunks = [
        {"content": "무관한 이야기", "similarity": 0.05, "rerank_score": 0.05, "doc_name": "a.pdf", "page": 1, "source": "b"}
    ]
    result = generate_rag_explanation("외계 우주선 조종사", {"risk_score": 90}, low_chunks)
    assert result["is_abstained"] is True
    assert result["source"] == "abstained"
    assert "근거가 부족하므로 답변을 보류합니다" in result["explanation"]


# 7. 근거 기반 설명 및 인용 테스트
def test_evidence_explanation_and_citations():
    good_chunks = [
        {
            "content": "야간 순찰 시 반드시 랜턴을 휴대하고 안전 손잡이를 잡아야 합니다.",
            "similarity": 0.85,
            "rerank_score": 0.88,
            "doc_name": "경비원안전가이드.pdf",
            "page": 2,
            "source": "안전보건공단",
        }
    ]
    risk_info = {"risk_score": 65, "risk_grade": "HIGH"}
    result = generate_rag_explanation("야간 아파트 경비원", risk_info, good_chunks)

    assert result["is_abstained"] is False
    assert len(result["citations"]) == 1
    citation = result["citations"][0]
    assert citation["doc_name"] == "경비원안전가이드.pdf"
    assert citation["page"] == 2
    assert citation["source"] == "안전보건공단"
    assert "설명" in result or len(result["explanation"]) > 20


# 8. LangGraph 실행 흐름 테스트
def test_langgraph_workflow_generate_path():
    graph = build_safety_rag_graph()
    store = InMemoryVectorStore()
    store.add_chunks([
        {"content": "고령 청소원은 바닥 물기 미끄러짐 사고를 주의해야 합니다.", "doc_name": "청소.pdf", "page": 1, "source": "공단"}
    ])

    state = {
        "query": "바닥 청소원",
        "risk_info": {"risk_score": 45, "risk_grade": "MID"},
        "vector_store": store,
    }
    final_state = graph.invoke(state)

    assert final_state["status"] == "COMPLETED"
    assert final_state["is_abstained"] is False
    assert "explanation" in final_state
    assert len(final_state["citations"]) > 0


def test_langgraph_workflow_abstain_path():
    graph = build_safety_rag_graph()
    empty_store = InMemoryVectorStore()

    state = {
        "query": "관련없는 직무",
        "risk_info": {"risk_score": 20, "risk_grade": "LOW"},
        "vector_store": empty_store,
    }
    final_state = graph.invoke(state)

    assert final_state["status"] == "ABSTAINED"
    assert final_state["is_abstained"] is True


# 9. Harness 테스트 (입력 검증, 재시도, 오류 처리)
def test_harness_validation_rejects_empty_title():
    with pytest.raises(ValidationError):
        validate_rag_input("", {"risk_score": 50})


def test_harness_validation_rejects_invalid_score():
    with pytest.raises(ValidationError):
        validate_rag_input("경비원", {"risk_score": 150})


def test_harness_retry_success_after_failure():
    attempts = 0

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def flaky_task():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise ConnectionError("일시적 네트워크 불안정")
        return "SUCCESS"

    result = flaky_task()
    assert result == "SUCCESS"
    assert attempts == 2


def test_harness_error_handling_fallback():
    def failing_action():
        raise RuntimeError("치명적 시스템 오류 발생")

    def fallback(error):
        return {"status": "FALLBACK_CALLED", "error": str(error)}

    res = execute_with_harness(failing_action, fallback, step_name="테스트단계")
    assert res["status"] == "FALLBACK_CALLED"


# 10. 통합 End-to-End 파이프라인 테스트
def test_full_pipeline_end_to_end():
    risk_info = {
        "risk_score": 72,
        "risk_grade": "HIGH",
        "factors": [{"name": "야간 근무", "points": 8}],
    }
    response = run_safety_rag("야간 아파트 경비원", risk_info)

    assert response["model_version"] == "RAG_V1"
    assert response["status"] in ("COMPLETED", "ABSTAINED")
    assert response["explanation"]
    assert isinstance(response["citations"], list)
    assert isinstance(response["is_abstained"], bool)

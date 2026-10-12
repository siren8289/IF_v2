"""RAG 전용 독립 FastAPI 라우터 및 API 모듈.

기존 main.py나 API를 변경하지 않고 독립적으로 동작하는 RAG REST API입니다.
독립 FastAPI 앱으로 단독 실행하거나, 기존 FastAPI 앱에 include_router로 연동할 수 있습니다.
"""
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.rag.harness import ValidationError
from src.rag.pipeline import run_safety_rag
from src.rag.vector_store import get_vector_store

# RAG 독립 라우터
rag_router = APIRouter(prefix="/api/v1/rag", tags=["RAG"])


class RagExplainRequest(BaseModel):
    """RAG 안전 지침 설명 요청 스키마"""
    title: str = Field(..., min_length=1, max_length=300, examples=["야간 아파트 경비원"])
    risk_score: int = Field(default=50, ge=0, le=100, description="0~100점 참고 지수")
    risk_grade: str = Field(default="MID", description="LOW, MID, HIGH")


class RagSearchRequest(BaseModel):
    """RAG 안전 지침 단순 검색 요청 스키마"""
    query: str = Field(..., min_length=1, max_length=300, examples=["바닥 미끄러짐 청소"])
    top_k: int = Field(default=3, ge=1, le=10)


@rag_router.get("/health")
def rag_health():
    """RAG 서비스 상태 확인 API"""
    return {"status": "ok", "service": "rag_safety_guidelines"}


@rag_router.post("/search")
def search_guidelines_api(request: RagSearchRequest):
    """안전 지침 벡터 검색 API"""
    from src.rag.pipeline import get_initialized_vector_store
    from src.rag.reranker import rerank_chunks

    store = get_initialized_vector_store()
    raw_results = store.search(request.query, top_k=request.top_k * 2)
    reranked = rerank_chunks(request.query, raw_results, top_k=request.top_k)
    return {"query": request.query, "count": len(reranked), "results": reranked}


@rag_router.post("/explain")
def explain_with_rag_api(request: RagExplainRequest):
    """RAG 기반 고령자 직무 안전 지침 근거 생성 및 설명 API"""
    title = request.title.strip()
    if not title:
        raise HTTPException(status_code=422, detail="직무 제목을 입력해 주세요.")

    risk_info = {
        "risk_score": request.risk_score,
        "risk_grade": request.risk_grade,
    }

    try:
        result = run_safety_rag(title=title, risk_info=risk_info)
        return result
    except ValidationError as error:
        raise HTTPException(status_code=422, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"RAG 처리 중 오류: {str(error)}")


# 독립 실행을 위한 전용 FastAPI 앱
rag_app = FastAPI(title="IF RAG Safety Service", version="1.0.0")
rag_app.include_router(rag_router)

"""RAG 전용 독립 FastAPI 라우터 및 API 모듈.

main.py의 점수 API와는 별도 주소다. 점수 계산은 하지 않고,
이미 나온 점수와 직무 제목으로 안전 지침을 찾아 설명을 만든다.

  GET  /api/v1/rag/health   살아 있는지
  POST /api/v1/rag/search   지침 검색만
  POST /api/v1/rag/explain  검색 + 설명 + 인용

단독으로 켜거나, 기존 FastAPI 앱에 include_router로 붙일 수 있다.
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
    # 재순위에서 떨어질 것을 감안해, 요청한 개수의 두 배를 먼저 찾는다.
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

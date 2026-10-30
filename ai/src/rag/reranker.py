"""검색 결과 재순위화(Reranking) 모듈.

1차로 벡터 검색이 "비슷한 문장"을 골라 오면, 그중에서
질문 단어가 실제로 들어 있는지, 낙상·야간 같은 위험 단어가 있는지를
다시 점수로 매긴다. 숫자만 비슷한 엉뚱한 문단이 1등으로 올라오는 것을 줄인다.
"""
import re

# 고령 근로자에게 특히 위험한 주요 안전 키워드 목록
HIGH_RISK_KEYWORDS = [
    "넘어짐", "낙상", "미끄러짐", "떨어짐", "추락",
    "야간", "심혈관", "혈압", "수면", "과로",
    "허리", "디스크", "관절염", "무리한", "중량물", "무거운",
    "운전", "반응속도", "시력", "졸음",
    "폭염", "한파", "탈진", "휴식",
]


def calculate_keyword_score(query: str, content: str) -> float:
    """질의 및 고령자 안전 키워드가 본문에 얼마나 포함되어 있는지 0.0 ~ 1.0 점수로 계산합니다."""
    query_words = set(re.findall(r"\w+", query.lower()))
    content_lower = content.lower()

    if not query_words:
        return 0.0

    # 1. 질문 속 단어가 본문에 몇 개나 들어 있는지. 전부 있으면 1.0이다.
    matched_query = sum(1 for word in query_words if word in content_lower)
    query_ratio = matched_query / len(query_words) if query_words else 0.0

    # 2. 위험 단어 하나당 0.2점. 5개 이상이면 1.0에서 멈춘다.
    matched_risk = sum(1 for kw in HIGH_RISK_KEYWORDS if kw in content_lower)
    risk_boost = min(1.0, matched_risk * 0.2)

    # 3. 종합 점수 (질의 일치 60% + 고령자 위험 키워드 40%)
    return (0.6 * query_ratio) + (0.4 * risk_boost)


def rerank_chunks(query: str, chunks: list[dict], top_k: int = 3) -> list[dict]:
    """1차 검색된 청크들을 키워드 일치도와 벡터 유사도를 결합하여 재정렬합니다.
    
    매개변수:
        query: 검색 질의 (예: "야간 아파트 경비원", "노인 건물 청소")
        chunks: 1차 검색된 청크 목록
        top_k: 최종 반환할 상위 청크 수 (기본 3개)
        
    반환값:
        재순위화된 상위 청크 목록 (rerank_score 필드 추가)
    """
    if not chunks:
        return []

    reranked = []
    for chunk in chunks:
        vector_sim = chunk.get("similarity", 0.0)
        kw_score = calculate_keyword_score(query, chunk.get("content", ""))

        # 최종 점수 = 벡터 유사도 50% + 키워드 연관도 50%
        final_score = (0.5 * vector_sim) + (0.5 * kw_score)

        item = dict(chunk)
        item["rerank_score"] = round(final_score, 4)
        item["keyword_score"] = round(kw_score, 4)
        reranked.append(item)

    # 점수 높은 순으로 정렬
    reranked.sort(key=lambda x: x["rerank_score"], reverse=True)
    return reranked[:top_k]

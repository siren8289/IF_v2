"""LangGraph 기반 RAG 실행 흐름(Workflow Graph) 모듈.

RAG 파이프라인을 상태 그래프(StateGraph) 방식으로 제어합니다.
흐름: [검색] -> [재순위] -> [근거 평가] -> 조건부 분기:
       - 근거 충분 -> [답변 및 인용 생성] -> 종료
       - 근거 부족 -> [답변 보류] -> 종료

외부 langgraph 패키지 설치 여부와 상관없이 완전히 동일한 방식으로 동작하는
가볍고 직관적인 순수 파이썬 StateGraph 엔진을 내장하고 있습니다.
"""
from typing import Any, Callable

from src.rag.evidence_explainer import (
    MIN_EVIDENCE_THRESHOLD,
    generate_rag_explanation,
)
from src.rag.reranker import rerank_chunks


class SimpleStateGraph:
    """초급자도 이해하기 쉬운 직관적인 경량 StateGraph 클래스.
    
    LangGraph와 동일하게 노드(Node), 엣지(Edge), 조건부 엣지(Conditional Edge)를 등록하고
    상태(State)를 전달하며 단계별로 실행합니다.
    """

    def __init__(self):
        self.nodes: dict[str, Callable[[dict], dict]] = {}
        self.edges: dict[str, str] = {}
        self.conditional_edges: dict[str, tuple[Callable[[dict], str], dict[str, str]]] = {}
        self.entry_point: str = ""

    def add_node(self, name: str, func: Callable[[dict], dict]):
        """그래프에 실행할 함수(노드)를 등록합니다."""
        self.nodes[name] = func

    def set_entry_point(self, name: str):
        """가장 먼저 실행할 첫 번째 노드를 지정합니다."""
        self.entry_point = name

    def add_edge(self, from_node: str, to_node: str):
        """한 노드가 끝나면 다음 노드로 넘어가는 일반 연결선을 만듭니다."""
        self.edges[from_node] = to_node

    def add_conditional_edges(
        self,
        source: str,
        condition_func: Callable[[dict], str],
        route_map: dict[str, str],
    ):
        """조건 함수 결과에 따라 다음으로 이동할 노드를 결정하는 분기선을 만듭니다."""
        self.conditional_edges[source] = (condition_func, route_map)

    def compile(self):
        """그래프를 실행 가능한 상태로 확정(컴파일)합니다."""
        return self

    def invoke(self, initial_state: dict) -> dict:
        """초기 상태를 넣고 그래프를 끝까지 실행합니다."""
        current_node = self.entry_point
        state = dict(initial_state)

        # 무한 루프 방지를 위한 최대 실행 단계 수
        max_steps = 20
        steps = 0

        while current_node and steps < max_steps:
            steps += 1
            if current_node not in self.nodes:
                break

            # 현재 노드 함수 실행
            node_func = self.nodes[current_node]
            updates = node_func(state)
            if updates and isinstance(updates, dict):
                state.update(updates)

            # 다음 노드 결정
            if current_node in self.conditional_edges:
                cond_func, route_map = self.conditional_edges[current_node]
                decision = cond_func(state)
                current_node = route_map.get(decision, "")
            elif current_node in self.edges:
                current_node = self.edges[current_node]
            else:
                # 다음 노드가 없으면 종료
                break

        return state


# ==========================================
# RAG 워크플로우 각 단계 노드 함수들
# ==========================================

def retrieve_node(state: dict) -> dict:
    """1단계: 안전 지침 벡터 검색 노드"""
    vector_store = state.get("vector_store")
    query = state.get("query", "")
    top_k = state.get("retrieve_top_k", 5)

    if vector_store:
        retrieved = vector_store.search(query, top_k=top_k)
    else:
        retrieved = []

    return {"retrieved_chunks": retrieved}


def rerank_node(state: dict) -> dict:
    """2단계: 검색 결과 재순위화 노드"""
    query = state.get("query", "")
    chunks = state.get("retrieved_chunks", [])
    top_k = state.get("rerank_top_k", 3)

    reranked = rerank_chunks(query, chunks, top_k=top_k)
    return {"reranked_chunks": reranked}


def evaluate_evidence_node(state: dict) -> dict:
    """3단계: 근거 충분성 평가 노드"""
    chunks = state.get("reranked_chunks", [])
    if not chunks:
        return {"has_enough_evidence": False}

    best_score = max(c.get("rerank_score", 0.0) for c in chunks)
    has_enough = best_score >= MIN_EVIDENCE_THRESHOLD
    return {"has_enough_evidence": has_enough}


def should_abstain_decision(state: dict) -> str:
    """조건부 분기 판단 함수: 근거가 충분하면 generate, 부족하면 abstain 반환"""
    if state.get("has_enough_evidence", False):
        return "generate"
    return "abstain"


def generate_node(state: dict) -> dict:
    """4단계 (성공 경로): 충분한 근거를 바탕으로 설명과 인용 생성 노드"""
    title = state.get("query", "")
    risk_info = state.get("risk_info", {})
    chunks = state.get("reranked_chunks", [])

    result = generate_rag_explanation(title, risk_info, chunks)
    return {
        "explanation": result["explanation"],
        "is_abstained": result["is_abstained"],
        "citations": result["citations"],
        "source": result["source"],
        "status": "COMPLETED",
    }


def abstain_node(state: dict) -> dict:
    """4단계 (보류 경로): 근거 부족으로 답변 보류 처리 노드"""
    chunks = state.get("reranked_chunks", [])
    result = generate_rag_explanation(state.get("query", ""), state.get("risk_info", {}), chunks)
    return {
        "explanation": result["explanation"],
        "is_abstained": True,
        "citations": result["citations"],
        "source": "abstained",
        "status": "ABSTAINED",
    }


def build_safety_rag_graph():
    """고령자 직무 안전 RAG StateGraph를 생성하고 연결하여 돌려줍니다."""
    graph = SimpleStateGraph()

    # 노드 등록
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("rerank", rerank_node)
    graph.add_node("evaluate", evaluate_evidence_node)
    graph.add_node("generate", generate_node)
    graph.add_node("abstain", abstain_node)

    # 시작점 설정
    graph.set_entry_point("retrieve")

    # 고정 연결선
    graph.add_edge("retrieve", "rerank")
    graph.add_edge("rerank", "evaluate")

    # 조건부 분기: 근거 충분 여부에 따라 generate 또는 abstain으로 이동
    graph.add_conditional_edges(
        source="evaluate",
        condition_func=should_abstain_decision,
        route_map={
            "generate": "generate",
            "abstain": "abstain",
        },
    )

    return graph.compile()

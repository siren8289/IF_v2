"""근거 기반 설명 생성, 출처 인용 및 답변 보류 모듈.

검색된 안전 지침을 바탕으로 고령자 직무 위험도 판단 근거를 생성합니다.
근거가 부족하면 환각을 방지하기 위해 답변을 보류(Abstain)하고,
근거가 충분하면 문서명, 페이지 번호, 출처를 명확히 인용합니다.
"""
import os

# 근거가 충분한지 판단하는 최소 기준 점수 (0.0 ~ 1.0)
MIN_EVIDENCE_THRESHOLD = 0.25

GRADE_NAMES = {"LOW": "낮음", "MID": "보통", "HIGH": "높음"}


def format_citations(chunks: list[dict]) -> list[dict]:
    """검색된 청크 목록에서 인용 정보(문서명, 페이지, 출처, 발췌문)를 추출합니다."""
    citations = []
    for chunk in chunks:
        content = chunk.get("content", "").strip()
        # 발췌문은 앞부분 120자만 간략히 요약
        snippet = content[:120] + "..." if len(content) > 120 else content
        citations.append({
            "doc_name": chunk.get("doc_name", "미상 문서"),
            "page": chunk.get("page", 1),
            "source": chunk.get("source", "출처 미상"),
            "snippet": snippet,
        })
    return citations


def build_fallback_explanation(title: str, risk_info: dict, chunks: list[dict]) -> str:
    """Gemini API 키가 없거나 호출 실패 시 사용하는 기본 근거 기반 설명입니다."""
    grade = GRADE_NAMES.get(risk_info.get("risk_grade", "LOW"), "보통")
    score = risk_info.get("risk_score", 0)

    lines = [
        f"'{title}' 직무의 참고 지수는 {score}점({grade})입니다.",
    ]

    if chunks:
        first = chunks[0]
        lines.append(
            f"안전 지침({first.get('doc_name')}, p.{first.get('page')})에 따르면, "
            f"고령 근로자의 안전을 위해 다음 사항에 유의해야 합니다: {first.get('content')[:100]}..."
        )
    lines.append("이 분석은 참고용 지침이므로 현장 안전 관리 지침을 함께 준수해 주십시오.")
    return " ".join(lines)


def generate_rag_explanation(
    title: str,
    risk_info: dict,
    chunks: list[dict],
) -> dict:
    """안전 지침 근거를 바탕으로 설명 문장을 생성하고 인용 정보를 포함합니다.
    
    근거가 부족하면(유사도 미달 또는 청크 없음) 답변을 보류합니다.
    
    반환값:
        {
            "explanation": "설명 문장",
            "is_abstained": False,  # 보류 여부
            "citations": [...],     # 인용 문서 목록
            "source": "gemini" 또는 "fallback" 또는 "abstained"
        }
    """
    # 1. 근거 부족 시 답변 보류 (Abstain) 검사
    if not chunks:
        return {
            "explanation": "관련 고령자 직무 안전 지침 근거를 찾을 수 없어 답변을 보류합니다. 현장 관리자가 지침을 직접 확인해 주세요.",
            "is_abstained": True,
            "citations": [],
            "source": "abstained",
        }

    best_score = max(c.get("rerank_score", c.get("similarity", 0.0)) for c in chunks)
    if best_score < MIN_EVIDENCE_THRESHOLD:
        return {
            "explanation": (
                f"검색된 지침과의 연관도 점수({best_score})가 기준치({MIN_EVIDENCE_THRESHOLD})보다 낮아 "
                "안전 판단 근거가 부족하므로 답변을 보류합니다. 담당자가 안전보건공단 지침을 직접 확인해 주세요."
            ),
            "is_abstained": True,
            "citations": format_citations(chunks),
            "source": "abstained",
        }

    citations = format_citations(chunks)

    # 2. Gemini 호출을 위한 프롬프트 구성
    api_key = os.getenv("GEMINI_API_KEY", "")
    if api_key:
        try:
            from google import genai
            from google.genai import types

            context_lines = []
            for i, c in enumerate(chunks, 1):
                context_lines.append(
                    f"[{i}] 문서: {c.get('doc_name')} (p.{c.get('page')}, 출처: {c.get('source')})\n"
                    f"내용: {c.get('content')}"
                )
            context_str = "\n\n".join(context_lines)

            prompt = (
                "너는 고령자 일자리 안전 평가 및 직무 배치 상담을 돕는 안전보건 전문가다.\n"
                "반드시 아래에 제공된 [공식 안전 지침]에만 기반하여, 직무의 위험 요인과 고령자 보호 대책을 3문장 내외로 설명하라.\n"
                "제공된 지침에 없는 내용은 추측하거나 단정하지 말고, 문장 끝에 반드시 인용한 문서명과 페이지를 명시하라.\n\n"
                f"[평가 대상 직무]: {title}\n"
                f"[참고 위험도 지수]: {risk_info.get('risk_score', 0)}점 (등급: {GRADE_NAMES.get(risk_info.get('risk_grade'), '보통')})\n\n"
                f"[공식 안전 지침]:\n{context_str}\n"
            )

            client = genai.Client(
                api_key=api_key,
                http_options=types.HttpOptions(timeout=15000),
            )
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=prompt,
            )
            if response.text and response.text.strip():
                return {
                    "explanation": response.text.strip(),
                    "is_abstained": False,
                    "citations": citations,
                    "source": "gemini",
                }
        except Exception as error:
            print(f"Gemini 설명 생성 실패, 기본 템플릿 사용: {error}")

    # 3. Gemini 미사용 시 기본 폴백 설명
    return {
        "explanation": build_fallback_explanation(title, risk_info, chunks),
        "is_abstained": False,
        "citations": citations,
        "source": "fallback",
    }

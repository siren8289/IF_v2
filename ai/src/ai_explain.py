"""생성형 AI(Gemini)로 결과 설명 문장을 만든다.

GEMINI_API_KEY가 없거나 호출이 실패하면 미리 정해 둔 기본 문장을 쓴다.
"""
import os

GRADE_NAMES = {"LOW": "낮음", "MID": "보통", "HIGH": "높음"}


def basic_explanation(result):
    """AI 없이 만드는 기본 설명"""
    grade = GRADE_NAMES[result["risk_grade"]]
    biggest = max(result["factors"], key=lambda factor: factor["points"])
    return (
        f"참고 지수는 {result['risk_score']}점({grade})입니다. "
        f"가장 크게 반영된 항목은 '{biggest['name']}'입니다. "
        "이 점수는 사고 확률이 아니므로 담당자가 실제 작업 조건을 함께 확인해 주세요."
    )


def make_prompt(title, result):
    lines = [
        "너는 고령자 일자리 상담을 돕는 도우미다.",
        "아래 참고 지수 결과를 보고 담당자에게 3문장 이내의 쉬운 한국어로 설명해라.",
        "사고 확률이나 안전 여부를 단정하지 말고, 확인할 점을 알려줘라.",
        "",
        f"직무: {title}",
        f"점수: {result['risk_score']}점 / 등급: {GRADE_NAMES[result['risk_grade']]}",
    ]
    for factor in result["factors"]:
        lines.append(f"- {factor['name']}: {factor['points']}점 (최대 {factor['max']}점)")
    return "\n".join(lines)


def explain(title, result):
    """(설명 문장, 출처) 를 돌려준다. 출처는 "gemini" 또는 "basic"."""
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return basic_explanation(result), "basic"

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=15000),  # 15초
        )
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=make_prompt(title, result),
        )
        if response.text:
            return response.text.strip(), "gemini"
    except Exception as error:
        print("Gemini 호출 실패, 기본 설명을 사용합니다:", type(error).__name__)

    return basic_explanation(result), "basic"

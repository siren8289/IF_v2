"""생성형 AI(Gemini)로 결과 설명 문장을 만든다.

GEMINI_API_KEY가 없거나 호출이 실패하면 미리 정해 둔 기본 문장을 쓴다.
그래서 API 키가 없어도 분석 자체는 끝까지 끝난다.
"""
import os

# 등급 코드를 상담사가 읽는 말로 바꾼다. 점수 계산은 영어 코드를 그대로 쓴다.
GRADE_NAMES = {"LOW": "낮음", "MID": "보통", "HIGH": "높음"}


def basic_explanation(result):
    """AI 없이 만드는 기본 설명.

    점수, 등급, 가장 점수가 큰 항목만 문장으로 잇는다.
    사고 확률이라고 말하지 말라고 마지막 문장에 적어 둔다.
    """
    grade = GRADE_NAMES[result["risk_grade"]]
    # factors 안에서 points가 가장 큰 항목 하나를 고른다.
    biggest = max(result["factors"], key=lambda factor: factor["points"])
    return (
        f"참고 지수는 {result['risk_score']}점({grade})입니다. "
        f"가장 크게 반영된 항목은 '{biggest['name']}'입니다. "
        "이 점수는 사고 확률이 아니므로 담당자가 실제 작업 조건을 함께 확인해 주세요."
    )


def make_prompt(title, result):
    """Gemini에게 보낼 지시문. 역할, 금지 사항, 점수 내역을 한 글에 담는다."""
    lines = [
        "너는 고령자 일자리 상담을 돕는 도우미다.",
        "아래 참고 지수 결과를 보고 담당자에게 3문장 이내의 쉬운 한국어로 설명해라.",
        # 모델이 "위험하다/안전하다"고 단정하지 않게 막는다.
        "사고 확률이나 안전 여부를 단정하지 말고, 확인할 점을 알려줘라.",
        "",
        f"직무: {title}",
        f"점수: {result['risk_score']}점 / 등급: {GRADE_NAMES[result['risk_grade']]}",
    ]
    # 항목별 점수를 불릿으로 붙여, 모델이 없는 숫자를 지어내지 않게 한다.
    for factor in result["factors"]:
        lines.append(f"- {factor['name']}: {factor['points']}점 (최대 {factor['max']}점)")
    return "\n".join(lines)


def explain(title, result):
    """(설명 문장, 출처) 를 돌려준다. 출처는 "gemini" 또는 "basic".

    화면은 출처를 보고 "생성형 AI가 작성"인지 "기본 설명"인지 표시한다.
    """
    # 환경 변수에 키가 없으면 외부 AI를 부르지 않고 기본 문장을 쓴다.
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return basic_explanation(result), "basic"

    try:
        # 키가 있을 때만 구글 라이브러리를 불러온다. 없어도 서버가 켜지게 하려는 것이다.
        from google import genai
        from google.genai import types

        client = genai.Client(
            api_key=api_key,
            # 15초 안에 답이 없으면 실패로 보고 기본 문장으로 넘어간다.
            http_options=types.HttpOptions(timeout=15000),
        )
        response = client.models.generate_content(
            # 모델 이름은 환경 변수로 바꿀 수 있다. 없으면 gemini-2.5-flash.
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=make_prompt(title, result),
        )
        # 빈 답이면 성공으로 치지 않고 아래 기본 문장으로 떨어진다.
        if response.text:
            return response.text.strip(), "gemini"
    except Exception as error:
        # 네트워크 오류, 키 오류, 할당량 초과 모두 여기로 온다.
        # 사용자에게는 분석을 실패로 돌리지 않고 기본 설명을 준다.
        print("Gemini 호출 실패, 기본 설명을 사용합니다:", type(error).__name__)

    return basic_explanation(result), "basic"

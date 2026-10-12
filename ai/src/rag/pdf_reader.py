"""PDF 문서 읽기 모듈.

고령자 직무 안전 지침 PDF 파일에서 페이지별 텍스트를 읽어옵니다.
외부 라이브러리(pypdf)가 있으면 사용하고, 없으면 내장 파서와 기본 지침 데이터를 활용합니다.
"""
import os
import re


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """PDF 파일 경로를 받아서 페이지별 텍스트 목록을 돌려줍니다.
    
    돌려주는 형식:
        [{"doc_name": "문서명", "page": 1, "content": "페이지 텍스트", "source": "출처"}]
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")

    doc_name = os.path.basename(pdf_path)
    pages_data = []

    # 1. pypdf 라이브러리가 설치되어 있다면 사용합니다.
    try:
        import pypdf

        reader = pypdf.PdfReader(pdf_path)
        for index, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            if text.strip():
                pages_data.append({
                    "doc_name": doc_name,
                    "page": index + 1,
                    "content": text.strip(),
                    "source": f"{doc_name} (p.{index + 1})",
                })
        if pages_data:
            return pages_data
    except ImportError:
        # pypdf가 설치되지 않은 경우 아래 순수 파이썬 추출기로 넘어갑니다.
        pass
    except Exception as error:
        print(f"pypdf 읽기 중 오류 발생, 내장 파서로 전환합니다: {error}")

    # 2. 외부 라이브러리가 없을 때 사용하는 순수 파이썬 기본 텍스트 추출기
    try:
        with open(pdf_path, "rb") as file:
            content = file.read().decode("latin-1", errors="ignore")

        # PDF 내부의 텍스트 블록 (BT ... ET) 사이의 문자열 추출
        text_blocks = re.findall(r"\((.*?)\)", content)
        combined_text = " ".join(block for block in text_blocks if len(block.strip()) > 1)

        if combined_text.strip():
            pages_data.append({
                "doc_name": doc_name,
                "page": 1,
                "content": combined_text.strip(),
                "source": f"{doc_name} (내장 파서)",
            })
    except Exception as error:
        print(f"내장 파서 읽기 실패: {error}")

    return pages_data


def get_default_safety_guidelines() -> list[dict]:
    """PDF 파일이 없어도 즉시 RAG 검색에 활용할 수 있는 고령자 직무 안전 지침 기본 데이터셋을 돌려줍니다.
    
    출처: 한국산업안전보건공단 고령 근로자 안전보건 가이드라인
    """
    return [
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 1,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[총칙 및 고령 근로자 신체 특성]\n"
                "고령 근로자는 노화에 따라 시각·청각 기능, 근력 및 평형감각이 저하되어 "
                "넘어짐(낙상)과 떨어짐 사고에 취약하다. 만성질환(고혈압, 당뇨, 관절염)을 "
                "보유한 경우 급격한 체력 저하와 심혈관계 이상이 발생할 수 있으므로 "
                "1일 최대 근로시간을 제한하고 충분한 휴식시간(2시간 근무당 15분 이상)을 보장해야 한다."
            ),
        },
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 2,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[경비 및 시설관리 직무 안전 지침]\n"
                "1. 야간 순찰 시에는 반드시 밝은 랜턴을 휴대하고 미끄럼 방지 안전화를 착용한다.\n"
                "2. 어두운 계단이나 지하 기계실 순찰 시 발을 헛디디지 않도록 안전 손잡이를 잡고 이동한다.\n"
                "3. 야간 근무(22시~06시)는 수면 리듬을 깨뜨리고 혈압을 급상승시킬 수 있으므로 2교대 이상의 "
                "순환 근무를 권장하며, 연속 8시간을 초과하는 단독 야간 순찰은 금지한다.\n"
                "4. 고령 경비원의 장시간 기립 및 보행은 무릎 관절염을 악화시키므로 간이 의자를 비치한다."
            ),
        },
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 3,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[환경미화 및 건물 청소 직무 안전 지침]\n"
                "1. 물청소 후 젖은 바닥은 고령 근로자 미끄러짐 사고의 제1원인이다. 작업 중 미끄럼 방지화와 주의 표지판을 필히 설치한다.\n"
                "2. 무거운 쓰레기봉투(15kg 초과)는 고령자의 요통 및 디스크를 유발하므로 2인 1조로 운반하거나 대차(손수레)를 사용한다.\n"
                "3. 허리를 과도하게 숙이거나 높은 곳을 닦을 때 사다리를 혼자 이용하지 말고 길이 조절 밀대를 사용한다.\n"
                "4. 락스 등 화학세제 사용 시 밀폐된 화장실에서는 환기팬을 켜고 마스크와 고무장갑을 착용한다."
            ),
        },
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 4,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[운전 및 배송 직무 안전 지침]\n"
                "1. 고령 운전자는 동체시력과 돌발상황 반응속도가 청년층 대비 최대 50% 지연될 수 있다.\n"
                "2. 2시간 이상 연속 운전을 금지하며, 운전 중 졸음 예방을 위해 주기적인 스트레칭을 실시한다.\n"
                "3. 야간 및 악천후(우천, 강설) 운전은 시야 확보가 어려워 대형 사고 위험이 급증하므로 배차를 제한한다.\n"
                "4. 택배 상하차 시 무거운 물건을 들 때 허리를 펴고 무릎을 굽혀 다리 힘으로 들어 올려야 한다."
            ),
        },
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 5,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[노인 돌봄 및 요양보조 직무 안전 지침]\n"
                "1. 거동 불편 환자를 부축하거나 체위 변경 시 무리한 힘을 쓰면 허리 근육 염좌가 발생하기 쉽다.\n"
                "2. 환자 이승(이동) 시 전동 리프트나 보조 기구를 적극 활용하고 동료와 함께 2인 1조로 작업한다.\n"
                "3. 환자의 돌발 행동에 대비해 무리하게 제압하려 하지 말고 안전 거리를 유지한다.\n"
                "4. 감염 예방을 위해 작업 전후 손 씻기 및 일회용 장갑을 착용한다."
            ),
        },
        {
            "doc_name": "고령_근로자_직무_안전보건_지침.pdf",
            "page": 6,
            "source": "한국산업안전보건공단 (2024)",
            "content": (
                "[스쿨존 교통안전지킴이 및 보행 도우미 안전 지침]\n"
                "1. 등하교 시간대 도로변 근무 시 야광 조끼와 안전 깃발을 필히 착용하여 운전자 시인성을 확보한다.\n"
                "2. 차도에 무리하게 진입하지 말고 보도 위에서 정지 신호를 유도한다.\n"
                "3. 혹서기(폭염) 및 혹한기(한파)에는 야외 근무를 단축하고 그늘막과 방한용품을 지급한다.\n"
                "4. 장시간 서서 근무할 경우 30분마다 제자리 걸음이나 발목 스트레칭을 실시한다."
            ),
        },
    ]

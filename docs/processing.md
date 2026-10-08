# Processing

`external_normalization.py`는 공공 payload 파싱, 필드 매핑, 타입 정규화, 필수 필드 검사와 natural key 중복 제거를 담당합니다. 수집 모듈이 이 함수를 호출하며 입력·출력 계약은 기존 ETL과 같습니다. AI 전용 전처리는 기존 `ai/src/etl/`에 유지합니다.

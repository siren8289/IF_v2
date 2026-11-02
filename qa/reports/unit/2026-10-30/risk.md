# RISK
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:39 KST)

- **검출/추적 리스크 건수**: 1건

### [RISK-UNIT-001] data/etl/transform.py 깨진 원본(Malformed XML/JSON) 파싱 시 예외 방어 부재 (심각도: **MEDIUM**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `UNIT-DAT-001`
- **실행 일시**: `2026-10-30 17:32:26 KST`
- **기능명 / 테스트 종류**: Data ETL 비정상 응답 파싱 예외 처리 (`unit`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `Python unittest CLI` → 정상 XML/JSON 입력 PASS
- **도구 B 및 결과**: `Static AST & Exception Path Inspector` → parse_data() 내 JSONDecodeError / ET.ParseError 방어 블록 미존재 확인
- **대상 코드 위치**: 파일 `data/etl/transform.py` / 함수 `parse_data` / 줄 번호 `11-36`
- **심각도 (Severity)**: **MEDIUM**
- **발생 가능성 (Likelihood)**: **MEDIUM**
- **영향 (Impact)**: 공공데이터 API가 점검 페이지(HTML)나 깨진 XML/JSON을 반환할 경우 parse_data() 내부 json.loads / ET.fromstring에서 비포착 예외가 발생하여 배치 중단 가능
- **상세 내용**: parse_data()가 json.loads() 및 ET.fromstring() 호출 시 try-except 없이 바로 파싱하므로 외부 API 장애 응답 수신 시 파이프라인이 즉시 중단됨.
- **권장 조치 (Recommendation)**: json.loads 및 ET.fromstring 호출부를 try-except로 감싸고 로깅 후 빈 리스트([]) 또는 명시적 ETL 예외를 반환하도록 개선 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:32:26 KST (RUN-20261030-001) 최초 검출 및 risk.md 선기록 완료


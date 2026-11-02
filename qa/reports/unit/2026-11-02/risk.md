# RISK

## 20261102T130018-a7c3e91b04
- IF-0178~IF-0246에서 새 RISK는 없다. FAIL도 없다.
- 작업 라벨을 모두 1로 두면 행 합은 48이다. calculate_score에 들어가는 작업 factor는 94행 min(total, 30) 때문에 30이다. IF-0245 기대 30, IF-0246 기대 100과 맞다.
- IF-0241 건강 12.5는 factor에 12.5로 남고, 총점만 Python round로 12가 된다.
- 기존 ai/tests/test_risk_score.py는 5 passed다. StarletteDeprecationWarning 1건은 실패가 아니다.
- Ruff E9,F63,F7,F82는 통과했다. 문법 검사이므로 이 시트 숫자의 재검증으로 세지 않는다.
- 공식 게이트 scripts/qa/run.py는 파일이 없어 실행하지 않았다.
- RISK-SEC-001, RISK-LEGACY-FAILS, RISK-QA-AUTH는 이 실행에서 다시 검증하지 않았다. 상태는 그대로다.
- 제품 코드는 수정하지 않았다. Postgres는 호출하지 않았다.

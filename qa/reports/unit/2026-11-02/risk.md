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

## 20261102T131137-c6d14f0a82
- IF-0247~IF-0255에서 새 RISK는 없다. FAIL도 없다.
- Gemini 클라이언트는 sys.modules의 가짜 google.genai다. 네트워크 호출은 없다.
- Ruff E9,F63,F7,F82는 통과했다. 문법 검사이므로 이 시트 분기의 재검증으로 세지 않는다.
- 공식 게이트 scripts/qa/run.py는 파일이 없어 실행하지 않았다.
- RISK-SEC-001, RISK-LEGACY-FAILS, RISK-QA-AUTH는 이 실행에서 다시 검증하지 않았다.
- 제품 코드는 수정하지 않았다. Postgres는 호출하지 않았다.

## 20261102T131746-e5a91c7b20
- IF-0259, IF-0268은 FAIL이다. 새 RISK ID는 만들지 않았다.
- 없는 모델 파일은 FileNotFoundError가 된다. 로그 레코드와 서버 오류 기록은 없다.
- 원인 위치는 ml_model.py load_ml_models 27행, dl_model.py load_dl_model 76행이다. 제품 코드는 수정하지 않았다.
- 실제 ai/models/task_ml.joblib, task_cnn.pt의 크기와 mtime은 테스트 전후가 같다.
- Ruff는 문법 검사이므로 이 실패의 재검증으로 세지 않는다.
- 공식 게이트 scripts/qa/run.py는 파일이 없어 실행하지 않았다.
- RISK-SEC-001, RISK-LEGACY-FAILS, RISK-QA-AUTH는 이 실행에서 다시 검증하지 않았다.

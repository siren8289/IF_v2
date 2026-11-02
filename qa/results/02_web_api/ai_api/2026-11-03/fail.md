# FAIL

## 20261103T023608-84ddceb76c / TC-WEBAPI-AI-001
- RUN_ID: 20261103T023608-84ddceb76c
- TC_ID: TC-WEBAPI-AI-001
- FEATURE_ID: FEAT-AI-API
- timestamp_start: 2026-11-03T02:55:25+09:00
- timestamp_end: 2026-11-03T02:57:56+09:00
- area: 02_web_api
- section: ai_api
- scenario: 위험점수·RAG·OpenAPI
- tool_a: pytest
- command_a: python3 -m pytest tests -q --junitxml=../qa/.runtime/20261103T023608-84ddceb76c/TC-WEBAPI-AI-001-a.xml
- result_a: FAIL
- expected_a: PASS
- actual_a: arlette.testclient` is deprecated; install `httpx2` instead. from starlette.testclient import TestClient as TestClient # noqa -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html =========================== short test summary info ============================ FAILED tests/te
- tool_b: schemathesis_or_openapi
- command_b: python3 scripts/qa/probes/openapi_check.py --base http://127.0.0.1:8000
- result_b: PASS
- expected_b: PASS
- actual_b: OK openapi paths=2 NOTE schemathesis not installed; OpenAPI document check only
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/risk_score.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023608-84ddceb76c/pytest.log#e39982b1b67f927f;qa/.runtime/20261103T023608-84ddceb76c/schemathesis_or_openapi.log#612ffb384963b5e8

시나리오: 위험점수·RAG·OpenAPI
비교: pytest API/로직 + OpenAPI/Schemathesis 독립 검사(서버 없으면 BLOCKED).
1차: pytest 기대=PASS 실제=FAIL
2차: schemathesis_or_openapi 기대=PASS 실제=PASS
최종=FAIL. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-WEBAPI-AI-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-WEBAPI-AI-001
- FEATURE_ID: FEAT-AI-API
- timestamp_start: 2026-11-03T04:00:18+09:00
- timestamp_end: 2026-11-03T04:04:15+09:00
- area: 02_web_api
- section: ai_api
- scenario: pytest API/로직 + OpenAPI/Schemathesis 독립 검사(서버 없으면 BLOCKED).
- tool_a: pytest
- command_a: python3 -m pytest tests -q --junitxml=../qa/.runtime/20261103T034221-c3386f4577/TC-WEBAPI-AI-001-a.xml
- result_a: FAIL
- expected_a: PASS
- actual_a: arlette.testclient` is deprecated; install `httpx2` instead. from starlette.testclient import TestClient as TestClient # noqa -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html =========================== short test summary info ============================ FAILED tests/te
- tool_b: schemathesis_or_openapi
- command_b: python3 scripts/qa/probes/openapi_check.py --base http://127.0.0.1:8000
- result_b: PASS
- expected_b: PASS
- actual_b: OK openapi paths=2 NOTE schemathesis not installed; OpenAPI document check only
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/pytest.log#9fc5f6d0103042c6;qa/.runtime/20261103T034221-c3386f4577/schemathesis_or_openapi.log#612ffb384963b5e8

시나리오: pytest API/로직 + OpenAPI/Schemathesis 독립 검사(서버 없으면 BLOCKED).
비교: pytest API/로직 + OpenAPI/Schemathesis 독립 검사(서버 없으면 BLOCKED).
1차: pytest 기대=PASS 실제=FAIL
2차: schemathesis_or_openapi 기대=PASS 실제=PASS
최종=FAIL. 미실행을 PASS로 처리하지 않음.

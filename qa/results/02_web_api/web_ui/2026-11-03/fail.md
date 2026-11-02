# FAIL

## 20261103T023608-84ddceb76c / TC-WEBAPI-UI-001
- RUN_ID: 20261103T023608-84ddceb76c
- TC_ID: TC-WEBAPI-UI-001
- FEATURE_ID: FEAT-WEB-UI
- timestamp_start: 2026-11-03T02:57:56+09:00
- timestamp_end: 2026-11-03T02:57:56+09:00
- area: 02_web_api
- section: web_ui
- scenario: UI 스모크와 루트 HTTP
- tool_a: Playwright
- command_a: python3 scripts/qa/probes/playwright_smoke.py
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: NOT_RUN: Playwright Python package missing; install before UI E2E PASS
- tool_b: http_blackbox
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1 --path /
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1/ bytes=200
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: web-vite
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-V30-003
- evidence: qa/.runtime/20261103T023608-84ddceb76c/Playwright.log#b9fbf5a9881c4b9e;qa/.runtime/20261103T023608-84ddceb76c/http_blackbox.log#2cff014da314bd46

RISK RISK-V30-003
시나리오: UI 스모크와 루트 HTTP
비교: Playwright UI 스모크 + 독립 HTTP 스모크. Schemathesis는 OpenAPI TC로 분리.
1차: Playwright 기대=PASS 실제=NOT_RUN
2차: http_blackbox 기대=PASS 실제=PASS
최종=NOT_RUN. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-WEBAPI-UI-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-WEBAPI-UI-001
- FEATURE_ID: FEAT-WEB-UI
- timestamp_start: 2026-11-03T04:00:12+09:00
- timestamp_end: 2026-11-03T04:00:16+09:00
- area: 02_web_api
- section: web_ui
- scenario: Playwright UI 스모크 + 독립 HTTP 스모크. Schemathesis는 OpenAPI TC로 분리.
- tool_a: Playwright
- command_a: python3 scripts/qa/probes/playwright_smoke.py
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: NOT_RUN: Playwright Python package missing; install before UI E2E PASS
- tool_b: http_blackbox
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1 --path /
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1/ bytes=200
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-V30-003
- evidence: qa/.runtime/20261103T034221-c3386f4577/Playwright.log#b9fbf5a9881c4b9e;qa/.runtime/20261103T034221-c3386f4577/http_blackbox.log#2cff014da314bd46

RISK RISK-V30-003
시나리오: Playwright UI 스모크 + 독립 HTTP 스모크. Schemathesis는 OpenAPI TC로 분리.
비교: Playwright UI 스모크 + 독립 HTTP 스모크. Schemathesis는 OpenAPI TC로 분리.
1차: Playwright 기대=PASS 실제=NOT_RUN
2차: http_blackbox 기대=PASS 실제=PASS
최종=NOT_RUN. 미실행을 PASS로 처리하지 않음.

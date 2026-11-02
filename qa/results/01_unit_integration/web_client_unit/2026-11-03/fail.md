# FAIL

## 20261103T023608-84ddceb76c / TC-UNIT-WEB-001
- RUN_ID: 20261103T023608-84ddceb76c
- TC_ID: TC-UNIT-WEB-001
- FEATURE_ID: FEAT-WEB-UNIT
- timestamp_start: 2026-11-03T02:36:09+09:00
- timestamp_end: 2026-11-03T02:38:56+09:00
- area: 01_unit_integration
- section: web_client_unit
- scenario: 프론트 단위·타입 회귀
- tool_a: Vitest
- command_a: npm test -- --reporter=default --reporter=junit --outputFile=../qa/.runtime/20261103T023608-84ddceb76c/TC-UNIT-WEB-001-a.xml
- result_a: FAIL
- expected_a: PASS
- actual_a: ges/pages.test.tsx > 화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다 Error: Test timed out in 5000ms. If this is a long-running test, pass a timeout value as the last argument or configure it globally with "testTimeout". ❯ src/pages/pages.test.tsx:44:3 42| }); 43| 44| it("평가 입력 후 POST 한 번
- tool_b: TypeScript
- command_b: npm run typecheck
- result_b: PASS
- expected_b: PASS
- actual_b: > if-web-vite@0.2.0 typecheck > tsc --noEmit
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: web-vite/src/pages/pages.test.tsx
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023608-84ddceb76c/Vitest.log#124afba98acf4b10;qa/.runtime/20261103T023608-84ddceb76c/TypeScript.log#03d193eb3ee4ef77

시나리오: 프론트 단위·타입 회귀
비교: Vitest 동작 + tsc 정적. UI E2E는 TC-WEBAPI-UI-001(Playwright)로 분리.
1차: Vitest 기대=PASS 실제=FAIL
2차: TypeScript 기대=PASS 실제=PASS
최종=FAIL. 미실행을 PASS로 처리하지 않음.

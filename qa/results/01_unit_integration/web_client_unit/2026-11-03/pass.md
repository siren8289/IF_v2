# PASS

## 20261103T034221-c3386f4577 / TC-UNIT-WEB-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-UNIT-WEB-001
- FEATURE_ID: FEAT-WEB-UNIT
- timestamp_start: 2026-11-03T03:56:19+09:00
- timestamp_end: 2026-11-03T04:00:11+09:00
- area: 01_unit_integration
- section: web_client_unit
- scenario: Vitest 동작 + tsc 정적. UI E2E는 TC-WEBAPI-UI-001(Playwright)로 분리.
- tool_a: Vitest
- command_a: npm test -- --reporter=default --reporter=junit --outputFile=../qa/.runtime/20261103T034221-c3386f4577/TC-UNIT-WEB-001-a.xml
- result_a: PASS
- expected_a: PASS
- actual_a: .test.ts (4 tests) 503ms ✓ src/pages/pages.test.tsx (3 tests) 10250ms ✓ 화면 (3) ✓ 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다 2240ms ✓ 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다 3213ms ✓ 입력값이 잘못되면 API를 호출하지 않는다 4297ms Test Files 2 passed (2) Tests 7 passed (7) Start at 03:57:00 Duration
- tool_b: TypeScript
- command_b: npm run typecheck
- result_b: PASS
- expected_b: PASS
- actual_b: > if-web-vite@0.2.0 typecheck > tsc --noEmit
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/Vitest.log#a3e7bcc53646ce1c;qa/.runtime/20261103T034221-c3386f4577/TypeScript.log#03d193eb3ee4ef77

시나리오: Vitest 동작 + tsc 정적. UI E2E는 TC-WEBAPI-UI-001(Playwright)로 분리.
비교: Vitest 동작 + tsc 정적. UI E2E는 TC-WEBAPI-UI-001(Playwright)로 분리.
1차: Vitest 기대=PASS 실제=PASS
2차: TypeScript 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

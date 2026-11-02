# PASS

## 20261030T172455-160ef4c9a6 / QA-WEB
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-WEB
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T172455-160ef4c9a6/QA-WEB-a.log sha256=9bf13639e760400f313fd7a54e5fe55801b6d5b46f0b0090c8ccbdae5d8557d2; qa/.runtime/evidence/unit/2026-10-30/20261030T172455-160ef4c9a6/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T172455-160ef4c9a6 / QA-DATA
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-DATA
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T172455-160ef4c9a6/QA-DATA-a.log sha256=11867943893057b8045126b8d08e9373c40af67aad3c638bf8d548c8a65541e0; qa/.runtime/evidence/unit/2026-10-30/20261030T172455-160ef4c9a6/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173027-a0890b20ec/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-a.log sha256=55a0428c4aa46d97022d432300206dfc3983733e926810b4ef6974a75cdccdea; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-web.xml sha256=49ed6f5f89a78dd40d17bb03f4db711fd6987fb1f2b426174da66734d3feee2c; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-DATA
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-DATA
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-QA-DATA.xml sha256=24fb65598c88354da0f87378000358ba6ef0ea41b3a165adcdbf4beb5ef41f02

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-QA-DATA.xml sha256=24fb65598c88354da0f87378000358ba6ef0ea41b3a165adcdbf4beb5ef41f02

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-QA-DATA.xml sha256=24fb65598c88354da0f87378000358ba6ef0ea41b3a165adcdbf4beb5ef41f02

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173027-a0890b20ec/QA-DATA-QA-DATA.xml sha256=24fb65598c88354da0f87378000358ba6ef0ea41b3a165adcdbf4beb5ef41f02

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:39 KST)

- **통과 건수**: 6건 / 전체 6건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `UNIT-SPR-001` | 2026-10-30 17:32:26 KST | Spring AssessmentController 슬라이스/단위 검증 (나이 범위 400, 미존재 404, 목록/요약 200) | `Gradle JUnit5 (./gradlew test)` (PASS (BUILD SUCCESSFUL)) | `JUnit XML Report Parser (TEST-AssessmentControllerTest.xml)` (PASS (tests=3, failures=0, errors=0)) | **PASS** | `9491fb1b` | `spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java` | `AssessmentControllerTest` | `24-56` | `-` | **목적**: 컨트롤러 입력 검증(age=200 -> 400), 미존재 결과 조회(404), 목록/요약/직무 조회(200) 확인<br>**기대**: 3개 테스트 메서드 모두 failures=0, errors=0 통과<br>**실제/근거**: Gradle rc=0, XML tests=3, failures=0, errors=0 (spring/build/test-results/test/TEST-com.example.demo.assessment.AssessmentControllerTest.xml) |
| `RUN-20261030-001` | `UNIT-SPR-002` | 2026-10-30 17:32:26 KST | Spring AssessmentService 비즈니스 로직 단위 검증 (AI 저장, 범위 외 점수 거절, 삭제) | `Gradle JUnit5 (./gradlew test)` (PASS (BUILD SUCCESSFUL)) | `JUnit XML Report Parser (TEST-AssessmentServiceTest.xml)` (PASS (tests=3, failures=0, errors=0)) | **PASS** | `9491fb1b` | `spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java` | `AssessmentServiceTest` | `32-114` | `-` | **목적**: AI 응답 정상 저장(65점 HIGH), 범위 초과 점수(150점) ApiException 발생, 평가 삭제 검증<br>**기대**: 3개 테스트 메서드 모두 failures=0, errors=0 통과<br>**실제/근거**: Gradle rc=0, XML tests=3, failures=0, errors=0 (spring/build/test-results/test/TEST-com.example.demo.assessment.AssessmentServiceTest.xml) |
| `RUN-20261030-001` | `UNIT-AI-001` | 2026-10-30 17:32:26 KST | AI 위험도 등급 경계값(40/41, 60/61) 및 0~100점 상하한 계산 검증 | `Host Python 3.11 Direct Module Assertion (ai.src.risk_score)` (PASS (min=0, max=100)) | `Docker FastAPI Python 3.12 Runtime Verifier` (PASS (40=LOW, 41=MID, 60=MID, 61=HIGH, score 0..100 일치)) | **PASS** | `9491fb1b` | `ai/src/risk_score.py` | `grade_of, calculate_score` | `97-131` | `-` | **목적**: ISTQB 경계값 분석에 따라 등급 경계(40/41, 60/61)와 최솟값(0점)/최댓값(100점) 캡핑 검증<br>**기대**: 40->LOW, 41->MID, 60->MID, 61->HIGH 및 최솟값 0, 최댓값 100 반환<br>**실제/근거**: min=0(LOW), max=100(HIGH) (ai/tests/test_risk_score.py & ai/src/risk_score.py:97-131) |
| `RUN-20261030-001` | `UNIT-AI-002` | 2026-10-30 17:32:26 KST | AI 설명 생성기(explain) API 키 미설정 시 규칙 기반 기본 설명(basic) 폴백 검증 | `Host Python 3.11 Direct Call (ai.src.ai_explain.explain)` (PASS (source=basic, len=98)) | `Docker FastAPI Python 3.12 Runtime Verifier` (PASS (basic fallback 문장 생성 확인)) | **PASS** | `9491fb1b` | `ai/src/ai_explain.py` | `explain, basic_explanation` | `12-78` | `-` | **목적**: GEMINI_API_KEY 부재 또는 실패 시 분석 중단 없이 기본 설명 문장과 출처(basic)를 반환하는지 검증<br>**기대**: 비어 있지 않은 한국어 설명 문자열 및 유효 출처 반환<br>**실제/근거**: source=basic, text='참고 지수는 100점(높음)입니다. 가장 크게 반영된 항목은 '작업 특성 (ML+...' (ai/src/ai_explain.py:45-78) |
| `RUN-20261030-001` | `UNIT-DAT-001` | 2026-10-30 17:32:26 KST | Data ETL XML/JSON 파싱 및 필수값·중복 제거(normalize_rows) 단위 검증 | `Python unittest CLI (python3 -m unittest discover -s data/tests -v)` (PASS (Ran 3 tests OK)) | `Direct ETL Function Edge-Case Harness (parse_data & normalize_rows)` (PASS (xml=1건, dedup_filtered=1건)) | **PASS** | `9491fb1b` | `data/etl/transform.py` | `parse_data, normalize_rows` | `11-97` | `-` | **목적**: XML/JSON 원본 파싱, 필수 필드 누락 행 제외, 중복 키 제거 로직 검증<br>**기대**: unittest 3건 통과 및 빈 필수값/중복 행 필터링 후 1건 반환<br>**실제/근거**: unittest rc=0, xml_rows=1, dedup_rows=1 (data/tests/test_transform.py:1-57) |
| `RUN-20261030-001` | `UNIT-WEB-001` | 2026-10-30 17:32:26 KST | Frontend API 클라이언트(client.ts) 및 페이지 컴포넌트(pages.test.tsx) 단위·타입 교차 검증 | `Vitest Runner (npm test -> client.test.ts, pages.test.tsx)` (PASS (2 test files, 7 tests passed)) | `TypeScript Compiler (npm run typecheck -> tsc --noEmit)` (PASS (타입 오류 0건)) | **PASS** | `9491fb1b` | `web-vite/src/pages/pages.test.tsx` | `apiRequest, DashboardPage, AssessmentFormPage` | `1-80` | `-` | **목적**: React 컴포넌트 렌더링·폼 검증·API 클라이언트(204/에러 파싱) 동작과 TypeScript 정적 타입 일치성 교차 검증<br>**기대**: Vitest 7개 테스트 모두 통과 및 tsc --noEmit 종료 코드 0<br>**실제/근거**: vitest rc=0, tsc rc=0 (web-vite/src/shared/api/client.test.ts & web-vite/src/pages/pages.test.tsx) |


## 20261030T173746-09edf77edc / QA-WEB
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T173746-09edf77edc/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-a.log sha256=fd1b579418f23b39a8212e260a5200afa8ca0ec06717c13a37e668d44c7fd151; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-web.xml sha256=963b1636adddc6126869b0d3d062298afea8f9bda190eebfeec02f33b762e122; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-DATA
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-DATA
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-a.log sha256=decf2a3694869d0ccf5cb4b25c5522eeb8a06225fbe083ccdf017bcfe23fa2ba; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-QA-DATA.xml sha256=9fee768ffc13d725daea68d363887646efd36d6a9587db99fdf7edb62a3f1a7a

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-a.log sha256=decf2a3694869d0ccf5cb4b25c5522eeb8a06225fbe083ccdf017bcfe23fa2ba; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-QA-DATA.xml sha256=9fee768ffc13d725daea68d363887646efd36d6a9587db99fdf7edb62a3f1a7a

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-a.log sha256=decf2a3694869d0ccf5cb4b25c5522eeb8a06225fbe083ccdf017bcfe23fa2ba; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-QA-DATA.xml sha256=9fee768ffc13d725daea68d363887646efd36d6a9587db99fdf7edb62a3f1a7a

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-a.log sha256=decf2a3694869d0ccf5cb4b25c5522eeb8a06225fbe083ccdf017bcfe23fa2ba; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-b.log sha256=e0a6ea218ea5d725ce7272da8d68d45a029e489423e03af6960c7bff0f7fe414; qa/.runtime/evidence/unit/2026-10-30/20261030T173746-09edf77edc/QA-DATA-QA-DATA.xml sha256=9fee768ffc13d725daea68d363887646efd36d6a9587db99fdf7edb62a3f1a7a

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/pages/pages.test.tsx::화면 > 입력값이 잘못되면 API를 호출하지 않는다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 기본 주소(localhost:8080)로 JSON 요청을 보낸다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 실패 응답은 서버 메시지가 포함된 Error로 던진다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 204 응답은 undefined를 반환한다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-WEB/src/shared/api/client.test.ts::apiRequest > 평가 등록은 POST 한 번으로 id를 받는다
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 UI/API 클라이언트 TC 회귀
- test_type: unit
- tool_a: Vitest
- command_a: ["npm", "test", "--", "--reporter=default", "--reporter=junit", "--outputFile=../qa/.runtime/20261030T174647-e942dbd875/web.xml"]
- result_a: PASS
- tool_b: TypeScript
- command_b: ["npm", "run", "typecheck"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: web-vite/src/pages/pages.test.tsx, web-vite/src/shared/api/client.test.ts
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-a.log sha256=fa9dad15fef20d57de7180358367686c84f38bca6c7b8075090fb664cb55c836; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-web.xml sha256=bd7263116b175708365ea072d3ccbc821fdb5ccc3f9e81ee039fa03398e00ecf; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-WEB-b.log sha256=82c1e49d2fbf11cc5f81154c4f13c8823f697a17ee8e5fe41b20ef63309fd691

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Vitest는 동작, TypeScript는 정적 타입. 타입 검사는 동작 재실행을 대체하지 않음.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-DATA
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-DATA
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-b.log sha256=bf22e88f0e3a0e89eddb09d252b1661a48c9dfc4bd5aa177b5efca41f2700a18; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-QA-DATA.xml sha256=a76b071336b31b582d2481d716fa782d8081163468f7fc446fec8938aa727b46

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_duplicate_removed
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-b.log sha256=bf22e88f0e3a0e89eddb09d252b1661a48c9dfc4bd5aa177b5efca41f2700a18; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-QA-DATA.xml sha256=a76b071336b31b582d2481d716fa782d8081163468f7fc446fec8938aa727b46

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_json_parsing
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-b.log sha256=bf22e88f0e3a0e89eddb09d252b1661a48c9dfc4bd5aa177b5efca41f2700a18; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-QA-DATA.xml sha256=a76b071336b31b582d2481d716fa782d8081163468f7fc446fec8938aa727b46

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-DATA/data.tests.test_transform.TestTransform::test_parse_xml
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: JSON/XML 변환 및 중복 제거
- test_type: unit
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "data/tests", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-DATA.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/tests/test_transform.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-a.log sha256=7f8b68b10f0b6fb1b16dd5fd0efb46457e4b260e25b06c15b398b11434871908; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-b.log sha256=bf22e88f0e3a0e89eddb09d252b1661a48c9dfc4bd5aa177b5efca41f2700a18; qa/.runtime/evidence/unit/2026-10-30/20261030T174647-e942dbd875/QA-DATA-QA-DATA.xml sha256=a76b071336b31b582d2481d716fa782d8081163468f7fc446fec8938aa727b46

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 동일 기존 TC를 서로 다른 발견/실행 엔진으로 검증; 독립적인 요구사항 oracle은 아님.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

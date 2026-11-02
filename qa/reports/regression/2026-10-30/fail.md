# FAIL

## 20261030T172933-71ba9d567c / QA-CONFIG
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: FAIL
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T172933-71ba9d567c/QA-CONFIG-a.log sha256=28de98ca66dc5b73ea67b94d984a028b4a766f2bee8ac7424c4f3add1d431211; qa/.runtime/evidence/regression/2026-10-30/20261030T172933-71ba9d567c/QA-CONFIG-b.log sha256=2f0a3cd8a2e84a3aeb847c77c4b9b0fc94be5a220d1d8a27aed1667adc714542

Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

### QA-CONFIG / 20261030T172933-71ba9d567c 원인 분석 (수정 전)
- 입력/재현: actionlint .github/workflows/githubactions.yml .github/workflows/deploy.yml
- 오류: SC2034 i appears unused. 실제 위치: .github/workflows/deploy.yml:115, jobs.deploy.steps[Wait for deployment result].run.
- 기대: 워크플로/셸 정적 검사 PASS. 실제: 미사용 반복 변수로 실패. 수정 계획: 반복 변수를 _로 변경하여 대기 동작 유지.
- ISSUE_ID: QA-CI-001. 별도 실제 셸 오류 주입 테스트 2개는 PASS. 재검증은 수정 후 QA-CONFIG 및 전체 회귀로 수행.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:15 KST)

- **실패/미통과 건수**: 1건 / 전체 2건

### [REG-002] 운영/로컬 DB 기준 데이터(기본 직무 8건 및 기존 평가 id=2) 비파괴 무결성 회귀 검증 (`FAIL`) — `-`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:33:10 KST`
- **테스트 종류**: `regression`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (GET /api/assessments/summary)` → **PASS (totalCount=2, analyzedCount=1)**
- **도구 B 및 결과**: `psql Direct Invariant Query (assessment id=2 & job count)` → **FAIL (assessment_2='', jobs=8)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/job/JobDataInitializer.java` / 함수 `JobDataInitializer` / 줄 번호 `1-50`
- **입력값 (Input)**: `자동화 QA 실행 전후에 기존 DB 데이터(id=2 평가 및 8개 직무)가 오염되거나 삭제되지 않았음을 보장`
- **오류 메시지 / 응답**: `totalCount=2, id=2 상태='', 직무 수=8`
- **예상 결과 (Expected)**: totalCount=1, assessment id=2 AI_COMPLETED 유지, job count=8
- **실제 결과 (Actual)**: totalCount=2, id=2 상태='', 직무 수=8
- **재현 방법 (Reproduction)**:
  ```zsh
  GET /api/assessments/summary & psql
  ```
- **원인 분석 (Root Cause)**: 
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)


## 20261030T173710-26efa742be / QA-REGRESSION
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: FAIL
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173710-26efa742be / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173710-26efa742be/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-a.log sha256=0eaa3c96c6c036e15080d49197a8cca07d695b788cb6b8f00b7829735cb40e4e; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-b.log sha256=0b13b5cf297e820f505fb9b6a5a3c89085e04148ae28d643600d0e38a98904e9; qa/.runtime/evidence/regression/2026-10-30/20261030T173710-26efa742be/QA-REGRESSION-QA-REGRESSION.xml sha256=83ed24d53beb38b145ea3260e27db79e7f4ab72cf39892e8b723b5a50a78cdf0

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

### HISTORY-NORMALIZE-001 / 2026-10-30T17:37+09:00
- 도구: python3 scripts/qa/normalize_history.py. Git HEAD: 9491fb1b (dirty).
- 기대: 과거 바이트를 보존하고 모든 기존 TSV 스키마를 정규화. 실제: 혼합 스키마 5개는 원본 SHA256 보존 후 복구; 순수 legacy 헤더인 E2E/performance에서는 ValueError: Unexpected header로 중단.
- 위치: scripts/qa/normalize_history.py:19, normalize. 원인: 순수 legacy 헤더 처리 분기 누락. 수정 전 기록/보고 후 해당 헤더도 명시적으로 처리한다. 알려지지 않은 헤더는 계속 차단한다.

## 20261030T173728-084ab85c8a / QA-REGRESSION
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: FAIL
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: FAIL
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173728-084ab85c8a / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: FAIL
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173728-084ab85c8a/QA-REGRESSION.xml"]
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-a.log sha256=7bbc5694c3715319b14d52809dff2a8308c0583f20a3aef20a1e28d0b464ce3a; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-b.log sha256=eaec6cff32a183ab40282b5a78b689b3f7ccd595f178f39ae3314c250f42f6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173728-084ab85c8a/QA-REGRESSION-QA-REGRESSION.xml sha256=c613673fc1ccac2bab8c4c5d4ccc29e86a803a761bfdb4763ae74a8e0e725dcc

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/FAIL
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

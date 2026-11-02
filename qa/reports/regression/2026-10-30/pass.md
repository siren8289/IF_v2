# PASS

## 20261030T172455-160ef4c9a6 / QA-REGRESSION
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T172455-160ef4c9a6/QA-REGRESSION-a.log sha256=3bafd3c7cdc41052c99d64ead69424a5a3535cf13efb01eea18054ebf9bbf7e4; qa/.runtime/evidence/regression/2026-10-30/20261030T172455-160ef4c9a6/QA-REGRESSION-b.log sha256=452fada82e1df58d7f89fa99128aea691c519ad7daf4915a4bece62bd06ecbdf

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173027-a0890b20ec/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-a.log sha256=b858937e4a249123817311b4ade86ff663329fdece7ef37ede5b7253ea31b771; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-b.log sha256=8205f965257fdf54d45a3ab54560950b0388599ccedf75deeb3d3ce88f9bf6e1; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-REGRESSION-QA-REGRESSION.xml sha256=103d245369025fad7c53d20de5fe8c0d60be91ea4d1c150ca0f8b3ce9b6b0579

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-CONFIG
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T173027-a0890b20ec/QA-CONFIG-b.log sha256=33d23a5b222677eaccb42f0b7439bcbf5cad3d7f9ad765238d9599a046e8cab8

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173203-e98ac2d793/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-a.log sha256=245559cd015868d2d05e6f4309597424a66ff84a8ec0949bad8d80bfdef58f2d; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-b.log sha256=6f82ef266ce900a23d235710cf6f2bbaca30bf16812624e9eceae75322a6dedf; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-REGRESSION-QA-REGRESSION.xml sha256=e3345e873e396ffd5b3faab28418916c1539fcc91d93e2cc6d8f50d64049c527

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173203-e98ac2d793 / QA-CONFIG
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T173203-e98ac2d793/QA-CONFIG-b.log sha256=ca4fa1bb98e25de887114ed598ac5d90fef4a199671feaadbfba8569eed3d973

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:15 KST)

- **통과 건수**: 1건 / 전체 2건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `REG-001` | 2026-10-30 17:33:10 KST | 멀티모듈(Data ETL, Web-Vite Vitest/TSC, AI Score) 기본 회귀 스위트 일괄 검증 | `Multi-Module Test Runner (unittest + vitest)` (PASS (data_rc=0, vitest_rc=0)) | `Static Type & Formula Invariant Verifier (tsc --noEmit + risk_score)` (PASS (tsc_rc=0)) | **PASS** | `9491fb1b` | `web-vite/package.json` | `test, typecheck` | `6-13` | `-` | **목적**: 기존 통과하던 모듈별 자동화 테스트가 코드·환경 변경 후에도 깨지지 않았는지 회귀 검증<br>**기대**: 모든 모듈 테스트 및 타입 검사 종료 코드 0<br>**실제/근거**: data_rc=0, vitest_rc=0, tsc_rc=0 (data/tests/test_transform.py & web-vite/src/pages/pages.test.tsx) |


## 20261030T173420-dd42c9f7f7 / QA-REGRESSION
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173420-dd42c9f7f7/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-a.log sha256=f02dda5264985524a9d073da77bb204a223aea4fb22c908bd4a6a2029257fd65; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-b.log sha256=e116dd6e7837d34c3d45838b8e878a860c32a40fa817c782ab1cc87f639882af; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-REGRESSION-QA-REGRESSION.xml sha256=05aad5d009b4d8e13dfedcabead45ea6fa3d6b6cf7b5f62fb4adcaacc9530304

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173420-dd42c9f7f7 / QA-CONFIG
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T173420-dd42c9f7f7/QA-CONFIG-b.log sha256=ca5676030b4a8f2d4decb5b45e584d4547a2dc554f25f7bdb826094d5600c0a9

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173746-09edf77edc/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-a.log sha256=75941143e10b8feb430d562a044a34e0f493910a334f21578123948a8a3cb4d0; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-b.log sha256=4abe3af27a4a6e7811fd17e93e5055ed9ba1461574c385dfb624a8d1ec4bd4cb; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-REGRESSION-QA-REGRESSION.xml sha256=d8fee96804a4271eb3297b03757e5e74e8635acc78f0682a08a26873c91d3a8f

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-CONFIG
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T173746-09edf77edc/QA-CONFIG-b.log sha256=c6c718d966ec0fd8ee9e11f4511039b4cf539f93b9cb722e1233e3273557b022

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T173817-5b5ab53906/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-a.log sha256=faef6805493e16a09149993ff4afe69a883430f0779e57052c6aebffdc315a0b; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-b.log sha256=730d9ee57dd24c6396b3acf623278a56a5b744e3d8a10a85bcb34c1a8abed829; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-REGRESSION-QA-REGRESSION.xml sha256=0c5227c70c5a0ce637240da88e12f91e946873e08a21dddeaa789d4077d2dff8

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173817-5b5ab53906 / QA-CONFIG
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T173817-5b5ab53906/QA-CONFIG-b.log sha256=92afcc4ef7539a2506fdb9b7abd235ffe9edde26ee2635a9f47846eb6c5613a0

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_history.HistoryTests::test_both_legacy_and_mixed_formats_preserve_original_bytes
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_append_history_bom_unicode_and_only_requested_kind
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_exit_failure_missing_tool_and_empty_discovery_are_not_pass
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_incompatible_writers_cannot_corrupt_history
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_junit_preserves_failure_error_and_skip
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_timeout_is_error
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unknown_status_rejected
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_runner.RunnerTests::test_unresolved_high_blocks_and_resolution_preserves_history
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_accepts_successful_main_exact_sha
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-REGRESSION/scripts.qa.test_workflows.DeploymentGateTests::test_deployment_blocks_missing_failed_other_sha_and_pr_runs
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA 실행기 실패 차단·누적·상태·한글 검증
- test_type: regression
- tool_a: unittest
- command_a: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_*.py", "-v"]
- result_a: PASS
- tool_b: pytest
- command_b: ["python3", "-m", "pytest", "scripts/qa", "-q", "--junitxml=./qa/.runtime/20261030T174647-e942dbd875/QA-REGRESSION.xml"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: scripts/qa/run.py, scripts/qa/test_runner.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-a.log sha256=b6f4077d012450589fc3e2f831b7fbd606fa8708e0472f06215d6ed4770a98cd; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-b.log sha256=f3ee532ec20515956afea78f936408ac0951a7cbe77a51c73879b210db91d3ef; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-REGRESSION-QA-REGRESSION.xml sha256=bba14b5f33f5f4ef0be8f394374345bd23a4e4593777e2d062417d4a68dcdee7

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: 두 테스트 엔진에서 실행기 계약과 오류 주입 검증.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-CONFIG
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-CONFIG
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: CI 구성 및 실제 배포 셸 게이트 오류 주입
- test_type: regression
- tool_a: actionlint/ShellCheck
- command_a: ["actionlint", ".github/workflows/githubactions.yml", ".github/workflows/deploy.yml"]
- result_a: PASS
- tool_b: unittest deployment simulation
- command_b: ["python3", "-m", "unittest", "discover", "-s", "scripts/qa", "-p", "test_workflows.py", "-v"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml, .github/workflows/githubactions.yml, scripts/qa/test_workflows.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-CONFIG-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/regression/2026-10-30/20261030T174647-e942dbd875/QA-CONFIG-b.log sha256=905baa842a719a3ee6797f93eecf0ae1dfb707b1f559258b55a1ec518f4bab74

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: actionlint/ShellCheck 구문/셸 분석과 실제 gate 셸의 GitHub API 응답 오류 주입. AWS 배포 자체는 미실행.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

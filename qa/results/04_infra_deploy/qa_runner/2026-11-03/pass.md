# PASS

## 20261103T023235-7994cf0a4f / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T023235-7994cf0a4f
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T02:32:35+09:00
- timestamp_end: 2026-11-03T02:32:42+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: QA 실행기 계약 회귀
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T023235-7994cf0a4f/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 1.09s
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: scripts/qa/run.py
- function: main
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023235-7994cf0a4f/unittest.log#2b63f81e9e430f6c;qa/.runtime/20261103T023235-7994cf0a4f/pytest.log#3005dd91d6a745f8

시나리오: QA 실행기 계약 회귀
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:05:28+09:00
- timestamp_end: 2026-11-03T04:05:37+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T034221-c3386f4577/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 1.20s
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/unittest.log#d419733ee360a952;qa/.runtime/20261103T034221-c3386f4577/pytest.log#55802ede70b055a8

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041121-74509b288b / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041121-74509b288b
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:11:49+09:00
- timestamp_end: 2026-11-03T04:12:26+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041121-74509b288b/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.85s
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041121-74509b288b/unittest.log#a93219c8534f4d64;qa/.runtime/20261103T041121-74509b288b/pytest.log#6a4c07f240a7f593

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041346-02eb90aae9 / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041346-02eb90aae9
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:13:47+09:00
- timestamp_end: 2026-11-03T04:13:53+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041346-02eb90aae9/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.38s
- status: PASS
- git_commit: 3862d7fcc723
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041346-02eb90aae9/unittest.log#bfa5e47c56e22e57;qa/.runtime/20261103T041346-02eb90aae9/pytest.log#20c5bbb5985e1481

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041449-77bab4b99f / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041449-77bab4b99f
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:14:49+09:00
- timestamp_end: 2026-11-03T04:14:51+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041449-77bab4b99f/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.09s
- status: PASS
- git_commit: 3862d7fcc723
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041449-77bab4b99f/unittest.log#a802d0fd7c3f8467;qa/.runtime/20261103T041449-77bab4b99f/pytest.log#981e9346d5562190

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041509-98741bddc7 / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041509-98741bddc7
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:15:10+09:00
- timestamp_end: 2026-11-03T04:15:12+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041509-98741bddc7/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.13s
- status: PASS
- git_commit: 3862d7fcc723
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041509-98741bddc7/unittest.log#bfa5e47c56e22e57;qa/.runtime/20261103T041509-98741bddc7/pytest.log#2546cbe25cac6efb

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041532-9952fb2b6b / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041532-9952fb2b6b
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:15:33+09:00
- timestamp_end: 2026-11-03T04:15:41+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041532-9952fb2b6b/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 1.88s
- status: PASS
- git_commit: 3862d7fcc723
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041532-9952fb2b6b/unittest.log#aa50e6d063cb3b6a;qa/.runtime/20261103T041532-9952fb2b6b/pytest.log#3ce2712acd73268c

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041553-7a118e45b0 / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T041553-7a118e45b0
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:15:54+09:00
- timestamp_end: 2026-11-03T04:15:59+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T041553-7a118e45b0/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.18s
- status: PASS
- git_commit: 3862d7fcc723
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041553-7a118e45b0/unittest.log#86632f2af825175f;qa/.runtime/20261103T041553-7a118e45b0/pytest.log#afbe903dd450f06a

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T040956-523c5ec792 / TC-INFRA-RUNNER-001
- RUN_ID: 20261103T040956-523c5ec792
- TC_ID: TC-INFRA-RUNNER-001
- FEATURE_ID: FEAT-QA-RUNNER
- timestamp_start: 2026-11-03T04:16:16+09:00
- timestamp_end: 2026-11-03T04:16:18+09:00
- area: 04_infra_deploy
- section: qa_runner
- scenario: 실행기 계약을 unittest와 pytest로 교차 검증.
- tool_a: unittest
- command_a: python3 -m unittest discover -s scripts/qa -p test_*.py -v
- result_a: PASS
- expected_a: PASS
- actual_a: failed_ci_blocks_deploy) ... ok test_json_roundtrip_fixture (test_workflows.DeployGateTests.test_json_roundtrip_fixture) ... ok test_missing_sha_blocks (test_workflows.DeployGateTests.test_missing_sha_blocks) ... ok test_success_allows_deploy (test_workflows.DeployGateTests.test_success_allows_deplo
- tool_b: pytest
- command_b: python3 -m pytest scripts/qa -q --junitxml=./qa/.runtime/20261103T040956-523c5ec792/TC-INFRA-RUNNER-001-b.xml
- result_b: PASS
- expected_b: PASS
- actual_b: ......... [100%] 9 passed in 0.10s
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T040956-523c5ec792/unittest.log#3006e3b4d7e3b703;qa/.runtime/20261103T040956-523c5ec792/pytest.log#52e49ed99f2b1e76

시나리오: 실행기 계약을 unittest와 pytest로 교차 검증.
비교: 실행기 계약을 unittest와 pytest로 교차 검증.
1차: unittest 기대=PASS 실제=PASS
2차: pytest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

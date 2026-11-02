# PASS

## 20261103T023235-7994cf0a4f / TC-UNIT-DATA-001
- RUN_ID: 20261103T023235-7994cf0a4f
- TC_ID: TC-UNIT-DATA-001
- FEATURE_ID: FEAT-DATA-ETL
- timestamp_start: 2026-11-03T02:32:58+09:00
- timestamp_end: 2026-11-03T02:33:40+09:00
- area: 01_unit_integration
- section: data_etl
- scenario: JSON/XML 변환·중복 제거 경계
- tool_a: pytest
- command_a: python3 -m pytest data/tests -q --junitxml=./qa/.runtime/20261103T023235-7994cf0a4f/TC-UNIT-DATA-001-a.xml
- result_a: PASS
- expected_a: PASS
- actual_a: ... [100%] 3 passed in 0.71s
- tool_b: unittest
- command_b: python3 -m unittest discover -s data/tests -v
- result_b: PASS
- expected_b: PASS
- actual_b: test_duplicate_removed (test_transform.TestTransform.test_duplicate_removed) ... ok test_json_parsing (test_transform.TestTransform.test_json_parsing) ... ok test_parse_xml (test_transform.TestTransform.test_parse_xml) ... ok ---------------------------------------------------------------------- Ra
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: data/etl/transform.py
- function: parse_data
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023235-7994cf0a4f/pytest.log#ce9540832f1f6ec1;qa/.runtime/20261103T023235-7994cf0a4f/unittest.log#d920432624414db1

시나리오: JSON/XML 변환·중복 제거 경계
비교: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
1차: pytest 기대=PASS 실제=PASS
2차: unittest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-UNIT-DATA-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-UNIT-DATA-001
- FEATURE_ID: FEAT-DATA-ETL
- timestamp_start: 2026-11-03T03:42:29+09:00
- timestamp_end: 2026-11-03T03:42:38+09:00
- area: 01_unit_integration
- section: data_etl
- scenario: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
- tool_a: pytest
- command_a: python3 -m pytest data/tests -q --junitxml=./qa/.runtime/20261103T034221-c3386f4577/TC-UNIT-DATA-001-a.xml
- result_a: PASS
- expected_a: PASS
- actual_a: ... [100%] 3 passed in 0.54s
- tool_b: unittest
- command_b: python3 -m unittest discover -s data/tests -v
- result_b: PASS
- expected_b: PASS
- actual_b: test_duplicate_removed (test_transform.TestTransform.test_duplicate_removed) ... ok test_json_parsing (test_transform.TestTransform.test_json_parsing) ... ok test_parse_xml (test_transform.TestTransform.test_parse_xml) ... ok ---------------------------------------------------------------------- Ra
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/pytest.log#7f316e888f8a7571;qa/.runtime/20261103T034221-c3386f4577/unittest.log#d920432624414db1

시나리오: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
비교: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
1차: pytest 기대=PASS 실제=PASS
2차: unittest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T040956-523c5ec792 / TC-UNIT-DATA-001
- RUN_ID: 20261103T040956-523c5ec792
- TC_ID: TC-UNIT-DATA-001
- FEATURE_ID: FEAT-DATA-ETL
- timestamp_start: 2026-11-03T04:09:59+09:00
- timestamp_end: 2026-11-03T04:10:08+09:00
- area: 01_unit_integration
- section: data_etl
- scenario: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
- tool_a: pytest
- command_a: python3 -m pytest data/tests -q --junitxml=./qa/.runtime/20261103T040956-523c5ec792/TC-UNIT-DATA-001-a.xml
- result_a: PASS
- expected_a: PASS
- actual_a: ... [100%] 3 passed in 0.12s
- tool_b: unittest
- command_b: python3 -m unittest discover -s data/tests -v
- result_b: PASS
- expected_b: PASS
- actual_b: test_duplicate_removed (test_transform.TestTransform.test_duplicate_removed) ... ok test_json_parsing (test_transform.TestTransform.test_json_parsing) ... ok test_parse_xml (test_transform.TestTransform.test_parse_xml) ... ok ---------------------------------------------------------------------- Ra
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T040956-523c5ec792/pytest.log#c9a29c02af39f381;qa/.runtime/20261103T040956-523c5ec792/unittest.log#6569a6517ad35201

시나리오: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
비교: 동일 ETL TC를 pytest와 unittest 엔진으로 교차 실행. DB Testcontainers 비적용(순수 변환 로직).
1차: pytest 기대=PASS 실제=PASS
2차: unittest 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

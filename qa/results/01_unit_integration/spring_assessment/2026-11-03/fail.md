# FAIL

## 20261103T023608-84ddceb76c / TC-UNIT-SPRING-001
- RUN_ID: 20261103T023608-84ddceb76c
- TC_ID: TC-UNIT-SPRING-001
- FEATURE_ID: FEAT-SPRING-ASSESS
- timestamp_start: 2026-11-03T02:38:56+09:00
- timestamp_end: 2026-11-03T02:55:23+09:00
- area: 01_unit_integration
- section: spring_assessment
- scenario: 평가 Controller/Service 회귀
- tool_a: JUnit
- command_a: ./gradlew test --rerun-tasks --console=plain
- result_a: FAIL
- expected_a: PASS
- actual_a: umentation. 5 actionable tasks: 5 executed OpenJDK 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended 65 tests completed, 1 failed FAILURE: Build failed with an exception. * What went wrong: Execution failed for task ':test'.
- tool_b: http_blackbox
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8080 --path /api/jobs
- result_b: FAIL
- expected_b: PASS
- actual_b: BLOCKED connection to http://127.0.0.1:8080/api/jobs: timed out
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/java/com/example/demo/assessment
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-V30-001
- evidence: qa/.runtime/20261103T023608-84ddceb76c/JUnit.log#cd280ed4eb68c44b;qa/.runtime/20261103T023608-84ddceb76c/http_blackbox.log#8f7df6d71795cf4d

RISK RISK-V30-001
시나리오: 평가 Controller/Service 회귀
비교: JUnit 단위/슬라이스 + 독립 HTTP 블랙박스. Testcontainers 미도입(RISK-V30-001).
1차: JUnit 기대=PASS 실제=FAIL
2차: http_blackbox 기대=PASS 실제=FAIL
최종=FAIL. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-UNIT-SPRING-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-UNIT-SPRING-001
- FEATURE_ID: FEAT-SPRING-ASSESS
- timestamp_start: 2026-11-03T03:42:39+09:00
- timestamp_end: 2026-11-03T03:56:18+09:00
- area: 01_unit_integration
- section: spring_assessment
- scenario: JUnit 단위/슬라이스 + 독립 HTTP 블랙박스. Testcontainers 미도입(RISK-V30-001).
- tool_a: JUnit
- command_a: ./gradlew test --rerun-tasks --console=plain
- result_a: FAIL
- expected_a: PASS
- actual_a: umentation. 5 actionable tasks: 5 executed OpenJDK 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended 65 tests completed, 5 failed FAILURE: Build failed with an exception. * What went wrong: Execution failed for task ':test'.
- tool_b: http_blackbox
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8080 --path /api/jobs
- result_b: FAIL
- expected_b: PASS
- actual_b: BLOCKED connection to http://127.0.0.1:8080/api/jobs: timed out
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-V30-001
- evidence: qa/.runtime/20261103T034221-c3386f4577/JUnit.log#41ff8290f192f030;qa/.runtime/20261103T034221-c3386f4577/http_blackbox.log#8f7df6d71795cf4d

RISK RISK-V30-001
시나리오: JUnit 단위/슬라이스 + 독립 HTTP 블랙박스. Testcontainers 미도입(RISK-V30-001).
비교: JUnit 단위/슬라이스 + 독립 HTTP 블랙박스. Testcontainers 미도입(RISK-V30-001).
1차: JUnit 기대=PASS 실제=FAIL
2차: http_blackbox 기대=PASS 실제=FAIL
최종=FAIL. 미실행을 PASS로 처리하지 않음.

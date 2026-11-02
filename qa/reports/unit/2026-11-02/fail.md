# FAIL

## RUN-20261102-001 / QA-UNIT-SPRING
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-SPRING
- timestamp: 2026-11-02T11:57:51+09:00
- feature: Spring 평가 컨트롤러/서비스 단위 테스트
- test_type: unit
- tool_a: Gradle JUnit
- command_a: ./gradlew test --rerun-tasks
- result_a: FAIL
- tool_b: JUnit XML
- command_b: spring/build/test-results/test/TEST-*.xml
- result_b: FAIL
- status: FAIL
- git_commit: 69f74c49c8a9
- dirty: true
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java
- function: 나이가_범위를_벗어나면_400
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: gradle=FAIL xml tests=65 failures=1 errors=0 files=TEST-com.example.demo.assessment.AssessmentControllerTest.xml,TEST-com.example.demo.assessment.AssessmentPipelineIf0094Test.xml,TEST-com.example.demo.assessment.AssessmentServiceTest.xml

검증 목적: 기존 AssessmentControllerTest, AssessmentServiceTest가 통과하는지 확인한다.
도구 A는 Gradle 테스트 프로세스다. 도구 B는 그 실행이 남긴 JUnit XML을 따로 읽는다. XML은 두 번째 실행이 아니라 같은 실행의 독립 판독이다.
기대: 두 판독 모두 실패 0, 테스트 1건 이상. 실제: A=FAIL B=FAIL tests=65 failures=1 errors=0.
범위: H2와 Mock AI. 운영 PostgreSQL과 살아있는 FastAPI는 포함하지 않는다.
로그 끝:
11-02T11:58:01.793+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-2 - Shutdown initiated...
2026-11-02T11:58:01.794+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-2 - Shutdown completed.
2026-11-02T11:58:01.795+09:00  INFO 76243 --- [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2026-11-02T11:58:01.795+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-3 - Shutdown initiated...
2026-11-02T11:58:01.796+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-3 - Shutdown completed.

> Task :test FAILED

65 tests completed, 1 failed

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':test'.
> There were failing tests. See the report at: file:///Users/jeong-yelim/orca/IF_v2/spring/build/reports/tests/test/index.html

* Try:
> Run with --scan to get full insights.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.9/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 9s
5 actionable tasks: 5 executed

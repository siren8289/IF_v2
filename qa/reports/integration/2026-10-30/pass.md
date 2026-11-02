# PASS

## 20261030T172455-160ef4c9a6 / QA-SPRING
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-SPRING
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T172455-160ef4c9a6/QA-SPRING-a.log sha256=30114e0985c94ab609f00aa542b05722b4fd72a2ee50b91ac4733f2593502ec6; qa/.runtime/evidence/integration/2026-10-30/20261030T172455-160ef4c9a6/QA-SPRING-b.log sha256=62b000928e2621c8b23558a5192263f11f622291513dbad03db83045189e8ea2

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-a.log sha256=7f188c202e7c42fd0b27ea64d2ccf8763cb072c94d75c2ba6d78268635024295; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=c636e11b22bec5edd1819235b9651de0e9ff84413647fe7441434dd7ad35cd47; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=200715a819bd55426913a829030503be6b9ab4fcc0fcbb2531ea9792dcd44391; qa/.runtime/evidence/integration/2026-10-30/20261030T173027-a0890b20ec/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:53 KST)

- **통과 건수**: 0건 / 전체 2건

> 해당 실행(`RUN_ID`)에서 통과한 TC가 없습니다.


## 20261030T173746-09edf77edc / QA-SPRING
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-a.log sha256=dfc57d3ca3747e025291de60624257409f68a23060d97fbefed49f5977e63849; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=009e51fba9ce06e6e84c7bf1d89f451c6482ff3b216a6d009fb66b8847cb1e80; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=09b890de6232b04cf7deefe2ab3d336c2a93f1a0ad0aaa12de09ec09a74735d8; qa/.runtime/evidence/integration/2026-10-30/20261030T173746-09edf77edc/QA-SPRING-b.log sha256=b67670a84a3d8059be123dc1e850e3bb8a8f7374ce6b9191c872d10ac8453520

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::요약과_목록을_조회할_수_있다()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::나이가_범위를_벗어나면_400()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentControllerTest::없는_평가를_조회하면_404()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::AI_점수가_범위를_벗어나면_오류가_난다()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_등록하면_AI_결과가_저장된다()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SPRING/com.example.demo.assessment.AssessmentServiceTest::평가를_삭제할_수_있다()
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 기존 Controller/Service TC 회귀
- test_type: integration
- tool_a: JUnit/Gradle
- command_a: ["./gradlew", "test", "--rerun-tasks", "--console=plain"]
- result_a: PASS
- tool_b: javac/Gradle
- command_b: ["./gradlew", "classes", "--rerun-tasks", "--console=plain"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java, spring/src/test/java/com/example/demo/assessment/AssessmentServiceTest.java
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-a.log sha256=bc425889a84c9a5ccdab4962a49198fe10e808f9a4d1c448cd4abe44bc40a1cf; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentControllerTest.xml sha256=7572be626d454871019ea5ea8ccf8ff2e889f23d3b87453d1f5126724e2cf99e; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-TEST-com.example.demo.assessment.AssessmentServiceTest.xml sha256=9225160c8f5fc66837b2ccac738709addef2a013f8c53d8e089dcd863a70c707; qa/.runtime/evidence/integration/2026-10-30/20261030T174647-e942dbd875/QA-SPRING-b.log sha256=4b036a9d61da80778f5f5edb9dc6835305f161444a049cc93d9784fe1a2fcf5d

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: JUnit 컨트롤러/서비스 동작 및 javac 컴파일 검증. 실 DB/운영 통합 검증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## TC-20261030-1645 / LOG-001
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-001
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 정상 평가 처리 순서
- test_type: integration
- tool_a: API/코드/DB
- command_a: 정상 등록→Spring 로그·DB·결과 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 81–82행 직무 조회, 86–99행 저장과 PENDING_AI, 109행 AI 호출, 115–126행 결과 저장
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 직무 검증→개인정보 저장→AI 호출→결과 저장 | 실제: 직무 999999는 HTTP 404, 네 테이블 증가 0. 목 서버가 3초 지연하는 동안 평가 80은 PENDING_AI이고 AI 결과 행이 없었다. 응답 뒤 HTTP 201, AI_COMPLETED, 점수 42 MID. 순서는 직무 검증, 신청자·건강·평가 저장, AI 호출, 결과 저장이다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-002
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-002
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 작업 ID 연결
- test_type: integration
- tool_a: API/코드/DB
- command_a: 등록 데이터 jobId와 결과 조회 비교
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 93–94행 setJob. 결과 조회는 206행 getJobTitle
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 올바른 직무에 연결 | 실제: jobId 1은 DB job_id 1, 결과 직무명 아파트 야간 경비원. jobId 2는 택배 배송 기사. 결과 조회와 DB가 같다. 둘 다 HTTP 201, AI_COMPLETED. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-003
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-003
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 만성질환 저장
- test_type: integration
- tool_a: API/코드/DB
- command_a: 같은 입력에서 질환값만 다르게 등록
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 89–90행 HealthSnapshot 저장
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: true/false 일관 저장 | 실제: chronicDisease true는 health_snapshot.chronic_disease_flag가 t, false는 f. 둘 다 HTTP 201, AI_COMPLETED. psql은 boolean을 t/f로 보여 준다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-004
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-004
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 이름 trim 저장
- test_type: integration
- tool_a: API/코드/DB
- command_a: 공백 포함 이름 등록 후 DB 조회
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 87행 applicantName().trim()
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 앞뒤 공백 정규화 | 실제: 입력 ' LOG004 '의 저장 display_name은 LOG004. 공백이 붙은 이름은 조회되지 않았다. HTTP 201. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-005
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-005
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 평가 상태 시작
- test_type: integration
- tool_a: API/코드/DB
- command_a: AI 호출 직전 상태 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 97–99행 setStatus(PENDING_AI) 후 save
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: PENDING_AI 상태 관찰 가능 여부 확인 | 실제: 지연 요청에서 0.193초부터 2.765초까지 상태 PENDING_AI가 보였고 AI 결과 행은 없었다. 3.141초에 AI_COMPLETED가 됐다. 관찰된다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-006
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-006
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 평가 상태 성공
- test_type: integration
- tool_a: API/코드/DB
- command_a: 정상 AI 응답 후 상태 조회
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 125–126행 setStatus(AI_COMPLETED)
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: AI_COMPLETED 상태로 전이 | 실제: 실제 FastAPI 응답. HTTP 201. 상태 AI_COMPLETED, 점수 29, 등급 LOW, model_version SIMPLE_V1. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-007
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-007
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 호출 응답 형식
- test_type: integration
- tool_a: API/코드/DB
- command_a: AI mock의 risk_score/grade 반환
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 132–144행 checkAiResult
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 0..100, LOW/MID/HIGH 검증 | 실제: 목 응답 42와 MID가 그대로 저장됐다. model_version MOCK_LOG. 점수는 0~100, 등급은 LOW/MID/HIGH 안이다. HTTP 201. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-008
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-008
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 점수 음수
- test_type: integration
- tool_a: API/코드/DB
- command_a: mock risk_score=-1
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 137행 score.asInt() < 0
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 AI 결과가 성공 결과로 저장되지 않음 | 실제: HTTP 502 AI_ERROR. 문장 'AI 점수가 0~100 범위가 아닙니다.' AI 결과 증가 0. 상태는 PENDING_AI. 점수 -1은 저장되지 않았다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-009
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-009
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 점수 101
- test_type: integration
- tool_a: API/코드/DB
- command_a: mock risk_score=101
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 137행 score.asInt() > 100
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 AI 결과 거절 | 실제: HTTP 502 AI_ERROR. 문장은 점수 범위 오류. AI 결과 증가 0. 상태 PENDING_AI. 101은 저장되지 않았다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-010
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-010
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 등급 알 수 없는 값
- test_type: integration
- tool_a: API/코드/DB
- command_a: mock risk_grade=UNKNOWN
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 140–142행 LOW/MID/HIGH 비교
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 AI 결과 거절 | 실제: HTTP 502 AI_ERROR. 문장 'AI 등급 값이 올바르지 않습니다.' 등급 UNKNOWN은 저장되지 않았다. 상태 PENDING_AI. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-011
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-011
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 서버 연결 실패
- test_type: integration
- tool_a: API/코드/DB
- command_a: 테스트 환경에서 FastAPI 중단 후 평가
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/ai/client/AIClient.java
- function: UNKNOWN
- line: 39–40행 RestClientException을 502로 변환. 연결 제한은 AppConfig.java 21행 3초
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 정의된 실패 정책 확인, 데이터 정합성 점검 | 실제: FastAPI 중지 후 HTTP 502, 3.309초. errorCode AI_ERROR, 문장 'AI 서버 호출에 실패했습니다.' 평가·신청자·건강 +1, AI 결과 +0, 상태 PENDING_AI. 신청자·직무·건강 연결은 유지됐다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-012
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-012
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 응답 지연
- test_type: integration
- tool_a: API/코드/DB
- command_a: 테스트 환경에서 AI mock 지연
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/global/config/AppConfig.java
- function: UNKNOWN
- line: 22행 setReadTimeout 40초. 502 변환은 AIClient.java 39–40행
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 타임아웃/사용자 오류 정책 확인 | 실제: 목 서버가 50초를 기다릴 때 HTTP 502가 40.099초에 왔다. 문장 'AI 서버 호출에 실패했습니다.' 상태 PENDING_AI, AI 결과 없음. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-013
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-013
- timestamp: 2026-10-30T16:45:00+09:00
- feature: AI 응답 비어 있음
- test_type: integration
- tool_a: API/코드/DB
- command_a: AI mock 빈 JSON
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 132–138행 checkAiResult
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 처리 및 상태/DB 정합성 확인 | 실제: 목 응답 {}. HTTP 502, 문장 'AI 점수가 0~100 범위가 아닙니다.' 빈 객체는 null이 아니라서 134행이 아니라 137행이다. 상태 PENDING_AI, AI 결과 없음, 신청자·건강은 남음. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-014
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-014
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 부분 저장 정합성
- test_type: integration
- tool_a: API/코드/DB
- command_a: AI 실패 후 평가/신청자/스냅샷 테이블 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 45–46행, 77행. 저장과 AI 호출은 한 트랜잭션이 아님
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 고아 데이터나 미완료 상태가 운영 요구사항과 일치 | 실제: LOG-011과 LOG-013 모두 평가 PENDING_AI, 신청자와 건강 행은 있고 AI 결과는 없다. 관계 키는 깨지지 않았다. 이 잔존이 서비스에 적힌 정책이다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-015
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-015
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 동일 요청 동시 처리
- test_type: integration
- tool_a: API/코드/DB
- command_a: 격리된 환경에서 같은 입력 병렬 전송
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 79–128행 createAndAnalyze. 이름 유일 제약은 없음
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 중복 정책과 일관된 관계 데이터 | 실제: 같은 본문 두 건을 동시에 보냈다. 둘 다 HTTP 201. 평가 76·77은 각자 신청자, 건강, AI 결과를 가지고 직무 1, AI_COMPLETED, 점수 29였다. 번호를 서로 섞지 않았다. 중복을 거절하는 분기는 없다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-016
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-016
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 삭제 관계 정합성
- test_type: integration
- tool_a: API/코드/DB
- command_a: 테스트 평가 삭제 전후 연결 행 비교
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 216–227행 delete. 평가와 AI 결과만 삭제
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 연관 데이터 처리 정책 충족 | 실제: 평가 73 삭제 HTTP 204. assessment와 ai_risk_result는 없어졌고 신청자 73과 건강 73은 남았다. 삭제 메서드가 지우는 범위와 같다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-017
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-017
- timestamp: 2026-10-30T16:45:00+09:00
- feature: DB 외부 입력 무결성
- test_type: integration
- tool_a: API/코드/DB
- command_a: UI 우회 API 악성 입력 전달
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/service/AssessmentService.java
- function: UNKNOWN
- line: 81행 직무 조회와 86행 저장은 파라미터 바인딩. 나이 상한은 AssessmentCreateRequest.java 16행
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: DB 제약/서버 검증에 의해 일관성 유지 | 실제: 이름 '; DROP TABLE assessment;--' 는 HTTP 201, 그 문자 그대로 저장. assessment 테이블과 평가 id 2는 남았다. script 태그 이름도 201로 문자 저장. 나이 999는 400 VALIDATION_ERROR. jobId 문자열 '1 OR 1=1'은 400 INVALID_JSON. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1645 / LOG-018
- RUN_ID: TC-20261030-1645
- TC_ID: LOG-018
- timestamp: 2026-10-30T16:45:00+09:00
- feature: 로그 예외 원인
- test_type: integration
- tool_a: API/코드/DB
- command_a: 실패 후 spring 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/global/exception/GlobalExceptionHandler.java
- function: UNKNOWN
- line: 29행 log.error. 원인은 AIClient.java 40행이 넘긴 예외
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 해당 요청과 예외 원인 추적 가능 | 실제: 로그 2026-10-30T07:45:40.139Z. 문장 'API error: AI 서버 호출에 실패했습니다.' Caused by ResourceAccessException, 이어서 SocketTimeoutException: Connect timed out. 주소는 http://fastapi:8000/api/v1/risk/analyze. LOG-011 시각과 맞다. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.


# 수동 시트 원문 TC-20261030-1645

# LOG-001 ~ LOG-018 로직 테스트 결과

실행일: 2026-10-30 16:45~16:46 (KST)
대상: `http://localhost:8080` 의 Spring과 `if-app-stack-postgres-1`. 점수·지연 케이스는 같은 Docker 네트워크의 `fastapi` 별칭에 붙인 목 서버를 썼다.
판정: **18건 통과, 0건 실패**

원본 응답은 `results.json`, 표는 `LOG-001-018-결과표.tsv`, 엑셀은 `LOG-001-018-결과.xlsx` 다. 각 행의 실행일은 2026-10-30이다. 통과 건의 버그 번호는 없다.

기대 문장은 시트에 적힌 문장이다. 정책이 코드 주석에만 있는 경우 그 문장을 기준으로 봤다. 저장 후 AI가 실패하면 평가가 `PENDING_AI`로 남고 신청자·건강 행이 지워지지 않는 것이 그 정책이다.

## 결과

| 케이스 ID | 실행일 | 실행 상태 | 실제 결과 | 버그 번호 | 확인한 파일 | 확인한 위치 |
|---|---|---|---|---|---|---|
| LOG-001 | 2026-10-30 | 통과 | 직무 999999는 HTTP 404, 네 테이블 증가 0. 목 서버가 3초 지연하는 동안 평가 80은 PENDING_AI이고 AI 결과 행이 없었다. 응답 뒤 HTTP 201, AI_COMPLETED, 점수 42 MID. 순서는 직무 검증, 신청자·건강·평가 저장, AI 호출, 결과 저장이다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 81–82행 직무 조회, 86–99행 저장과 PENDING_AI, 109행 AI 호출, 115–126행 결과 저장 |
| LOG-002 | 2026-10-30 | 통과 | jobId 1은 DB job_id 1, 결과 직무명 아파트 야간 경비원. jobId 2는 택배 배송 기사. 결과 조회와 DB가 같다. 둘 다 HTTP 201, AI_COMPLETED. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 93–94행 setJob. 결과 조회는 206행 getJobTitle |
| LOG-003 | 2026-10-30 | 통과 | chronicDisease true는 health_snapshot.chronic_disease_flag가 t, false는 f. 둘 다 HTTP 201, AI_COMPLETED. psql은 boolean을 t/f로 보여 준다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 89–90행 HealthSnapshot 저장 |
| LOG-004 | 2026-10-30 | 통과 | 입력 '  LOG004  '의 저장 display_name은 LOG004. 공백이 붙은 이름은 조회되지 않았다. HTTP 201. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 87행 applicantName().trim() |
| LOG-005 | 2026-10-30 | 통과 | 지연 요청에서 0.193초부터 2.765초까지 상태 PENDING_AI가 보였고 AI 결과 행은 없었다. 3.141초에 AI_COMPLETED가 됐다. 관찰된다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 97–99행 setStatus(PENDING_AI) 후 save |
| LOG-006 | 2026-10-30 | 통과 | 실제 FastAPI 응답. HTTP 201. 상태 AI_COMPLETED, 점수 29, 등급 LOW, model_version SIMPLE_V1. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 125–126행 setStatus(AI_COMPLETED) |
| LOG-007 | 2026-10-30 | 통과 | 목 응답 42와 MID가 그대로 저장됐다. model_version MOCK_LOG. 점수는 0~100, 등급은 LOW/MID/HIGH 안이다. HTTP 201. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 132–144행 checkAiResult |
| LOG-008 | 2026-10-30 | 통과 | HTTP 502 AI_ERROR. 문장 'AI 점수가 0~100 범위가 아닙니다.' AI 결과 증가 0. 상태는 PENDING_AI. 점수 -1은 저장되지 않았다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 137행 score.asInt() < 0 |
| LOG-009 | 2026-10-30 | 통과 | HTTP 502 AI_ERROR. 문장은 점수 범위 오류. AI 결과 증가 0. 상태 PENDING_AI. 101은 저장되지 않았다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 137행 score.asInt() > 100 |
| LOG-010 | 2026-10-30 | 통과 | HTTP 502 AI_ERROR. 문장 'AI 등급 값이 올바르지 않습니다.' 등급 UNKNOWN은 저장되지 않았다. 상태 PENDING_AI. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 140–142행 LOW/MID/HIGH 비교 |
| LOG-011 | 2026-10-30 | 통과 | FastAPI 중지 후 HTTP 502, 3.309초. errorCode AI_ERROR, 문장 'AI 서버 호출에 실패했습니다.' 평가·신청자·건강 +1, AI 결과 +0, 상태 PENDING_AI. 신청자·직무·건강 연결은 유지됐다. |  | `spring/src/main/demo/ai/client/AIClient.java` | 39–40행 RestClientException을 502로 변환. 연결 제한은 AppConfig.java 21행 3초 |
| LOG-012 | 2026-10-30 | 통과 | 목 서버가 50초를 기다릴 때 HTTP 502가 40.099초에 왔다. 문장 'AI 서버 호출에 실패했습니다.' 상태 PENDING_AI, AI 결과 없음. |  | `spring/src/main/demo/global/config/AppConfig.java` | 22행 setReadTimeout 40초. 502 변환은 AIClient.java 39–40행 |
| LOG-013 | 2026-10-30 | 통과 | 목 응답 {}. HTTP 502, 문장 'AI 점수가 0~100 범위가 아닙니다.' 빈 객체는 null이 아니라서 134행이 아니라 137행이다. 상태 PENDING_AI, AI 결과 없음, 신청자·건강은 남음. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 132–138행 checkAiResult |
| LOG-014 | 2026-10-30 | 통과 | LOG-011과 LOG-013 모두 평가 PENDING_AI, 신청자와 건강 행은 있고 AI 결과는 없다. 관계 키는 깨지지 않았다. 이 잔존이 서비스에 적힌 정책이다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 45–46행, 77행. 저장과 AI 호출은 한 트랜잭션이 아님 |
| LOG-015 | 2026-10-30 | 통과 | 같은 본문 두 건을 동시에 보냈다. 둘 다 HTTP 201. 평가 76·77은 각자 신청자, 건강, AI 결과를 가지고 직무 1, AI_COMPLETED, 점수 29였다. 번호를 서로 섞지 않았다. 중복을 거절하는 분기는 없다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 79–128행 createAndAnalyze. 이름 유일 제약은 없음 |
| LOG-016 | 2026-10-30 | 통과 | 평가 73 삭제 HTTP 204. assessment와 ai_risk_result는 없어졌고 신청자 73과 건강 73은 남았다. 삭제 메서드가 지우는 범위와 같다. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 216–227행 delete. 평가와 AI 결과만 삭제 |
| LOG-017 | 2026-10-30 | 통과 | 이름 '; DROP TABLE assessment;--' 는 HTTP 201, 그 문자 그대로 저장. assessment 테이블과 평가 id 2는 남았다. script 태그 이름도 201로 문자 저장. 나이 999는 400 VALIDATION_ERROR. jobId 문자열 '1 OR 1=1'은 400 INVALID_JSON. |  | `spring/src/main/demo/assessment/service/AssessmentService.java` | 81행 직무 조회와 86행 저장은 파라미터 바인딩. 나이 상한은 AssessmentCreateRequest.java 16행 |
| LOG-018 | 2026-10-30 | 통과 | 로그 2026-10-30T07:45:40.139Z. 문장 'API error: AI 서버 호출에 실패했습니다.' Caused by ResourceAccessException, 이어서 SocketTimeoutException: Connect timed out. 주소는 http://fastapi:8000/api/v1/risk/analyze. LOG-011 시각과 맞다. |  | `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` | 29행 log.error. 원인은 AIClient.java 40행이 넘긴 예외 |

## 실행 방법

1. 실제 FastAPI로 LOG-002, 003, 004, 006, 015, 016, 017을 보냈다. 기본값은 나이 70, 건강 3, 만성질환 false, 근무 8시간, 직무 1이고 이름만 케이스별로 바꿨다.
2. `if-app-stack-fastapi-1` 을 멈추고 LOG-011을 보냈다. 로그는 LOG-018에서 읽었다.
3. 멈춘 컨테이너를 네트워크에서 떼고, 같은 `fastapi` 별칭으로 목 서버를 띄운 뒤 Spring을 재시작해 DNS가 목을 보게 했다. LOG-001, 005, 007, 008, 009, 010, 012, 013, 014를 여기서 봤다.
4. 목을 지우고 원래 FastAPI를 다시 붙인 뒤 Spring을 재시작했다. `GET /api/jobs` 는 200, FastAPI `/docs` 는 200이었다.
5. 이번 실행으로 만든 평가는 `DELETE /api/assessments/{id}` 로 지웠다. 삭제가 남긴 신청자와 건강 행만 추가로 지웠다. 평가 id 2는 건드리지 않았다.

종료 건수: 평가 1, 신청자 21, 건강 스냅샷 21, AI 결과 1. 평가 id는 2만 남았다. 시작 전과 같다.

## 케이스별 근거

- LOG-001. 없는 직무는 81–82행에서 404이고 그 전에 저장이 없다. 지연 중 DB에 신청자, 건강, PENDING_AI 평가가 먼저 보였고, 응답이 끝난 뒤에야 AI 결과와 AI_COMPLETED가 생겼다.
- LOG-002. 요청 jobId와 assessment.job_id, 결과 화면 jobTitle이 같은 직무를 가리켰다.
- LOG-003. true와 false가 서로 바뀌지 않고 chronic_disease_flag에 저장됐다.
- LOG-004. 앞뒤 공백은 87행 trim 한 번으로 빠진다. Applicant 생성자는 넘어온 문자열을 다시 자르지 않는다.
- LOG-005. AI가 돌아오기 전 상태가 DB에서 읽혔다. 97행에서 PENDING_AI로 저장한 뒤 109행에서 AI를 부른다.
- LOG-006. 실제 분석 응답 뒤 125행에서 AI_COMPLETED로 바뀌었다.
- LOG-007. 목의 42/MID가 검증을 통과해 total_risk_percent, risk_grade에 저장됐다.
- LOG-008과 LOG-009. 137행이 0 미만과 100 초과를 같은 502로 거절한다. 성공 상태와 AI 결과 행은 만들지 않는다.
- LOG-010. 점수는 범위 안이어도 140–142행이 LOW, MID, HIGH가 아닌 등급을 거절한다.
- LOG-011. 연결 제한 3초(AppConfig 21행) 안에 502가 왔다. 원인 예외는 로그의 SocketTimeoutException: Connect timed out 이다.
- LOG-012. 읽기 제한 40초(AppConfig 22행)에 맞춰 40.099초에 502가 왔다. 50초를 끝까지 기다리지 않았다.
- LOG-013. `{}` 는 JsonNode null이 아니다. 134행의 '응답이 비어 있습니다'가 아니라 137행 점수 검사를 탄다. 오류로 처리되고 AI 결과는 없다.
- LOG-014. 실패 뒤 남는 행은 신청자, 건강, PENDING_AI 평가다. 45–46행과 77행이 롤백하지 않는다고 적혀 있고, 이번 DB가 그 문장과 같았다.
- LOG-015. 동시에 보낸 두 요청이 각자 신청자, 건강, 평가, AI 결과를 가졌다. 중복 제거 분기는 없다.
- LOG-016. 216–227행은 AI 결과 연결을 끊고 평가와 AI 결과를 지운다. 신청자와 건강 스냅샷은 삭제 대상이 아니다.
- LOG-017. SQL 조각과 script 태그는 문자열로 저장됐고 테이블은 그대로였다. 범위를 넘는 나이는 400, 숫자가 아닌 jobId는 JSON 변환 400이다.
- LOG-018. 29행이 5xx ApiException을 스택과 함께 남긴다. 40행이 넘긴 원인까지 Caused by로 이어져 LOG-011 요청을 로그에서 찾을 수 있었다.


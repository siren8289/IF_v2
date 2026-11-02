# FAIL

## 20261102T030007-f93e24192e / IF-0098
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0098
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0098 평가 생성 직후 상태
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: FAIL
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: FAIL
- status: FAIL
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 기대 status=PENDING_AI와 assessedAt UTC. assessedAt offset은 UTC로 통과. 조회한 status는 AI_COMPLETED. Assessment 행은 1건 증가.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

재현: 격리 H2에서 jobId=1, 정상 요청, AI mock score 40 grade LOW로 createAndAnalyze를 한 번 호출한 뒤 assessment를 ID로 조회.
원인: AssessmentService.createAndAnalyze 97-99행이 PENDING_AI로 저장하고, 검증을 통과하면 124-126행이 AI_COMPLETED로 덮어 쓴다. 호출이 끝난 뒤의 행은 PENDING_AI가 아니다.
수정: 하지 않음. IF-0120은 같은 성공 경로의 최종 상태를 AI_COMPLETED로 기대하며 통과했다.

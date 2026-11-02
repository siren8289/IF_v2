# PASS

## 20261102T030007-f93e24192e / IF-0094
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0094
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0094 jobId=1 조회 후 평가 생성
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 81
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0095
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0095
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0095 없는 직무
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 81
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0096
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0096
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0096 신청자 이름 trim과 나이
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 87
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0097
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0097
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0097 건강 스냅샷 보존
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 89
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0099
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0099
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0099 AI title은 직무명
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 103
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0100
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0100
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0100 AI age
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 104
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0101
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0101
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0101 AI physical_level
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 105
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0102
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0102
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0102 AI chronic_disease
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0103
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0103
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0103 AI work_hour_limit
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 107
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0104
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0104
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0104 AI 응답 null
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 133
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0105
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0105
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0105 점수 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 136
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0106
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0106
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0106 점수 실수
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0107
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0107
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0107 점수 문자열
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0108
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0108
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0108 점수 -1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0109
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0109
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0109 점수 0
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0110
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0110
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0110 점수 100
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0111
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0111
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0111 점수 101
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 137
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0112
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0112
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0112 등급 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 140
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0113
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0113
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0113 등급 LOW
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 141
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0114
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0114
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0114 등급 MID
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 141
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0115
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0115
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0115 등급 HIGH
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 141
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0116
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0116
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0116 등급 소문자
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 141
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0117
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0117
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0117 등급 UNKNOWN
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: checkAiResult
- line: 141
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0118
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0118
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0118 모델 버전 기본값
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 119
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0119
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0119
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0119 설명 JSON 저장
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 121
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0120
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0120
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0120 상태 완료와 결과 연결
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 124
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0121
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0121
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0121 AI 호출 실패 시 PENDING_AI 잔존
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 109
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0122
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0122
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0122 AI 결과 저장 실패
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: createAndAnalyze
- line: 122
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0123
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0123
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0123 결과 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 169
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0124
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0124
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0124 설명 신형
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 184
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0125
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0125
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0125 설명 구형 summary
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 186
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0126
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0126
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0126 설명 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 186
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0127
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0127
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0127 출처 기본값
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 187
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0128
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0128
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0128 출처 gemini
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 187
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0129
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0129
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0129 요인 신형
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 189
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0130
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0130
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0130 요인 구형
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 190
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0131
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0131
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0131 요인 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 189
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0132
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0132
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0132 작업 신형
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 195
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0133
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0133
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0133 작업 구형
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 195
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0134
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0134
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0134 작업 없음
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 195
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0135
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0135
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0135 깨진 설명 JSON
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: readJson
- line: 234
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0136
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0136
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0136 없는 평가
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: findAssessment
- line: 229
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0137
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0137
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0137 AI 결과 있는 평가 삭제
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: delete
- line: 216
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0138
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0138
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0138 PENDING_AI 삭제
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: delete
- line: 226
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0139
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0139
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0139 없는 ID 삭제
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: findAssessment
- line: 229
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0140
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0140
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0140 같은 ID 두 번 삭제
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: findAssessment
- line: 229
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0141
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0141
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0141 삭제 후 조회
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: getResult
- line: 168
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0142
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0142
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0142 다른 평가는 유지
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: delete
- line: 216
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0143
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0143
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0143 총 평가 0
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 154
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0144
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0144
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0144 총 평가 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 156
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0145
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0145
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0145 미분석 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 158
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0146
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0146
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0146 완료 LOW 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 157
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0147
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0147
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0147 완료 HIGH 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 157
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0148
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0148
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0148 HIGH 2 MID 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: summary
- line: 157
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0149
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0149
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0149 첫 페이지 20
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: list
- line: 148
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0150
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0150
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0150 21건 page 0
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: list
- line: 148
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0151
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0151
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0151 21건 page 1
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: list
- line: 148
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.

## 20261102T030007-f93e24192e / IF-0152
- RUN_ID: 20261102T030007-f93e24192e
- TC_ID: IF-0152
- timestamp: 2026-11-02T03:00:07+09:00
- feature: IF-0152 같은 시각이면 id DESC
- test_type: api
- tool_a: Gradle JUnit
- command_a: ["./gradlew", "test", "--tests", "com.example.demo.assessment.AssessmentPipelineIf0094Test", "--offline"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "spring/src/main/demo/assessment/service/AssessmentService.java"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: spring/src/main/demo/assessment/service/AssessmentService.java, spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java
- function: list
- line: 148
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T030007-f93e24192e/AssessmentPipelineIf0094Test.xml sha256=a3c831855a6772f70729cbdb23b7ddbfc19391f7862cc759d504286aa6976542; qa/.runtime/20261102T030007-f93e24192e/gradle-summary.txt sha256=533998eacd656f04013c42fe5a9a682fe0cc43ad0996f9a4da0e64d1cdba92db; qa/.runtime/20261102T030007-f93e24192e/source-review.txt sha256=5ce3241008bd1a57007fa4a47126c36243239b9866cd23e41ae11baa47d78ba8

Expected/Actual: 시트 기대와 일치.
Scope: 격리 H2 jdbc:h2:mem:if0094. 운영 Postgres와 평가 id 2는 사용하지 않음. 제품 코드는 수정하지 않음.
## 20261102T121443-d28f9cf0f2 / IF-0153
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0153
- timestamp: 2026-11-02T12:14:43+09:00
- feature: title 빈 문자열
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 string_too_short. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0154
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0154
- timestamp: 2026-11-02T12:14:43+09:00
- feature: title 공백
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 직무 제목을 입력하세요. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0155
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0155
- timestamp: 2026-11-02T12:14:43+09:00
- feature: title 운전기사
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 50
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0156
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0156
- timestamp: 2026-11-02T12:14:43+09:00
- feature: title a 79자
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. 시트 셀 길이 79, 300 미만. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0157
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0157
- timestamp: 2026-11-02T12:14:43+09:00
- feature: title a 99자
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. 시트 셀 길이 99, 300 미만. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0158
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0158
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 0
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 greater_than_equal 1. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0159
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0159
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 1
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0160
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0160
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 60
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0161
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0161
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 90
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0162
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0162
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 120
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0163
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0163
- timestamp: 2026-11-02T12:14:43+09:00
- feature: age 121
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 35
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 less_than_equal 120. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0164
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0164
- timestamp: 2026-11-02T12:14:43+09:00
- feature: physical_level 0
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 37
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0165
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0165
- timestamp: 2026-11-02T12:14:43+09:00
- feature: physical_level 1
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 37
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0166
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0166
- timestamp: 2026-11-02T12:14:43+09:00
- feature: physical_level 3
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 37
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0167
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0167
- timestamp: 2026-11-02T12:14:43+09:00
- feature: physical_level 5
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 37
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0168
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0168
- timestamp: 2026-11-02T12:14:43+09:00
- feature: physical_level 6
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 37
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0169
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0169
- timestamp: 2026-11-02T12:14:43+09:00
- feature: chronic_disease true
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 39
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0170
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0170
- timestamp: 2026-11-02T12:14:43+09:00
- feature: chronic_disease false
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 39
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0171
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0171
- timestamp: 2026-11-02T12:14:43+09:00
- feature: chronic_disease abc
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 39
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 bool_parsing. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0172
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0172
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 0
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0173
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0173
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 1
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0174
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0174
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 7
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0175
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0175
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 8
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0176
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0176
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 24
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 200 결과 JSON. DB 클라이언트 없음.

## 20261102T121443-d28f9cf0f2 / IF-0177
- RUN_ID: 20261102T121443-d28f9cf0f2
- TC_ID: IF-0177
- timestamp: 2026-11-02T12:14:43+09:00
- feature: work_hour_limit 25
- test_type: api
- tool_a: pytest TestClient
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_analyze_input_if0153.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/main.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/main.py, ai/tests/test_analyze_input_if0153.py
- function: analyze
- line: 41
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T121443-d28f9cf0f2/if0153-junit.xml sha256=e460796adbdfd0544af717329834b01116347d4078ad99dcc3e20585b1ee0164; qa/.runtime/20261102T121443-d28f9cf0f2/source-review.txt sha256=d988688dd2dfca3b25baa5cf3d8942f0fab4ec49be8e5f94c263723ba7bed7fe; qa/.runtime/20261102T121443-d28f9cf0f2/pytest-summary.txt sha256=1fbf61ce1fe941aef3063c717418c83607da205aab1df96c08e71066052ae37d

Expected/Actual: 스키마 또는 trim 위반은 422, 유효 입력은 결과 JSON. 실제: 422 less_than_equal 24. DB 클라이언트 없음.

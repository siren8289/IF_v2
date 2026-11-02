# FAIL

## 20261103T033035-526c702671 / IF-0094
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0094
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 직무 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 직무 조회
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 직무 조회
기대: Job 저장소에서 정확한 ID 조회
1차=PASS 2차=FAIL 최종=FAIL
입력: jobId=1 존재

## 20261103T033035-526c702671 / IF-0095
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0095
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 직무 미존재
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 직무 미존재
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 직무 미존재
기대: ApiException.notFound
1차=PASS 2차=FAIL 최종=FAIL
입력: jobId=999999

## 20261103T033035-526c702671 / IF-0096
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0096
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: Applicant 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: Applicant 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Applicant 저장
기대: displayName은 trim된 이름, age 원본 숫자
1차=PASS 2차=FAIL 최종=FAIL
입력: 정상 요청

## 20261103T033035-526c702671 / IF-0097
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0097
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: HealthSnapshot 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: HealthSnapshot 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: HealthSnapshot 저장
기대: physicalLevel/chronicDisease/workHourLimit 보존
1차=PASS 2차=FAIL 최종=FAIL
입력: 만성질환=true, 시간=6

## 20261103T033035-526c702671 / IF-0098
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0098
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 평가 생성
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 평가 생성
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 평가 생성
기대: status=PENDING_AI; assessedAt UTC
1차=FAIL 2차=FAIL 최종=FAIL
입력: 정상 입력

## 20261103T033035-526c702671 / IF-0099
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0099
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 title
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 title
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 전송 title
기대: title에 jobTitle 전송
1차=PASS 2차=FAIL 최종=FAIL
입력: 직무명=아파트 야간 경비원

## 20261103T033035-526c702671 / IF-0100
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0100
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 age
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 age
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 전송 age
기대: age=72 그대로 전송
1차=PASS 2차=FAIL 최종=FAIL
입력: age=72

## 20261103T033035-526c702671 / IF-0101
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0101
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 physical_level
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 physical_level
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 전송 physical_level
기대: physical_level=3 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: physicalLevel=3

## 20261103T033035-526c702671 / IF-0102
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0102
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 chronic_disease
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 chronic_disease
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 전송 chronic_disease
기대: boolean true 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: chronicDisease=true

## 20261103T033035-526c702671 / IF-0103
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0103
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:47+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 work_hour_limit
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 work_hour_limit
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 전송 work_hour_limit
기대: work_hour_limit=6 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: workHourLimit=6

## 20261103T033035-526c702671 / IF-0104
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0104
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:48+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 응답 null
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 응답 null
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 응답 null
기대: ApiException.aiError
1차=PASS 2차=FAIL 최종=FAIL
입력: AI mock null

## 20261103T033035-526c702671 / IF-0105
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0105
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 없음
기대: 점수 검증 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0106
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0106
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 실수
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 실수
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 실수
기대: isIntegralNumber 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":40.5,"risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0107
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0107
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 문자열
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 문자열
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 문자열
기대: isIntegralNumber 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":"40","risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0108
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0108
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score -1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score -1
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score -1
기대: 0 미만 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":-1,"risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0109
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0109
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 0
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 0
기대: 점수 범위 통과
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":0,"risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0110
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0110
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 100
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 100
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 100
기대: 점수 범위 통과
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":100,"risk_grade":"HIGH"}

## 20261103T033035-526c702671 / IF-0111
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0111
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 101
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 101
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI score 101
기대: 100 초과 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":101,"risk_grade":"HIGH"}

## 20261103T033035-526c702671 / IF-0112
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0112
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade 없음
기대: 등급 검증 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":40}

## 20261103T033035-526c702671 / IF-0113
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0113
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:49+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade LOW
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade LOW
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade LOW
기대: 등급 통과
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"LOW"}

## 20261103T033035-526c702671 / IF-0114
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0114
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade MID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade MID
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade MID
기대: 등급 통과
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":50,"risk_grade":"MID"}

## 20261103T033035-526c702671 / IF-0115
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0115
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade HIGH
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade HIGH
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade HIGH
기대: 등급 통과
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":70,"risk_grade":"HIGH"}

## 20261103T033035-526c702671 / IF-0116
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0116
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade lower
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade lower
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade lower
기대: 등급 거절 (대소문자)
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"low"}

## 20261103T033035-526c702671 / IF-0117
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0117
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade UNKNOWN
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI grade UNKNOWN
기대: 등급 거절
1차=PASS 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"UNKNOWN"}

## 20261103T033035-526c702671 / IF-0118
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0118
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 버전 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 버전 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 버전 없음
기대: SIMPLE_V1 기본값
1차=PASS 2차=FAIL 최종=FAIL
입력: model_version 누락

## 20261103T033035-526c702671 / IF-0119
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0119
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 JSON 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 설명 JSON 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 설명 JSON 저장
기대: 설명 전체 JSON 문자열 저장
1차=PASS 2차=FAIL 최종=FAIL
입력: AI 응답에 factors/task_scores 포함

## 20261103T033035-526c702671 / IF-0120
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0120
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 상태 완료
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 상태 완료
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 상태 완료
기대: PENDING_AI→AI_COMPLETED
1차=PASS 2차=FAIL 최종=FAIL
입력: AI 성공 응답

## 20261103T033035-526c702671 / IF-0121
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0121
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 요청 실패
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 요청 실패
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 요청 실패
기대: AIClient 예외 처리
1차=PASS 2차=FAIL 최종=FAIL
입력: 연결 거절/응답 지연

## 20261103T033035-526c702671 / IF-0122
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0122
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 성공 후 저장 실패
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 성공 후 저장 실패
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 성공 후 저장 실패
기대: 실패 응답 확인
1차=PASS 2차=FAIL 최종=FAIL
입력: riskResultRepository.save 예외 주입

## 20261103T033035-526c702671 / IF-0123
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0123
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: result AI null
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: result AI null
기대: score/grade/explanation=null, factors/taskScores=[]
1차=PASS 2차=FAIL 최종=FAIL
입력: aiRiskResult=null

## 20261103T033035-526c702671 / IF-0124
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0124
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 설명 신형
기대: explanation=A
1차=PASS 2차=FAIL 최종=FAIL
입력: explanation="A"

## 20261103T033035-526c702671 / IF-0125
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0125
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 설명 구형
기대: explanation=B
1차=PASS 2차=FAIL 최종=FAIL
입력: summary="B"

## 20261103T033035-526c702671 / IF-0126
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0126
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 설명 없음
기대: explanation=null
1차=PASS 2차=FAIL 최종=FAIL
입력: explanation,summary 둘 다 누락

## 20261103T033035-526c702671 / IF-0127
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0127
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 출처 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 출처 없음
기대: source=basic
1차=PASS 2차=FAIL 최종=FAIL
입력: explanation_source 누락

## 20261103T033035-526c702671 / IF-0128
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0128
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 출처 gemini
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 출처 gemini
기대: source=gemini
1차=PASS 2차=FAIL 최종=FAIL
입력: explanation_source=gemini

## 20261103T033035-526c702671 / IF-0129
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0129
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 요인 신형
기대: 해당 name/max/points 유지
1차=PASS 2차=FAIL 최종=FAIL
입력: factors.name, max, points

## 20261103T033035-526c702671 / IF-0130
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0130
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 요인 구형
기대: name과 max로 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: factors.label, maximum, points

## 20261103T033035-526c702671 / IF-0131
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0131
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 요인 없음
기대: 빈 배열
1차=PASS 2차=FAIL 최종=FAIL
입력: factors 누락

## 20261103T033035-526c702671 / IF-0132
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0132
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:50+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 작업 신형
기대: 각 name, ML, DL 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: task_scores 포함

## 20261103T033035-526c702671 / IF-0133
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0133
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 작업 구형
기대: 각 name 또는 label 매핑
1차=PASS 2차=FAIL 최종=FAIL
입력: task_basis 포함

## 20261103T033035-526c702671 / IF-0134
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0134
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 작업 없음
기대: 빈 배열
1차=PASS 2차=FAIL 최종=FAIL
입력: task_scores/task_basis 누락

## 20261103T033035-526c702671 / IF-0135
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0135
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 깨진 설명
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 깨진 설명
기대: 빈 객체 fallback, 500 없음
1차=PASS 2차=FAIL 최종=FAIL
입력: explanationJson 잘못된 JSON

## 20261103T033035-526c702671 / IF-0136
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0136
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 없는 ID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 없는 ID
기대: notFound 오류
1차=PASS 2차=FAIL 최종=FAIL
입력: id=999999

## 20261103T033035-526c702671 / IF-0137
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0137
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 결과 있는 평가 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 결과 있는 평가 삭제
기대: 연결 해제→AI 결과 삭제→평가 삭제
1차=PASS 2차=FAIL 최종=FAIL
입력: AI 결과 있는 평가 삭제

## 20261103T033035-526c702671 / IF-0138
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0138
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: PENDING_AI 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: PENDING_AI 삭제
기대: AI 결과가 없어도 평가 삭제
1차=PASS 2차=FAIL 최종=FAIL
입력: PENDING_AI 삭제

## 20261103T033035-526c702671 / IF-0139
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0139
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 없는 ID 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 없는 ID 삭제
기대: notFound 응답
1차=PASS 2차=FAIL 최종=FAIL
입력: 없는 ID 삭제

## 20261103T033035-526c702671 / IF-0140
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0140
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:51+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 같은 ID 두 번 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 같은 ID 두 번 삭제
기대: 두 번째는 notFound
1차=PASS 2차=FAIL 최종=FAIL
입력: 같은 ID 두 번 삭제

## 20261103T033035-526c702671 / IF-0141
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0141
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 평가 삭제 후 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 평가 삭제 후 조회
기대: 해당 ID 조회 불가
1차=PASS 2차=FAIL 최종=FAIL
입력: 평가 삭제 후 조회

## 20261103T033035-526c702671 / IF-0142
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0142
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 한 평가 삭제 후 다른 평가 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 한 평가 삭제 후 다른 평가 조회
기대: 다른 ID는 유지
1차=PASS 2차=FAIL 최종=FAIL
입력: 한 평가 삭제 후 다른 평가 조회

## 20261103T033035-526c702671 / IF-0143
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0143
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 총 평가 0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 총 평가 0
기대: totalCount=0
1차=PASS 2차=FAIL 최종=FAIL
입력: 총 평가 0

## 20261103T033035-526c702671 / IF-0144
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0144
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 총 평가 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 총 평가 1
기대: totalCount=1
1차=PASS 2차=FAIL 최종=FAIL
입력: 총 평가 1

## 20261103T033035-526c702671 / IF-0145
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0145
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 미분석 평가 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 미분석 평가 1
기대: analyzedCount=0
1차=PASS 2차=FAIL 최종=FAIL
입력: 미분석 평가 1

## 20261103T033035-526c702671 / IF-0146
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0146
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 완료 LOW 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 완료 LOW 1
기대: analyzedCount=1/highRiskCount=0
1차=PASS 2차=FAIL 최종=FAIL
입력: 완료 LOW 1

## 20261103T033035-526c702671 / IF-0147
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0147
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 완료 HIGH 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 완료 HIGH 1
기대: analyzedCount=1/highRiskCount=1
1차=PASS 2차=FAIL 최종=FAIL
입력: 완료 HIGH 1

## 20261103T033035-526c702671 / IF-0148
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0148
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: HIGH 2+MID 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: HIGH 2+MID 1
기대: highRiskCount=2
1차=PASS 2차=FAIL 최종=FAIL
입력: HIGH 2+MID 1

## 20261103T033035-526c702671 / IF-0149
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0149
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 첫 페이지 20개
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 첫 페이지 20개
기대: content size<=20
1차=PASS 2차=FAIL 최종=FAIL
입력: 첫 페이지 20개

## 20261103T033035-526c702671 / IF-0150
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0150
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 21개에서 page0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 21개에서 page0
기대: 20개
1차=PASS 2차=FAIL 최종=FAIL
입력: 21개에서 page0

## 20261103T033035-526c702671 / IF-0151
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0151
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:52+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 21개에서 page1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 21개에서 page1
기대: 1개
1차=PASS 2차=FAIL 최종=FAIL
입력: 21개에서 page1

## 20261103T033035-526c702671 / IF-0152
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0152
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:53+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 동일 시각 2개
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 동일 시각 2개
기대: assessedAt,id DESC 순서
1차=PASS 2차=FAIL 최종=FAIL
입력: 동일 시각 2개

## 20261103T034653-861cf08d61 / IF-0094
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0094
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 직무 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 직무 조회
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 직무 조회
기대: Job 저장소에서 정확한 ID 조회
1차=FAIL 2차=FAIL 최종=FAIL
입력: jobId=1 존재

## 20261103T034653-861cf08d61 / IF-0095
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0095
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 직무 미존재
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 직무 미존재
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 직무 미존재
기대: ApiException.notFound
1차=FAIL 2차=FAIL 최종=FAIL
입력: jobId=999999

## 20261103T034653-861cf08d61 / IF-0096
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0096
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: Applicant 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: Applicant 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Applicant 저장
기대: displayName은 trim된 이름, age 원본 숫자
1차=FAIL 2차=FAIL 최종=FAIL
입력: 정상 요청

## 20261103T034653-861cf08d61 / IF-0097
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0097
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: HealthSnapshot 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: HealthSnapshot 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: HealthSnapshot 저장
기대: physicalLevel/chronicDisease/workHourLimit 보존
1차=FAIL 2차=FAIL 최종=FAIL
입력: 만성질환=true, 시간=6

## 20261103T034653-861cf08d61 / IF-0098
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0098
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 평가 생성
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 평가 생성
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 평가 생성
기대: status=PENDING_AI; assessedAt UTC
1차=FAIL 2차=FAIL 최종=FAIL
입력: 정상 입력

## 20261103T034653-861cf08d61 / IF-0099
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0099
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 title
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 title
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 전송 title
기대: title에 jobTitle 전송
1차=FAIL 2차=FAIL 최종=FAIL
입력: 직무명=아파트 야간 경비원

## 20261103T034653-861cf08d61 / IF-0100
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0100
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 age
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 age
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 전송 age
기대: age=72 그대로 전송
1차=FAIL 2차=FAIL 최종=FAIL
입력: age=72

## 20261103T034653-861cf08d61 / IF-0101
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0101
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 physical_level
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 physical_level
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 전송 physical_level
기대: physical_level=3 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: physicalLevel=3

## 20261103T034653-861cf08d61 / IF-0102
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0102
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:19+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 chronic_disease
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 chronic_disease
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 전송 chronic_disease
기대: boolean true 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: chronicDisease=true

## 20261103T034653-861cf08d61 / IF-0103
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0103
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 전송 work_hour_limit
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 전송 work_hour_limit
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 전송 work_hour_limit
기대: work_hour_limit=6 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: workHourLimit=6

## 20261103T034653-861cf08d61 / IF-0104
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0104
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 응답 null
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 응답 null
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 응답 null
기대: ApiException.aiError
1차=FAIL 2차=FAIL 최종=FAIL
입력: AI mock null

## 20261103T034653-861cf08d61 / IF-0105
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0105
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 없음
기대: 점수 검증 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0106
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0106
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 실수
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 실수
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 실수
기대: isIntegralNumber 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":40.5,"risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0107
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0107
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 문자열
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 문자열
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 문자열
기대: isIntegralNumber 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":"40","risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0108
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0108
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score -1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score -1
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score -1
기대: 0 미만 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":-1,"risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0109
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0109
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 0
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 0
기대: 점수 범위 통과
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":0,"risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0110
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0110
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 100
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 100
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 100
기대: 점수 범위 통과
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":100,"risk_grade":"HIGH"}

## 20261103T034653-861cf08d61 / IF-0111
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0111
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI score 101
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI score 101
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI score 101
기대: 100 초과 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":101,"risk_grade":"HIGH"}

## 20261103T034653-861cf08d61 / IF-0112
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0112
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:20+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade 없음
기대: 등급 검증 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":40}

## 20261103T034653-861cf08d61 / IF-0113
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0113
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:21+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade LOW
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade LOW
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade LOW
기대: 등급 통과
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"LOW"}

## 20261103T034653-861cf08d61 / IF-0114
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0114
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:21+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade MID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade MID
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade MID
기대: 등급 통과
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":50,"risk_grade":"MID"}

## 20261103T034653-861cf08d61 / IF-0115
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0115
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:21+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade HIGH
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade HIGH
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade HIGH
기대: 등급 통과
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":70,"risk_grade":"HIGH"}

## 20261103T034653-861cf08d61 / IF-0116
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0116
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:22+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade lower
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade lower
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade lower
기대: 등급 거절 (대소문자)
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"low"}

## 20261103T034653-861cf08d61 / IF-0117
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0117
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:22+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI grade UNKNOWN
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI grade UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI grade UNKNOWN
기대: 등급 거절
1차=FAIL 2차=FAIL 최종=FAIL
입력: {"risk_score":40,"risk_grade":"UNKNOWN"}

## 20261103T034653-861cf08d61 / IF-0118
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0118
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:22+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 버전 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 버전 없음
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 버전 없음
기대: SIMPLE_V1 기본값
1차=FAIL 2차=FAIL 최종=FAIL
입력: model_version 누락

## 20261103T034653-861cf08d61 / IF-0119
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0119
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:23+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 JSON 저장
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 설명 JSON 저장
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 설명 JSON 저장
기대: 설명 전체 JSON 문자열 저장
1차=FAIL 2차=FAIL 최종=FAIL
입력: AI 응답에 factors/task_scores 포함

## 20261103T034653-861cf08d61 / IF-0120
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0120
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:23+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 상태 완료
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: 상태 완료
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 상태 완료
기대: PENDING_AI→AI_COMPLETED
1차=FAIL 2차=FAIL 최종=FAIL
입력: AI 성공 응답

## 20261103T034653-861cf08d61 / IF-0121
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0121
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:23+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 요청 실패
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 요청 실패
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 요청 실패
기대: AIClient 예외 처리
1차=FAIL 2차=FAIL 최종=FAIL
입력: 연결 거절/응답 지연

## 20261103T034653-861cf08d61 / IF-0122
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0122
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:23+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 성공 후 저장 실패
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: AI 성공 후 저장 실패
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 성공 후 저장 실패
기대: 실패 응답 확인
1차=FAIL 2차=FAIL 최종=FAIL
입력: riskResultRepository.save 예외 주입

## 20261103T034653-861cf08d61 / IF-0123
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0123
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:24+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: result AI null
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: result AI null
기대: score/grade/explanation=null, factors/taskScores=[]
1차=FAIL 2차=FAIL 최종=FAIL
입력: aiRiskResult=null

## 20261103T034653-861cf08d61 / IF-0124
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0124
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:25+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 설명 신형
기대: explanation=A
1차=FAIL 2차=FAIL 최종=FAIL
입력: explanation="A"

## 20261103T034653-861cf08d61 / IF-0125
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0125
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:25+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 설명 구형
기대: explanation=B
1차=FAIL 2차=FAIL 최종=FAIL
입력: summary="B"

## 20261103T034653-861cf08d61 / IF-0126
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0126
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:25+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 설명 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 설명 없음
기대: explanation=null
1차=FAIL 2차=FAIL 최종=FAIL
입력: explanation,summary 둘 다 누락

## 20261103T034653-861cf08d61 / IF-0127
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0127
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:26+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 출처 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 출처 없음
기대: source=basic
1차=FAIL 2차=FAIL 최종=FAIL
입력: explanation_source 누락

## 20261103T034653-861cf08d61 / IF-0128
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0128
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:26+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 출처 gemini
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 출처 gemini
기대: source=gemini
1차=FAIL 2차=FAIL 최종=FAIL
입력: explanation_source=gemini

## 20261103T034653-861cf08d61 / IF-0129
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0129
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:28+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 요인 신형
기대: 해당 name/max/points 유지
1차=FAIL 2차=FAIL 최종=FAIL
입력: factors.name, max, points

## 20261103T034653-861cf08d61 / IF-0130
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0130
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:28+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 요인 구형
기대: name과 max로 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: factors.label, maximum, points

## 20261103T034653-861cf08d61 / IF-0131
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0131
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:28+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 요인 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 요인 없음
기대: 빈 배열
1차=FAIL 2차=FAIL 최종=FAIL
입력: factors 누락

## 20261103T034653-861cf08d61 / IF-0132
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0132
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:29+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 신형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 작업 신형
기대: 각 name, ML, DL 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: task_scores 포함

## 20261103T034653-861cf08d61 / IF-0133
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0133
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:29+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 구형
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 작업 구형
기대: 각 name 또는 label 매핑
1차=FAIL 2차=FAIL 최종=FAIL
입력: task_basis 포함

## 20261103T034653-861cf08d61 / IF-0134
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0134
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:30+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 작업 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 작업 없음
기대: 빈 배열
1차=FAIL 2차=FAIL 최종=FAIL
입력: task_scores/task_basis 누락

## 20261103T034653-861cf08d61 / IF-0135
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0135
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:30+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 깨진 설명
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 깨진 설명
기대: 빈 객체 fallback, 500 없음
1차=FAIL 2차=FAIL 최종=FAIL
입력: explanationJson 잘못된 JSON

## 20261103T034653-861cf08d61 / IF-0136
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0136
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:30+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 없는 ID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: getResult → JSON 파싱 → DTO
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 없는 ID
기대: notFound 오류
1차=FAIL 2차=FAIL 최종=FAIL
입력: id=999999

## 20261103T034653-861cf08d61 / IF-0137
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0137
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: AI 결과 있는 평가 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 결과 있는 평가 삭제
기대: 연결 해제→AI 결과 삭제→평가 삭제
1차=FAIL 2차=FAIL 최종=FAIL
입력: AI 결과 있는 평가 삭제

## 20261103T034653-861cf08d61 / IF-0138
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0138
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: PENDING_AI 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: PENDING_AI 삭제
기대: AI 결과가 없어도 평가 삭제
1차=FAIL 2차=FAIL 최종=FAIL
입력: PENDING_AI 삭제

## 20261103T034653-861cf08d61 / IF-0139
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0139
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 없는 ID 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 없는 ID 삭제
기대: notFound 응답
1차=FAIL 2차=FAIL 최종=FAIL
입력: 없는 ID 삭제

## 20261103T034653-861cf08d61 / IF-0140
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0140
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 같은 ID 두 번 삭제
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 같은 ID 두 번 삭제
기대: 두 번째는 notFound
1차=FAIL 2차=FAIL 최종=FAIL
입력: 같은 ID 두 번 삭제

## 20261103T034653-861cf08d61 / IF-0141
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0141
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 평가 삭제 후 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 평가 삭제 후 조회
기대: 해당 ID 조회 불가
1차=FAIL 2차=FAIL 최종=FAIL
입력: 평가 삭제 후 조회

## 20261103T034653-861cf08d61 / IF-0142
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0142
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 한 평가 삭제 후 다른 평가 조회
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: delete() FK 해제 / 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 한 평가 삭제 후 다른 평가 조회
기대: 다른 ID는 유지
1차=FAIL 2차=FAIL 최종=FAIL
입력: 한 평가 삭제 후 다른 평가 조회

## 20261103T034653-861cf08d61 / IF-0143
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0143
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 총 평가 0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 총 평가 0
기대: totalCount=0
1차=FAIL 2차=FAIL 최종=FAIL
입력: 총 평가 0

## 20261103T034653-861cf08d61 / IF-0144
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0144
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 총 평가 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 총 평가 1
기대: totalCount=1
1차=FAIL 2차=FAIL 최종=FAIL
입력: 총 평가 1

## 20261103T034653-861cf08d61 / IF-0145
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0145
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:31+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 미분석 평가 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 미분석 평가 1
기대: analyzedCount=0
1차=FAIL 2차=FAIL 최종=FAIL
입력: 미분석 평가 1

## 20261103T034653-861cf08d61 / IF-0146
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0146
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:32+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 완료 LOW 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 완료 LOW 1
기대: analyzedCount=1/highRiskCount=0
1차=FAIL 2차=FAIL 최종=FAIL
입력: 완료 LOW 1

## 20261103T034653-861cf08d61 / IF-0147
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0147
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 완료 HIGH 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 완료 HIGH 1
기대: analyzedCount=1/highRiskCount=1
1차=FAIL 2차=FAIL 최종=FAIL
입력: 완료 HIGH 1

## 20261103T034653-861cf08d61 / IF-0148
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0148
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: HIGH 2+MID 1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: HIGH 2+MID 1
기대: highRiskCount=2
1차=FAIL 2차=FAIL 최종=FAIL
입력: HIGH 2+MID 1

## 20261103T034653-861cf08d61 / IF-0149
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0149
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 첫 페이지 20개
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 첫 페이지 20개
기대: content size<=20
1차=FAIL 2차=FAIL 최종=FAIL
입력: 첫 페이지 20개

## 20261103T034653-861cf08d61 / IF-0150
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0150
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 21개에서 page0
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 21개에서 page0
기대: 20개
1차=FAIL 2차=FAIL 최종=FAIL
입력: 21개에서 page0

## 20261103T034653-861cf08d61 / IF-0151
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0151
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 21개에서 page1
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 21개에서 page1
기대: 1개
1차=FAIL 2차=FAIL 최종=FAIL
입력: 21개에서 page1

## 20261103T034653-861cf08d61 / IF-0152
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0152
- FEATURE_ID: FEAT-Spring 서비스
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:33+09:00
- area: 01_unit_integration
- section: spring_service
- scenario: 동일 시각 2개
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: GradleJUnitSuite
- command_b: gradlew test
- result_b: FAIL
- expected_b: PASS
- actual_b: cross=FAIL
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/service/AssessmentService.java
- function: summary/list
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 동일 시각 2개
기대: assessedAt,id DESC 순서
1차=FAIL 2차=FAIL 최종=FAIL
입력: 동일 시각 2개

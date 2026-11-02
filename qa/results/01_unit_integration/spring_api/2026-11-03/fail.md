# FAIL

## 20261103T033035-526c702671 / IF-0047
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0047
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 삭제

## 20261103T033035-526c702671 / IF-0048
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0048
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName ''
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName ''
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 ''로 변경

## 20261103T033035-526c702671 / IF-0049
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0049
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName ' '
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName ' '
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 ' '로 변경

## 20261103T033035-526c702671 / IF-0050
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0050
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'로 변경

## 20261103T033035-526c702671 / IF-0051
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0051
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'로 변경

## 20261103T033035-526c702671 / IF-0052
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0052
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 17
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: applicantName 17
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 17로 변경

## 20261103T033035-526c702671 / IF-0053
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0053
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 삭제

## 20261103T033035-526c702671 / IF-0054
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0054
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age -1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age -1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 -1로 변경

## 20261103T033035-526c702671 / IF-0055
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0055
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 0로 변경

## 20261103T033035-526c702671 / IF-0056
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0056
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 1로 변경

## 20261103T033035-526c702671 / IF-0057
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0057
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 120
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 120
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 120로 변경

## 20261103T033035-526c702671 / IF-0058
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0058
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 121
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 121
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 121로 변경

## 20261103T033035-526c702671 / IF-0059
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0059
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 60.5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age 60.5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 60.5로 변경

## 20261103T033035-526c702671 / IF-0060
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0060
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age '70'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: age '70'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 '70'로 변경

## 20261103T033035-526c702671 / IF-0061
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0061
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 삭제

## 20261103T033035-526c702671 / IF-0062
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0062
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 0로 변경

## 20261103T033035-526c702671 / IF-0063
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0063
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 1로 변경

## 20261103T033035-526c702671 / IF-0064
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0064
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 3
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 3
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 3로 변경

## 20261103T033035-526c702671 / IF-0065
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0065
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 5로 변경

## 20261103T033035-526c702671 / IF-0066
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0066
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 6
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel 6
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 6로 변경

## 20261103T033035-526c702671 / IF-0067
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0067
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel '3'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: physicalLevel '3'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 '3'로 변경

## 20261103T033035-526c702671 / IF-0068
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0068
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: chronicDisease 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 삭제

## 20261103T033035-526c702671 / IF-0069
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0069
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease True
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: chronicDisease True
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 True로 변경

## 20261103T033035-526c702671 / IF-0070
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0070
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease False
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: chronicDisease False
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 False로 변경

## 20261103T033035-526c702671 / IF-0071
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0071
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 'yes'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: chronicDisease 'yes'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 'yes'로 변경

## 20261103T033035-526c702671 / IF-0072
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0072
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: chronicDisease 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 1로 변경

## 20261103T033035-526c702671 / IF-0073
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0073
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 삭제

## 20261103T033035-526c702671 / IF-0074
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0074
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 0로 변경

## 20261103T033035-526c702671 / IF-0075
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0075
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 1로 변경

## 20261103T033035-526c702671 / IF-0076
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0076
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 8
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 8
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 8로 변경

## 20261103T033035-526c702671 / IF-0077
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0077
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 24
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 24
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 24로 변경

## 20261103T033035-526c702671 / IF-0078
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0078
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 25
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 25
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 25로 변경

## 20261103T033035-526c702671 / IF-0079
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0079
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:45+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 2.5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: workHourLimit 2.5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 2.5로 변경

## 20261103T033035-526c702671 / IF-0080
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0080
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 삭제

## 20261103T033035-526c702671 / IF-0081
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0081
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 1로 변경

## 20261103T033035-526c702671 / IF-0082
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0082
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 2
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId 2
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 2로 변경

## 20261103T033035-526c702671 / IF-0083
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0083
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 999999
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId 999999
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 999999로 변경

## 20261103T033035-526c702671 / IF-0084
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0084
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId -1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId -1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 -1로 변경

## 20261103T033035-526c702671 / IF-0085
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0085
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 'abc'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: jobId 'abc'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 'abc'로 변경

## 20261103T033035-526c702671 / IF-0086
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0086
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: malformed body: {"age":
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: malformed body: {"age":
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: malformed body: {"age":

## 20261103T033035-526c702671 / IF-0087
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0087
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: text/plain Content-Type
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: text/plain Content-Type
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: text/plain Content-Type

## 20261103T033035-526c702671 / IF-0088
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0088
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: POST body = []
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: POST body = []
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: POST body = []

## 20261103T033035-526c702671 / IF-0089
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0089
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: POST body=null
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: POST body=null
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: POST body=null

## 20261103T033035-526c702671 / IF-0090
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0090
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with page=-1
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: GET /api/assessments with page=-1
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with page=-1

## 20261103T033035-526c702671 / IF-0091
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0091
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with size=0
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: GET /api/assessments with size=0
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with size=0

## 20261103T033035-526c702671 / IF-0092
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0092
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with size=20
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: GET /api/assessments with size=20
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with size=20

## 20261103T033035-526c702671 / IF-0093
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0093
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:41:46+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with page=9999
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: GET /api/assessments with page=9999
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with page=9999

## 20261103T034653-861cf08d61 / IF-0047
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0047
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:15+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 삭제

## 20261103T034653-861cf08d61 / IF-0048
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0048
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:15+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName ''
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName ''
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 ''로 변경

## 20261103T034653-861cf08d61 / IF-0049
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0049
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName ' '
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName ' '
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 ' '로 변경

## 20261103T034653-861cf08d61 / IF-0050
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0050
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'로 변경

## 20261103T034653-861cf08d61 / IF-0051
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0051
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'로 변경

## 20261103T034653-861cf08d61 / IF-0052
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0052
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: applicantName 17
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: applicantName 17
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 applicantName만 17로 변경

## 20261103T034653-861cf08d61 / IF-0053
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0053
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 삭제

## 20261103T034653-861cf08d61 / IF-0054
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0054
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age -1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age -1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 -1로 변경

## 20261103T034653-861cf08d61 / IF-0055
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0055
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 0로 변경

## 20261103T034653-861cf08d61 / IF-0056
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0056
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 1로 변경

## 20261103T034653-861cf08d61 / IF-0057
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0057
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 120
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 120
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 120로 변경

## 20261103T034653-861cf08d61 / IF-0058
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0058
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 121
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 121
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 121로 변경

## 20261103T034653-861cf08d61 / IF-0059
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0059
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age 60.5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age 60.5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 60.5로 변경

## 20261103T034653-861cf08d61 / IF-0060
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0060
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: age '70'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: age '70'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 age만 '70'로 변경

## 20261103T034653-861cf08d61 / IF-0061
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0061
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 삭제

## 20261103T034653-861cf08d61 / IF-0062
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0062
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 0로 변경

## 20261103T034653-861cf08d61 / IF-0063
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0063
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 1로 변경

## 20261103T034653-861cf08d61 / IF-0064
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0064
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 3
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 3
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 3로 변경

## 20261103T034653-861cf08d61 / IF-0065
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0065
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 5로 변경

## 20261103T034653-861cf08d61 / IF-0066
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0066
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel 6
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel 6
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 6로 변경

## 20261103T034653-861cf08d61 / IF-0067
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0067
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: physicalLevel '3'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: physicalLevel '3'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 physicalLevel만 '3'로 변경

## 20261103T034653-861cf08d61 / IF-0068
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0068
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: chronicDisease 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 삭제

## 20261103T034653-861cf08d61 / IF-0069
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0069
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease True
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: chronicDisease True
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 True로 변경

## 20261103T034653-861cf08d61 / IF-0070
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0070
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:16+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease False
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: chronicDisease False
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 False로 변경

## 20261103T034653-861cf08d61 / IF-0071
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0071
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 'yes'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: chronicDisease 'yes'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 'yes'로 변경

## 20261103T034653-861cf08d61 / IF-0072
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0072
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: chronicDisease 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: chronicDisease 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 chronicDisease만 1로 변경

## 20261103T034653-861cf08d61 / IF-0073
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0073
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 삭제

## 20261103T034653-861cf08d61 / IF-0074
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0074
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 0
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 0
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 0로 변경

## 20261103T034653-861cf08d61 / IF-0075
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0075
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 1로 변경

## 20261103T034653-861cf08d61 / IF-0076
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0076
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 8
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 8
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 8로 변경

## 20261103T034653-861cf08d61 / IF-0077
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0077
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 24
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 24
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 24로 변경

## 20261103T034653-861cf08d61 / IF-0078
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0078
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 25
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 25
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 25로 변경

## 20261103T034653-861cf08d61 / IF-0079
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0079
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: workHourLimit 2.5
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: workHourLimit 2.5
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 workHourLimit만 2.5로 변경

## 20261103T034653-861cf08d61 / IF-0080
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0080
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 필드 누락
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId 필드 누락
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 삭제

## 20261103T034653-861cf08d61 / IF-0081
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0081
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId 1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 1로 변경

## 20261103T034653-861cf08d61 / IF-0082
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0082
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:17+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 2
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId 2
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 2로 변경

## 20261103T034653-861cf08d61 / IF-0083
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0083
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 999999
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId 999999
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 999999로 변경

## 20261103T034653-861cf08d61 / IF-0084
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0084
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId -1
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId -1
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 -1로 변경

## 20261103T034653-861cf08d61 / IF-0085
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0085
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: jobId 'abc'
- tool_a: Postman/MockMvc/SQL
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: jobId 'abc'
기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기본 정상 JSON에서 jobId만 'abc'로 변경

## 20261103T034653-861cf08d61 / IF-0086
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0086
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: malformed body: {"age":
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: malformed body: {"age":
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: malformed body: {"age":

## 20261103T034653-861cf08d61 / IF-0087
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0087
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: text/plain Content-Type
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: text/plain Content-Type
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: text/plain Content-Type

## 20261103T034653-861cf08d61 / IF-0088
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0088
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: POST body = []
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: POST body = []
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: POST body = []

## 20261103T034653-861cf08d61 / IF-0089
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0089
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: POST body=null
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: POST body=null
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: POST body=null

## 20261103T034653-861cf08d61 / IF-0090
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0090
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with page=-1
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: GET /api/assessments with page=-1
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with page=-1

## 20261103T034653-861cf08d61 / IF-0091
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0091
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with size=0
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: GET /api/assessments with size=0
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with size=0

## 20261103T034653-861cf08d61 / IF-0092
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0092
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with size=20
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: GET /api/assessments with size=20
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with size=20

## 20261103T034653-861cf08d61 / IF-0093
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0093
- FEATURE_ID: FEAT-Spring API
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:18+09:00
- area: 01_unit_integration
- section: spring_api
- scenario: GET /api/assessments with page=9999
- tool_a: Postman/MockMvc
- command_a: no automated test id mapping
- result_a: NOT_RUN
- expected_a: PASS
- actual_a: 시트 TC에 연결된 자동 테스트 식별자 없음
- tool_b: NOT_RUN
- command_b: NOT_RUN
- result_b: NOT_RUN
- expected_b: PASS
- actual_b: cross=NOT_RUN
- status: NOT_RUN
- git_commit: aad712788755
- dirty: true
- code_file: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: GET /api/assessments with page=9999
기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/assessments with page=9999

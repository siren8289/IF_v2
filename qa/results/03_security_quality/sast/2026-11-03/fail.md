# FAIL

## 20261103T033035-526c702671 / IF-0334
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0334
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 03_security_quality
- section: sast
- scenario: 개인정보 응답
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 개인정보 응답
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 개인정보 응답
기대: 불필요한 민감정보 최소화 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 결과 조회 응답에 민감한 불필요 필드 포함 여부

## 20261103T033035-526c702671 / IF-0335
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0335
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 03_security_quality
- section: sast
- scenario: 인증 없는 조회
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 인증 없는 조회
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 인증 없는 조회
기대: 현재 공개 API 정책인지 확인 후 취약점 분류
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 인증 없이 GET /api/assessments

## 20261103T033035-526c702671 / IF-0336
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0336
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 03_security_quality
- section: sast
- scenario: 인증 없는 삭제
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 인증 없는 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 인증 없는 삭제
기대: 요구사항의 접근통제 정책 대비
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 인증 없이 DELETE

## 20261103T033035-526c702671 / IF-0337
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0337
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:10+09:00
- area: 03_security_quality
- section: sast
- scenario: XSS 이름
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: XSS 이름
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: XSS 이름
기대: 화면 스크립트 실행 금지
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: <script>alert(1)</script>

## 20261103T033035-526c702671 / IF-0338
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0338
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:11+09:00
- area: 03_security_quality
- section: sast
- scenario: 대형 요청
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 대형 요청
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 대형 요청
기대: 4xx/크기 제한 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 이름 10000자

## 20261103T033035-526c702671 / IF-0339
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0339
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:11+09:00
- area: 03_security_quality
- section: sast
- scenario: SQL 문자열
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: SQL 문자열
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: SQL 문자열
기대: SQL 문맥 비실행
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 이름에 SQL 특수문자

## 20261103T033035-526c702671 / IF-0340
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0340
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:11+09:00
- area: 03_security_quality
- section: sast
- scenario: API Key
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: API Key
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: API Key
기대: 키 노출 없음
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GEMINI_API_KEY 로그 확인

## 20261103T033035-526c702671 / IF-0341
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0341
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 03_security_quality
- section: sast
- scenario: CORS
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: CORS
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: CORS
기대: 서버 정책에 맞는 응답
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 허용되지 않은 Origin

## 20261103T034653-861cf08d61 / IF-0334
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0334
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: 개인정보 응답
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 개인정보 응답
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 개인정보 응답
기대: 불필요한 민감정보 최소화 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 결과 조회 응답에 민감한 불필요 필드 포함 여부

## 20261103T034653-861cf08d61 / IF-0335
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0335
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: 인증 없는 조회
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 인증 없는 조회
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 인증 없는 조회
기대: 현재 공개 API 정책인지 확인 후 취약점 분류
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 인증 없이 GET /api/assessments

## 20261103T034653-861cf08d61 / IF-0336
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0336
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: 인증 없는 삭제
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 인증 없는 삭제
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 인증 없는 삭제
기대: 요구사항의 접근통제 정책 대비
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 인증 없이 DELETE

## 20261103T034653-861cf08d61 / IF-0337
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0337
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: XSS 이름
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: XSS 이름
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: XSS 이름
기대: 화면 스크립트 실행 금지
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: <script>alert(1)</script>

## 20261103T034653-861cf08d61 / IF-0338
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0338
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: 대형 요청
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: 대형 요청
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 대형 요청
기대: 4xx/크기 제한 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 이름 10000자

## 20261103T034653-861cf08d61 / IF-0339
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0339
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: SQL 문자열
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: SQL 문자열
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: SQL 문자열
기대: SQL 문맥 비실행
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 이름에 SQL 특수문자

## 20261103T034653-861cf08d61 / IF-0340
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0340
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: API Key
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: API Key
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: API Key
기대: 키 노출 없음
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GEMINI_API_KEY 로그 확인

## 20261103T034653-861cf08d61 / IF-0341
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0341
- FEATURE_ID: FEAT-보안
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 03_security_quality
- section: sast
- scenario: CORS
- tool_a: OWASP/부하도구/SQL
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
- code_file: https://owasp.org/www-project-web-security-testing-guide/
- function: CORS
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: CORS
기대: 서버 정책에 맞는 응답
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 허용되지 않은 Origin

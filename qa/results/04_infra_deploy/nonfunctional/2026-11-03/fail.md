# FAIL

## 20261103T033035-526c702671 / IF-0342
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0342
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 직무 조회 응답시간
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
- code_file: https://docs.docker.com/compose/
- function: 직무 조회 응답시간
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 직무 조회 응답시간
기대: p50/p95 측정, 합격 SLO 확정 필요
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/jobs 30회

## 20261103T033035-526c702671 / IF-0343
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0343
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 평가 동시 요청
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
- code_file: https://docs.docker.com/compose/
- function: 평가 동시 요청
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 평가 동시 요청
기대: 정합성·중복 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 2~5명 정상 등록

## 20261103T033035-526c702671 / IF-0344
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0344
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: AI 응답 지연
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
- code_file: https://docs.docker.com/compose/
- function: AI 응답 지연
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: AI 응답 지연
기대: 타임아웃 정책 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: AI 15초 이상 mock

## 20261103T033035-526c702671 / IF-0345
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0345
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 서비스 시작 순서
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
- code_file: https://docs.docker.com/compose/
- function: 서비스 시작 순서
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 서비스 시작 순서
기대: Nginx crash loop 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: Spring 시작 전 Frontend 기동

## 20261103T033035-526c702671 / IF-0346
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0346
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: DB 복원
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
- code_file: https://docs.docker.com/compose/
- function: DB 복원
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DB 복원
기대: 테스트 DB 일관성
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 백업 후 복구 리허설

## 20261103T033035-526c702671 / IF-0347
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0347
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 모델 메모리
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
- code_file: https://docs.docker.com/compose/
- function: 모델 메모리
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 모델 메모리
기대: Docker OOM 없고 자원 기록
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: ML+DL 초기화 후 memory

## 20261103T033035-526c702671 / IF-0348
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0348
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 로그 추적
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
- code_file: https://docs.docker.com/compose/
- function: 로그 추적
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 로그 추적
기대: Spring↔AI 상관관계 식별 가능 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 평가 등록 1회

## 20261103T033035-526c702671 / IF-0349
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0349
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:12+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 장애 이후 회귀
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
- code_file: https://docs.docker.com/compose/
- function: 장애 이후 회귀
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 장애 이후 회귀
기대: 핵심 시나리오 정상
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 서비스 재시작 후 POST/GET/DELETE

## 20261103T034653-861cf08d61 / IF-0342
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0342
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 직무 조회 응답시간
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
- code_file: https://docs.docker.com/compose/
- function: 직무 조회 응답시간
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 직무 조회 응답시간
기대: p50/p95 측정, 합격 SLO 확정 필요
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: GET /api/jobs 30회

## 20261103T034653-861cf08d61 / IF-0343
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0343
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 평가 동시 요청
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
- code_file: https://docs.docker.com/compose/
- function: 평가 동시 요청
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 평가 동시 요청
기대: 정합성·중복 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 2~5명 정상 등록

## 20261103T034653-861cf08d61 / IF-0344
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0344
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: AI 응답 지연
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
- code_file: https://docs.docker.com/compose/
- function: AI 응답 지연
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: AI 응답 지연
기대: 타임아웃 정책 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: AI 15초 이상 mock

## 20261103T034653-861cf08d61 / IF-0345
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0345
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 서비스 시작 순서
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
- code_file: https://docs.docker.com/compose/
- function: 서비스 시작 순서
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 서비스 시작 순서
기대: Nginx crash loop 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: Spring 시작 전 Frontend 기동

## 20261103T034653-861cf08d61 / IF-0346
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0346
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: DB 복원
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
- code_file: https://docs.docker.com/compose/
- function: DB 복원
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DB 복원
기대: 테스트 DB 일관성
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 백업 후 복구 리허설

## 20261103T034653-861cf08d61 / IF-0347
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0347
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 모델 메모리
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
- code_file: https://docs.docker.com/compose/
- function: 모델 메모리
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 모델 메모리
기대: Docker OOM 없고 자원 기록
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: ML+DL 초기화 후 memory

## 20261103T034653-861cf08d61 / IF-0348
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0348
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 로그 추적
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
- code_file: https://docs.docker.com/compose/
- function: 로그 추적
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 로그 추적
기대: Spring↔AI 상관관계 식별 가능 여부
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 평가 등록 1회

## 20261103T034653-861cf08d61 / IF-0349
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0349
- FEATURE_ID: FEAT-비기능
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:54+09:00
- area: 04_infra_deploy
- section: nonfunctional
- scenario: 장애 이후 회귀
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
- code_file: https://docs.docker.com/compose/
- function: 장애 이후 회귀
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 장애 이후 회귀
기대: 핵심 시나리오 정상
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 서비스 재시작 후 POST/GET/DELETE

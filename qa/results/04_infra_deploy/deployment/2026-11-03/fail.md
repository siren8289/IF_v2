# FAIL

## 20261103T033035-526c702671 / IF-0305
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0305
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: IF_DB_PASSWORD 누락
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: IF_DB_PASSWORD 누락
기대: 설정 단계 실패; 비밀번호 값 미출력
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose config --quiet

## 20261103T033035-526c702671 / IF-0306
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0306
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: .env 경로 오류
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: .env 경로 오류
기대: Compose 루트 파일 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: pwd; ls -la .env ai/.env

## 20261103T033035-526c702671 / IF-0307
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0307
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: DB 비밀번호 변경
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DB 비밀번호 변경
기대: 비밀번호 불일치 시 인증 실패 추적
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기존 DB 볼륨과 .env 설정 비교

## 20261103T033035-526c702671 / IF-0308
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0308
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 8000 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: FastAPI 8000 점유
기대: 충돌 컨테이너 식별
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker ps --format "table {{.Names}}\t{{.Ports}}"

## 20261103T033035-526c702671 / IF-0309
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0309
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 8080 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Spring 8080 점유
기대: 점유 PID 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: lsof -nP -iTCP:8080 -sTCP:LISTEN

## 20261103T033035-526c702671 / IF-0310
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0310
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Nginx 80 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Nginx 80 점유
기대: 점유 PID 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: lsof -nP -iTCP:80 -sTCP:LISTEN

## 20261103T033035-526c702671 / IF-0311
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0311
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: spring→postgres 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: spring→postgres 이름해석
기대: 동일 네트워크/alias 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker network inspect if-app-stack_default

## 20261103T033035-526c702671 / IF-0312
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0312
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: nginx→spring 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: nginx→spring 이름해석
기대: host not found 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=50 frontend

## 20261103T033035-526c702671 / IF-0313
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0313
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: spring→fastapi 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: spring→fastapi 이름해석
기대: UnknownHostException 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=50 spring

## 20261103T033035-526c702671 / IF-0314
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0314
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: PostgreSQL healthcheck
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: PostgreSQL healthcheck
기대: postgres Up(healthy)
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps

## 20261103T033035-526c702671 / IF-0315
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0315
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI health
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: FastAPI health
기대: {"status":"ok"}
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -fsS http://localhost:8000/health

## 20261103T033035-526c702671 / IF-0316
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0316
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring jobs API
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Spring jobs API
기대: 200 JSON
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -i http://localhost:8080/api/jobs

## 20261103T033035-526c702671 / IF-0317
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0317
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Frontend API 프록시
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Frontend API 프록시
기대: 200 JSON
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -i http://localhost/api/jobs

## 20261103T033035-526c702671 / IF-0318
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0318
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 반복 재시작
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Spring 반복 재시작
기대: Restarting 반복 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps -a

## 20261103T033035-526c702671 / IF-0319
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0319
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Frontend 반복 재시작
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Frontend 반복 재시작
기대: Restarting 반복 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps -a

## 20261103T033035-526c702671 / IF-0320
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0320
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: CPU/메모리
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: CPU/메모리
기대: 자원 사용 측정·기준 정의
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker stats --no-stream

## 20261103T033035-526c702671 / IF-0321
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0321
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:08+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: OOMKilled
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: OOMKilled
기대: false; OOM이면 제한 조정
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker inspect if-app-stack-spring-1 --format "{{.State.OOMKilled}}"

## 20261103T033035-526c702671 / IF-0322
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0322
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 재생성 후 데이터 유지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 재생성 후 데이터 유지
기대: 동일 평가 유지
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose down; docker compose up -d --no-build

## 20261103T033035-526c702671 / IF-0323
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0323
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 볼륨 마운트
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 볼륨 마운트
기대: DB 영속 볼륨 존재
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker volume ls

## 20261103T033035-526c702671 / IF-0324
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0324
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 민감정보 출력
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 민감정보 출력
기대: API key/password 등 평문 미노출
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=100 spring fastapi

## 20261103T033035-526c702671 / IF-0325
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0325
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: FastAPI 정지
기대: Spring의 AI 오류/평가 상태 정책 검증
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop fastapi

## 20261103T033035-526c702671 / IF-0326
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0326
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Postgres 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Postgres 정지
기대: Spring 오류 처리·복구 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop postgres

## 20261103T033035-526c702671 / IF-0327
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0327
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Spring 정지
기대: Nginx 실패 응답/재기동 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop spring

## 20261103T033035-526c702671 / IF-0328
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0328
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 복구
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: FastAPI 복구
기대: AI 호출 복구
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose start fastapi

## 20261103T033035-526c702671 / IF-0329
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0329
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 복구
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Spring 복구
기대: GET/POST 회복
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose start spring

## 20261103T033035-526c702671 / IF-0330
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0330
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 외부 노출 여부
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 외부 노출 여부
기대: 8000/8080 127.0.0.1 바인딩
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps

## 20261103T033035-526c702671 / IF-0331
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0331
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: DB 포트 노출
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DB 포트 노출
기대: 5432 호스트 미공개
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps postgres

## 20261103T033035-526c702671 / IF-0332
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0332
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 유효성
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Compose 유효성
기대: 오류 없이 종료
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose config --quiet

## 20261103T033035-526c702671 / IF-0333
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0333
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:09+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 이미지 빌드
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 이미지 빌드
기대: 각 서비스 이미지 성공
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose build

## 20261103T034653-861cf08d61 / IF-0305
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0305
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:51+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: IF_DB_PASSWORD 누락
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: IF_DB_PASSWORD 누락
기대: 설정 단계 실패; 비밀번호 값 미출력
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose config --quiet

## 20261103T034653-861cf08d61 / IF-0306
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0306
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: .env 경로 오류
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: .env 경로 오류
기대: Compose 루트 파일 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: pwd; ls -la .env ai/.env

## 20261103T034653-861cf08d61 / IF-0307
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0307
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: DB 비밀번호 변경
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DB 비밀번호 변경
기대: 비밀번호 불일치 시 인증 실패 추적
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: 기존 DB 볼륨과 .env 설정 비교

## 20261103T034653-861cf08d61 / IF-0308
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0308
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 8000 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: FastAPI 8000 점유
기대: 충돌 컨테이너 식별
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker ps --format "table {{.Names}}\t{{.Ports}}"

## 20261103T034653-861cf08d61 / IF-0309
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0309
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 8080 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Spring 8080 점유
기대: 점유 PID 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: lsof -nP -iTCP:8080 -sTCP:LISTEN

## 20261103T034653-861cf08d61 / IF-0310
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0310
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Nginx 80 점유
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Nginx 80 점유
기대: 점유 PID 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: lsof -nP -iTCP:80 -sTCP:LISTEN

## 20261103T034653-861cf08d61 / IF-0311
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0311
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: spring→postgres 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: spring→postgres 이름해석
기대: 동일 네트워크/alias 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker network inspect if-app-stack_default

## 20261103T034653-861cf08d61 / IF-0312
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0312
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: nginx→spring 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: nginx→spring 이름해석
기대: host not found 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=50 frontend

## 20261103T034653-861cf08d61 / IF-0313
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0313
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: spring→fastapi 이름해석
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: spring→fastapi 이름해석
기대: UnknownHostException 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=50 spring

## 20261103T034653-861cf08d61 / IF-0314
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0314
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: PostgreSQL healthcheck
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: PostgreSQL healthcheck
기대: postgres Up(healthy)
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps

## 20261103T034653-861cf08d61 / IF-0315
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0315
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI health
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: FastAPI health
기대: {"status":"ok"}
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -fsS http://localhost:8000/health

## 20261103T034653-861cf08d61 / IF-0316
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0316
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring jobs API
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Spring jobs API
기대: 200 JSON
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -i http://localhost:8080/api/jobs

## 20261103T034653-861cf08d61 / IF-0317
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0317
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Frontend API 프록시
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Frontend API 프록시
기대: 200 JSON
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: curl -i http://localhost/api/jobs

## 20261103T034653-861cf08d61 / IF-0318
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0318
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 반복 재시작
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Spring 반복 재시작
기대: Restarting 반복 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps -a

## 20261103T034653-861cf08d61 / IF-0319
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0319
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Frontend 반복 재시작
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Frontend 반복 재시작
기대: Restarting 반복 없어야 함
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps -a

## 20261103T034653-861cf08d61 / IF-0320
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0320
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: CPU/메모리
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: CPU/메모리
기대: 자원 사용 측정·기준 정의
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker stats --no-stream

## 20261103T034653-861cf08d61 / IF-0321
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0321
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: OOMKilled
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: OOMKilled
기대: false; OOM이면 제한 조정
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker inspect if-app-stack-spring-1 --format "{{.State.OOMKilled}}"

## 20261103T034653-861cf08d61 / IF-0322
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0322
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 재생성 후 데이터 유지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 재생성 후 데이터 유지
기대: 동일 평가 유지
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose down; docker compose up -d --no-build

## 20261103T034653-861cf08d61 / IF-0323
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0323
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:52+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 볼륨 마운트
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 볼륨 마운트
기대: DB 영속 볼륨 존재
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker volume ls

## 20261103T034653-861cf08d61 / IF-0324
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0324
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 민감정보 출력
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 민감정보 출력
기대: API key/password 등 평문 미노출
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose logs --tail=100 spring fastapi

## 20261103T034653-861cf08d61 / IF-0325
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0325
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: FastAPI 정지
기대: Spring의 AI 오류/평가 상태 정책 검증
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop fastapi

## 20261103T034653-861cf08d61 / IF-0326
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0326
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Postgres 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Postgres 정지
기대: Spring 오류 처리·복구 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop postgres

## 20261103T034653-861cf08d61 / IF-0327
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0327
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 정지
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Spring 정지
기대: Nginx 실패 응답/재기동 확인
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose stop spring

## 20261103T034653-861cf08d61 / IF-0328
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0328
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: FastAPI 복구
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: FastAPI 복구
기대: AI 호출 복구
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose start fastapi

## 20261103T034653-861cf08d61 / IF-0329
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0329
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Spring 복구
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Spring 복구
기대: GET/POST 회복
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose start spring

## 20261103T034653-861cf08d61 / IF-0330
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0330
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 외부 노출 여부
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 외부 노출 여부
기대: 8000/8080 127.0.0.1 바인딩
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps

## 20261103T034653-861cf08d61 / IF-0331
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0331
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: DB 포트 노출
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DB 포트 노출
기대: 5432 호스트 미공개
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose ps postgres

## 20261103T034653-861cf08d61 / IF-0332
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0332
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 유효성
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Compose 유효성
기대: 오류 없이 종료
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose config --quiet

## 20261103T034653-861cf08d61 / IF-0333
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0333
- FEATURE_ID: FEAT-인프라
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:53+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: 이미지 빌드
- tool_a: Docker CLI + curl + 로그
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
- code_file: compose.yaml
- function: Docker Compose 컨테이너/네트워크/운영 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 이미지 빌드
기대: 각 서비스 이미지 성공
1차=NOT_RUN 2차=NOT_RUN 최종=NOT_RUN
입력: docker compose build

# pass

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0305
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: docker compose --env-file 빈 파일 config --quiet exit=1. stderr는 required variable IF_DB_PASSWORD is missing a value 이고 비밀번호 값은 없다. POSTGRES_PASSWORD: 는 설정 키 경로다. B: compose.yaml 의 ${IF_DB_PASSWORD:?}.

## 20261109T2305-349tc / IF-0306
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. 프로젝트 .env 존재=True, ai/.env 존재=True, compose config --quiet exit=0. Compose 기본 env는 프로젝트 루트 .env

## 20261109T2305-349tc / IF-0307
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. 호스트명 postgres로 틀린 비밀번호 exit=2, 인증실패문구=True

## 20261109T2305-349tc / IF-0308
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: lsof 8000 은 com.docke 가 127.0.0.1:8000 LISTEN. Docker 프로세스명이 잘려 docker 문자열 검사는 빗나갔고, 점유 주체는 Docker 다. B: compose 가 127.0.0.1:8000 을 연다.

## 20261109T2305-349tc / IF-0309
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: lsof 8080 은 com.docke 가 127.0.0.1:8080 LISTEN. B: compose 가 127.0.0.1:8080 을 연다.

## 20261109T2305-349tc / IF-0310
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: lsof 80 은 com.docke 가 *:80 LISTEN. B: compose frontend 는 80:80 으로 모든 인터페이스에 연다.

## 20261109T2305-349tc / IF-0311
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. network if-app-stack_default에 네 서비스 이름 포함=True

## 20261109T2305-349tc / IF-0312
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: 검사 시점 최근 50줄에 앞선 장애 주입의 host not found 가 남아 있었다. 같은 시점 frontend 는 running 이고 GET :80/api/jobs 는 200 이었다. B: nginx.conf proxy_pass http://spring:8080.

## 20261109T2305-349tc / IF-0313
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. spring 최근 50줄 UnknownHostException=False

## 20261109T2305-349tc / IF-0314
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. postgres 상태: if-app-stack-fastapi-1 Up 12 minutes

## 20261109T2305-349tc / IF-0315
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. GET :8000/health 200 {"status":"ok"}

## 20261109T2305-349tc / IF-0316
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. GET :8080/api/jobs 200 bytes=408

## 20261109T2305-349tc / IF-0317
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. GET :80/api/jobs 200 bytes=408

## 20261109T2305-349tc / IF-0318
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. spring RestartCount Status Restarting=0 running false

## 20261109T2305-349tc / IF-0319
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. frontend RestartCount Status Restarting=3 running false

## 20261109T2305-349tc / IF-0321
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. /if-app-stack-spring-1 OOMKilled=false | /if-app-stack-postgres-1 OOMKilled=false | /if-app-stack-fastapi-1 OOMKilled=false | /if-app-stack-frontend-1 OOMKilled=false

## 20261109T2305-349tc / IF-0322
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. down exit=0, up --no-build exit=0, assessment 2 before=2:AI_COMPLETED after=2:AI_COMPLETED

## 20261109T2305-349tc / IF-0323
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. volume if-app-stack_postgres-data

## 20261109T2305-349tc / IF-0324
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. 비밀번호 로그포함=False, GEMINI 설정됨=True, GEMINI 로그포함=False. 값은 기록하지 않음

## 20261109T2305-349tc / IF-0325
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A: fastapi 정지 후 POST HTTP 502 errorCode=AI_ERROR, message=AI 서버 호출에 실패했습니다. 응답에 id 는 없고 DB assessment 155 status=PENDING_AI. B: 서비스가 AI 실패를 502 로 두고 저장 상태는 PENDING_AI.

## 20261109T2305-349tc / IF-0326
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. postgres stop 후 jobs HTTP 500 body={"success":false,"data":null,"message":"서버 오류가 발생했습니다.","errorCode":"INTERNAL_ERROR"}; 복구 후 jobs=True

## 20261109T2305-349tc / IF-0327
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. spring stop 후 :80/api/jobs HTTP 502 nginx문구=True; 복구=True

## 20261109T2305-349tc / IF-0328
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. 시도 상태 [502, 502, 502, 0, 201]

## 20261109T2305-349tc / IF-0329
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. GET jobs 200, 빈 JSON POST 400 {"success":false,"data":null,"message":"chronicDisease: must not be null workHou, assessment count 7->7

## 20261109T2305-349tc / IF-0330
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. /if-app-stack-fastapi-1 {"8000/tcp":[{"HostIp":"127.0.0.1","HostPort":"8000"}]} | /if-app-stack-spring-1 {"8080/tcp":[{"HostIp":"127.0.0.1","HostPort":"8080"}]} | /if-app-stack-frontend-1 {"80/tcp":[{"HostIp":"","HostPort":"80"}]}. 80은 compose가 모든 인터페이스에 연다

## 20261109T2305-349tc / IF-0331
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. postgres PortBindings={}

## 20261109T2305-349tc / IF-0332
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. config --quiet exit=0

## 20261109T2305-349tc / IF-0343
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. 5동시 status=[201, 201, 201, 201, 201] ids=[165, 168, 166, 167, 164]

## 20261109T2305-349tc / IF-0346
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. throwaway postgres 복원 assessment 14 -> 14 pg_restore exit=0. 운영 볼륨은 교체하지 않음

## 20261109T2305-349tc / IF-0347
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. if-app-stack-fastapi-1 364.5MiB / 3.827GiB OOMKilled=false. mem_limit 없음

## 20261109T2305-349tc / IF-0349
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. restart 후 jobs=True POST 201 GET 200 DELETE 204 assessment 2 잔존=1

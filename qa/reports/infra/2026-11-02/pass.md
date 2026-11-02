# PASS

## 20261102T133209-b7e2c41d08 / IF-0305
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0305
- timestamp: 2026-11-02T13:32:09+09:00
- feature: IF_DB_PASSWORD 누락
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: env -u IF_DB_PASSWORD docker compose --env-file /tmp/if0305-empty.env config --quiet
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: POSTGRES_PASSWORD
- line: 15
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0305.err sha256=026b78cce7800cd90cac2ccbd2114a66738cfc90f7659a481859e69a2d8ffa1a; qa/.runtime/20261102T133209-b7e2c41d08/if0305.out sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 설정 단계가 실패하고 비밀번호 값은 나오지 않는다. 실제: exit 1. stderr는 required variable IF_DB_PASSWORD is missing a value: IF_DB_PASSWORD_not_set. stdout은 비어 있고 비밀번호 값은 없다. 루트 .env를 피하려고 빈 env 파일을 지정했다. 렌더된 설정은 저장하지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0306
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0306
- timestamp: 2026-11-02T13:32:09+09:00
- feature: .env 경로
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: pwd; ls -la .env ai/.env
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml,.env
- function: name
- line: 7
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0306.txt sha256=2857420bd96c5d306beb9c6fe38a175bcc6123a29c2c33f0b71a9a9c5df46b9a; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Compose 루트 파일을 확인한다. 실제: pwd는 저장소 루트다. .env와 ai/.env가 둘 다 있다. Compose 기본 env 파일은 프로젝트 디렉터리의 .env다. 파일 내용은 출력하지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0307
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0307
- timestamp: 2026-11-02T13:32:09+09:00
- feature: DB 비밀번호 불일치
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: psql -h postgres -U if_user -d if_spring
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: POSTGRES_PASSWORD
- line: 15
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0307-net-wrong.err sha256=884f4e5f5276775e612b90e0f344a9e2f7c68ce1cdb296c39e78deac8639b496; qa/.runtime/20261102T133209-b7e2c41d08/if0307-net-match.out sha256=5ab76041d4a6b192273d0fb6d5eb18a9feb23c133eb8b2056c03c20f22837cc0; qa/.runtime/20261102T133209-b7e2c41d08/if0307-hba.txt sha256=cda346512501b56342174d2856343f8be88bf27cd061ed5d932feea395038d03; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 비밀번호가 다르면 인증이 실패한다. 볼륨 비밀번호는 바꾸지 않았다. 컨테이너 안 127.0.0.1은 pg_hba가 trust라 틀린 비밀번호도 select 1이 되었다. 다시 측정한 네트워크 주소 172.25.0.4는 scram-sha-256이다. 주입된 POSTGRES_PASSWORD로는 ok. 다른 비밀번호는 password authentication failed, exit 2. .env 값은 출력하지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0308
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0308
- timestamp: 2026-11-02T13:32:09+09:00
- feature: FastAPI 8000 점유
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker ps --format "{{.Names}} {{.Ports}}"
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: ports
- line: 51
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0308.txt sha256=2f6885b42dcdd6cb6084283b09b137a0506e9b14c015609d0a2b52f51d8573b8; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 8000을 연 컨테이너를 찾는다. 실제: if-app-stack-fastapi-1이 127.0.0.1:8000->8000이다. 다른 프로세스는 죽이지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0309
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0309
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Spring 8080 점유
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: lsof -nP -iTCP:8080 -sTCP:LISTEN
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: ports
- line: 31
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0309.txt sha256=a0d188bb9333ae83baafdb48950d13aaf4f94f8557d8f9a4ff715aa496cb6278; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 8080 LISTEN PID를 확인한다. 실제: com.docke PID 88459가 127.0.0.1:8080을 연다. 컨테이너는 if-app-stack-spring-1이다. 프로세스는 죽이지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0310
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0310
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Nginx 80 점유
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: lsof -nP -iTCP:80 -sTCP:LISTEN
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml,web-vite/nginx.conf
- function: listen
- line: 5
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0310.txt sha256=9fdf03d10fff36b1a5f4041448e1cb3c431eec098c0e2416f3fea7e4180d3044; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 80 LISTEN PID를 확인한다. 실제: com.docke PID 88459가 *:80을 연다. 컨테이너는 if-app-stack-frontend-1이다. 프로세스는 죽이지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0311
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0311
- timestamp: 2026-11-02T13:32:09+09:00
- feature: spring에서 postgres 이름
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker network inspect if-app-stack_default
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: SPRING_DATASOURCE_URL
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0311-names.txt sha256=5b15446e4508cb4cc7902027653f3e632832632eb6ed78f87094e4145b2d69aa; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 같은 네트워크와 서비스 이름을 확인한다. 실제: postgres, spring, fastapi, frontend 컨테이너가 if-app-stack_default에 함께 있다. JDBC 호스트는 postgres다.

## 20261102T133209-b7e2c41d08 / IF-0312
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0312
- timestamp: 2026-11-02T13:32:09+09:00
- feature: nginx에서 spring 이름
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose logs --tail=50 frontend
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: web-vite/nginx.conf
- function: proxy_pass
- line: 16
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0312.txt sha256=69d9648341acfef2bc519b30f1d7dda6826dcdd114643e0c1ca0d3e2584fd432; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: host not found가 없다. 실제: frontend 최근 50줄에 host not found와 could not be resolved가 없다. nginx는 spring:8080으로 프록시한다.

## 20261102T133209-b7e2c41d08 / IF-0313
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0313
- timestamp: 2026-11-02T13:32:09+09:00
- feature: spring에서 fastapi 이름
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose logs --tail=50 spring
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml,AIClient.java
- function: analyze
- line: 38
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0313.txt sha256=854677af468a8eca9a5d67f30de2395afe765e3b083e182552695aaccc3ccae7; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 정상 구간의 로그에 UnknownHostException이 없다. 실제: 장애 주입 전 spring 최근 50줄에 없다. AI 주소는 http://fastapi:8000. 시작 직후 잠깐의 이름 오류는 IF-0328에 적었다.

## 20261102T133209-b7e2c41d08 / IF-0314
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0314
- timestamp: 2026-11-02T13:32:09+09:00
- feature: PostgreSQL healthcheck
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose ps
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: healthcheck
- line: 18
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0314.txt sha256=027bacef57fd1f34903336fa1fe3f0c5b4562da2cd02203d40991254ca58edf9; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: postgres가 Up (healthy)다. 실제: Up (healthy). healthcheck는 pg_isready -U if_user -d if_spring.

## 20261102T133209-b7e2c41d08 / IF-0315
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0315
- timestamp: 2026-11-02T13:32:09+09:00
- feature: FastAPI health
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: curl -fsS http://127.0.0.1:8000/health
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: ai/src/main.py
- function: health
- line: 44
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0315.txt sha256=a29ee2b15c494311c52521766e44af56a3ad2248e7a8ab465e5206463c13d288; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: {"status":"ok"}. 실제: {"status":"ok"}.

## 20261102T133209-b7e2c41d08 / IF-0316
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0316
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Spring jobs API
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: curl -i http://127.0.0.1:8080/api/jobs
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: JobController.java
- function: list
- line: 27
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0316.hdr sha256=c3d7a50ba0cbf353d7ece3701a08a798e5b4d4cdfcabb83087045070899619df; qa/.runtime/20261102T133209-b7e2c41d08/if0316.body sha256=9177b7c73358d6b111ef7ff69e35b4cf7413396090144893eee5312a19322335; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 200 JSON. 실제: HTTP 200, 본문은 JSON 배열이다.

## 20261102T133209-b7e2c41d08 / IF-0317
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0317
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Frontend API 프록시
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: curl -i http://127.0.0.1/api/jobs
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: web-vite/nginx.conf
- function: proxy_pass
- line: 16
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0317.hdr sha256=4e428380f51a82d8e32946b87c4e4845a88a43930d5312eeb3425837ef500be0; qa/.runtime/20261102T133209-b7e2c41d08/if0317.body sha256=9177b7c73358d6b111ef7ff69e35b4cf7413396090144893eee5312a19322335; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 200 JSON. 실제: HTTP 200, 본문은 JSON 배열이다. nginx가 /api/를 spring:8080으로 넘긴다.

## 20261102T133209-b7e2c41d08 / IF-0318
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0318
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Spring 반복 재시작
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose ps -a; docker inspect RestartCount
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: restart
- line: 44
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0318-inspect.txt sha256=bf900de0fb16be0a7ee8ae9dee006833fd1809eccbc2e55f895cd0bb99fb5206; qa/.runtime/20261102T133209-b7e2c41d08/if0318.txt sha256=027bacef57fd1f34903336fa1fe3f0c5b4562da2cd02203d40991254ca58edf9; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Restarting 반복이 없다. 실제: 장애 주입 전 상태는 running, RestartCount 0. ps에 Restarting이 없다. restart 정책은 unless-stopped.

## 20261102T133209-b7e2c41d08 / IF-0319
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0319
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Frontend 반복 재시작
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose ps -a; docker inspect RestartCount
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: restart
- line: 64
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0319-inspect.txt sha256=bf900de0fb16be0a7ee8ae9dee006833fd1809eccbc2e55f895cd0bb99fb5206; qa/.runtime/20261102T133209-b7e2c41d08/if0318.txt sha256=027bacef57fd1f34903336fa1fe3f0c5b4562da2cd02203d40991254ca58edf9; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Restarting 반복이 없다. 실제: 장애 주입 전 상태는 running, RestartCount 0. frontend 줄에 Restarting이 없다.

## 20261102T133209-b7e2c41d08 / IF-0320
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0320
- timestamp: 2026-11-02T13:32:09+09:00
- feature: CPU와 메모리
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker stats --no-stream
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: services
- line: 9
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0320.txt sha256=62a21da041d715811ecc3bc0080d1864653292df532875c50516a3b6e3097f14; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

수적 목표는 compose에 없다. 측정값: spring 0.26% 305.2MiB / 3.827GiB, postgres 0.00% 65.58MiB / 3.827GiB, fastapi 0.65% 294.3MiB / 3.827GiB, frontend 0.00% 13.32MiB / 3.827GiB. 같은 호스트의 다른 컨테이너도 함께 찍혔다. 제한은 바꾸지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0321
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0321
- timestamp: 2026-11-02T13:32:09+09:00
- feature: OOMKilled
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker inspect if-app-stack-spring-1 --format "{{.State.OOMKilled}}"
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: spring
- line: 25
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0321.txt sha256=2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: false. 실제: false. 메모리 제한은 조정하지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0322
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0322
- timestamp: 2026-11-02T13:32:09+09:00
- feature: 재생성 후 데이터 유지
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose down; docker compose up -d --no-build
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: postgres-data
- line: 17
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0322-compare.txt sha256=7b6f5b6e8c9da25a0f2cbca1fd7d6910419da565f9e1822b54a1cd72b580fc3c; qa/.runtime/20261102T133209-b7e2c41d08/if0322-down.txt sha256=67dc39d44f7193dd6865d95ffba2bd47f860a4dfdfd19dfadce5adf2eab8be58; qa/.runtime/20261102T133209-b7e2c41d08/if0322-up.txt sha256=b67840c45214228a336152c451179c92c76136468c335a822b9c1e9f2e786407; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 같은 평가가 남는다. -v는 쓰지 않았다. 재생성 전후 목록은 둘 다 2 AI_COMPLETED. GET /api/jobs는 200. assessment_id 2는 지우지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0323
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0323
- timestamp: 2026-11-02T13:32:09+09:00
- feature: 볼륨 마운트
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker volume ls
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: postgres-data
- line: 67
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0323.txt sha256=cc44290b365d0eea8b02fd74d1e4dc4a74db1d0af1ef46ed958e89fe060933ab; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: DB 영속 볼륨이 있다. 실제: if-app-stack_postgres-data.

## 20261102T133209-b7e2c41d08 / IF-0324
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0324
- timestamp: 2026-11-02T13:32:09+09:00
- feature: 로그 민감정보
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose logs --tail=100 spring fastapi
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: IF_DB_PASSWORD
- line: 15
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0324-hits.txt sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/20261102T133209-b7e2c41d08/if0324.txt sha256=20c5bece62f9fb717feb0570bce4196835e26924f6107d161bf393963408dbd2; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: API 키와 비밀번호 평문이 없다. 실제: 최근 100줄에서 비밀번호 값, GEMINI 키 값, IF_DB_PASSWORD=, POSTGRES_PASSWORD=, SPRING_DATASOURCE_PASSWORD= 가 없다. 값은 보고서에 적지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0325
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0325
- timestamp: 2026-11-02T13:32:09+09:00
- feature: FastAPI 정지
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose stop fastapi
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: AssessmentService.java,AIClient.java
- function: createAndAnalyze
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0325-summary.txt sha256=9d302b46787a6fa7e882b58377305c4d72770f641e32ebd50cdc6eaaf7b76cec; qa/.runtime/20261102T133209-b7e2c41d08/if0325.body sha256=5817c19814f37f6e30df34b91d5466ea0e02c2f499cb6813667a4718a27fa944; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Spring의 AI 오류와 평가 상태를 본다. 실제: POST /api/assessments는 502, errorCode AI_ERROR. DB 상태는 PENDING_AI. 저장은 AI 호출 전이라 롤백되지 않는다. 이 프로브 행은 나중에 지웠다.

## 20261102T133209-b7e2c41d08 / IF-0326
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0326
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Postgres 정지
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose stop postgres
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: GlobalExceptionHandler.java
- function: handleUnexpected
- line: 49
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0326-re.hdr sha256=97dc968aa4a98a8627338529cb9e9d42db99b77c5a5ea93729d839384bbbb6bf; qa/.runtime/20261102T133209-b7e2c41d08/if0326-re.body sha256=d5446d108e3fcd09e741478e17bf577f4ba3e73bd6f3ebe99259f84ea466551f; qa/.runtime/20261102T133209-b7e2c41d08/if0326-summary.txt sha256=eb154230d4fde34c03f578c3fe53d6d9702444f310dd48f1319489b159f80e75; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Spring 오류와 복구를 본다. 20초 curl은 HTTP 상태를 받지 못했다. 45초로 다시 측정하면 GET /api/jobs는 500, 본문은 INTERNAL_ERROR, 메시지 서버 오류가 발생했습니다. postgres를 다시 시작한 뒤 healthy가 되고 GET /api/jobs는 200. assessment_id 2는 AI_COMPLETED로 남았다.

## 20261102T133209-b7e2c41d08 / IF-0327
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0327
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Spring 정지
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose stop spring
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: web-vite/nginx.conf
- function: proxy_pass
- line: 16
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0327-re.hdr sha256=c91b9495e46fd776b276a85b7c7fe8f044a2b422aadea6d60f27af500b2066c0; qa/.runtime/20261102T133209-b7e2c41d08/if0327-re.body sha256=069a19dd1f7d5afcb6614df8b8bafa7304145c8bb5f29a36331e96b91413600a; qa/.runtime/20261102T133209-b7e2c41d08/if0327.curl sha256=65e1b753f0b71b15c4efdd033a2431014f10d67e8d9ae80c170945106b70e47e; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: Nginx 실패 응답과 재기동을 본다. 10초 curl은 0바이트로 시간 초과했다. Nginx proxy_connect_timeout 기본값은 60초다. 75초로 다시 측정하면 HTTP 502 Bad Gateway, nginx/1.30.6. spring을 다시 시작한 뒤 GET /api/jobs는 200.

## 20261102T133209-b7e2c41d08 / IF-0328
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0328
- timestamp: 2026-11-02T13:32:09+09:00
- feature: FastAPI 복구
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose start fastapi
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: AIClient.java,AssessmentController.java
- function: create
- line: 56
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0328-re-attempts.txt sha256=63e9e1d64441025e833c5b5ace168d9858a8cd53a06b452dffc37959862f22e9; qa/.runtime/20261102T133209-b7e2c41d08/if0328-re-spring.log sha256=038039489ea8408108e20bad1f1a0f6ba28d0cbb30b44f35ba375c4793221276; qa/.runtime/20261102T133209-b7e2c41d08/if0328-re-health.txt sha256=a29ee2b15c494311c52521766e44af56a3ad2248e7a8ab465e5206463c13d288; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: AI 호출이 회복된다. /health는 {"status":"ok"}. 시작 직후 POST 세 번은 502다. spring 로그 원인은 UnknownHostException: fastapi. 네 번째 POST는 201이고 본문에 id가 있다. 컨트롤러 성공 코드는 201이다. 만든 평가는 삭제했다. 첫 단일 POST만 본 실행은 502였다.

## 20261102T133209-b7e2c41d08 / IF-0329
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0329
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Spring 복구
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose start spring
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: AssessmentController.java
- function: create
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0329.hdr sha256=6ac84add71859b901a7040b6d7b2dcd16895f7362cd73ba3d9b0d24a5a078517; qa/.runtime/20261102T133209-b7e2c41d08/if0329.body sha256=71daa9802d1392845dcf8242c24b6f3f9c9de23b78c149d31601baee55868642; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: GET과 POST가 다시 응답한다. 실제: GET /api/jobs 200. 빈 JSON POST /api/assessments는 400. 검증에서 거절되어 행이 추가되지 않았다.

## 20261102T133209-b7e2c41d08 / IF-0330
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0330
- timestamp: 2026-11-02T13:32:09+09:00
- feature: 8000과 8080 바인딩
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose ps
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: ports
- line: 31
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0330.txt sha256=027bacef57fd1f34903336fa1fe3f0c5b4562da2cd02203d40991254ca58edf9; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 8000과 8080이 127.0.0.1에만 열린다. 실제: 127.0.0.1:8000->8000, 127.0.0.1:8080->8080. frontend 80:80은 이 케이스의 판정에 넣지 않았다. 80은 모든 인터페이스에 열린다.

## 20261102T133209-b7e2c41d08 / IF-0331
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0331
- timestamp: 2026-11-02T13:32:09+09:00
- feature: DB 포트 노출
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose ps postgres
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: postgres
- line: 10
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0331.txt sha256=8cdea68b36e70fcdebc19c920518db1f206720d3ecc6734f950580dbc483e7c0; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 5432가 호스트에 공개되지 않는다. 실제: 포트 칸은 5432/tcp만 있다. 호스트 바인딩은 없다.

## 20261102T133209-b7e2c41d08 / IF-0332
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0332
- timestamp: 2026-11-02T13:32:09+09:00
- feature: Compose 유효성
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose config --quiet
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: PASS
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: compose.yaml
- function: IF_DB_PASSWORD
- line: 15
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0332.out sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/20261102T133209-b7e2c41d08/if0332.err sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 비밀번호가 있으면 오류 없이 끝난다. 실제: exit 0, stdout은 비어 있다. 렌더된 설정은 저장하지 않았고 비밀번호 값은 출력하지 않았다.

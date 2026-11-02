# FAIL

## 20261102T133209-b7e2c41d08 / IF-0333
- RUN_ID: 20261102T133209-b7e2c41d08
- TC_ID: IF-0333
- timestamp: 2026-11-02T13:32:09+09:00
- feature: 이미지 빌드
- test_type: infra
- tool_a: Docker CLI + curl + 로그
- command_a: docker compose build
- result_a: FAIL
- tool_b: 소스 대조
- command_b: read compose.yaml web-vite/nginx.conf AIClient.java AssessmentService.java
- result_b: PASS
- status: FAIL
- git_commit: 7d72400cf420dc5eae07c0fa98ddaf390b816f64
- dirty: True
- files: spring/Dockerfile,ai/Dockerfile,web-vite/Dockerfile
- function: FROM
- line: 2
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T133209-b7e2c41d08/if0333-build.log sha256=1d6daefdf5c43a083750f294ad38b5826d83bf873e63c5be5d77b34110b6187f; qa/.runtime/20261102T133209-b7e2c41d08/if0333-build-retry.log sha256=26b54221f4a8abd14b3951a383cc7b8955fc81e9b77a77f0b9ff48282931a67a; qa/.runtime/20261102T133209-b7e2c41d08/source-review.txt sha256=f147abf5a610bc11cc71852cd68a17010a18876c56b91b45ef5836e18fc270b5

기대: 각 서비스 이미지가 빌드된다. 실제: 두 번 모두 exit 1. BuildKit이 docker/dockerfile:1, node:24-alpine, nginx:stable-alpine 메타데이터에서 DeadlineExceeded. Dockerfile의 RUN까지 가지 않았다. 기존 if-spring:local, if-fastapi:local, if-frontend:local은 3일 전 이미지 그대로다. 실행 중인 컨테이너는 바꾸지 않았다.

Expected: docker compose build가 spring, fastapi, frontend 이미지를 만든다.
Actual: 1차 BUILD_EXIT 1, 2차 BUILD_EXIT 1. 이미지 ID는 빌드 전과 같다. if-spring:local 726eb439c7ce, if-fastapi:local 3d41e2bbf1d1, if-frontend:local fd2c77bb28b8. 생성 시각은 3일 전이다.
Input: 저장소 루트에서 docker compose build. 캐시를 지우지 않았다.
Error: DeadlineExceeded: context deadline exceeded. 1차는 dockerfile:1, nginx:stable-alpine, node:24-alpine. 2차는 node:24-alpine과 dockerfile:1. nginx 메타데이터는 CANCELED.
Repro: docker compose build
Cause: BuildKit이 베이스 이미지 메타데이터를 기한 안에 받지 못했다. 호스트의 registry-1.docker.io 조회는 401과 0.6초였다. 빌드는 Dockerfile 명령 실행 전에 멈췄다.
Location: web-vite/Dockerfile 2행 FROM node:24-alpine. spring/Dockerfile 1행과 ai/Dockerfile 1행은 # syntax=docker/dockerfile:1. 수정하지 않음. 재검증은 같은 RUN의 2차 빌드이며 역시 FAIL.

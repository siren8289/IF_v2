# RISK

## 20261102T182447-n4f8a21c06
- IF-0345는 FAIL이다. 새 RISK ID는 만들지 않았다. scripts/qa/run.py가 없어 risks.json에도 넣지 않았다.
- 원인 위치는 web-vite/nginx.conf 16행과 compose.yaml frontend 57-64행이다. frontend는 spring에 의존한다고 적혀 있지 않다. 제품 코드는 수정하지 않았다.
- IF-0342, IF-0344, IF-0348은 BLOCKED다. 측정은 했고 통과로 두지 않았다.
- IF-0342 ab p50 6ms, p95 68ms, 최대 1025ms. python p50 4.1ms, p95 12.8ms, 최대 50.8ms. 30건 모두 성공. 합격 SLO는 없다. 2026-10-30 PERF-001의 500ms는 이 시트의 기준이 아니다.
- IF-0344 읽기 제한은 40초, 연결 제한은 3초다. 15초 mock은 201과 15.139초였다. 15초를 실패로 보는 기준은 없다.
- IF-0348 평가 114의 Spring 로그와 FastAPI 로그에 공통 식별자가 없다. 성공 경로는 요청 ID를 남기지 않는다.
- IF-0343 다섯 건은 201과 AI_COMPLETED로 맞았다. IF-0346 임시 복구 건수는 원본과 같다. IF-0347 OOMKilled는 false, 메모리 339.2MiB다. IF-0349 재시작 뒤 POST 201, GET 200, DELETE 204다.
- 평가 2는 AI_COMPLETED다. IF034로 만든 행과 신청자는 지웠다. 임시 Postgres와 15초 mock은 삭제했다. 운영 볼륨은 덮어쓰지 않았다.
- 마지막 상태: fastapi, frontend, postgres healthy, spring이 Up이다.
- 공식 게이트 scripts/qa/run.py는 실행하지 않았다. 이 기록은 QA 통과가 아니다.
- RISK-SEC-001, RISK-LEGACY-FAILS, RISK-QA-AUTH는 이 실행에서 다시 검증하지 않았다.
- .github/workflows/githubactions.yml 수정은 이 검사의 변경이 아니다. dirty는 True다.

# 판정 보류

상태는 BLOCKED다. FAIL이 아니고 PASS도 아니다. 합격 기준이 없는 측정이다.

## 20261102T182447-n4f8a21c06 / IF-0342
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0342
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 직무 조회 응답시간
- test_type: nonfunctional
- tool_a: ab
- command_a: ab -n 30 -c 1 http://127.0.0.1:8080/api/jobs
- result_a: BLOCKED
- tool_b: python urllib
- command_b: GET /api/jobs 30회 perf_counter
- result_b: BLOCKED
- status: BLOCKED
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: JobController.java
- function: list
- line: 27
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0342-ab.txt sha256=2561763494681f610582a8e97afc1768e11da254f59c1c1e46dcbeb5d07e9ff2; qa/.runtime/20261102T182447-n4f8a21c06/if0342-python.json sha256=bffbcc5904dcadfde458a6f2926f3bbbc4bea98cef19755bf231f0508e8179f8; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: p50과 p95를 재고, 합격 SLO는 정해져 있지 않다. 미정책은 통과가 아니다. 실제: ab 30건 실패 0, p50 6ms, p95 68ms, 최대 1025ms. python 30건 모두 200, p50 4.1ms, p95 12.8ms, 최대 50.8ms. 두 표본의 백분위가 다르다. 과거 PERF-001의 500ms 기준은 이 시트에 없다. 판정 보류.

## 20261102T182447-n4f8a21c06 / IF-0344
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0344
- timestamp: 2026-11-02T18:24:47+09:00
- feature: AI 응답 지연
- test_type: nonfunctional
- tool_a: 지연 mock
- command_a: fastapi 정지 후 15초 응답 mock으로 POST /api/assessments
- result_a: BLOCKED
- tool_b: 소스 대조
- command_b: read AppConfig.java AIClient.java
- result_b: BLOCKED
- status: BLOCKED
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: AppConfig.java
- function: restTemplate
- line: 21
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0344-meta.txt sha256=a03ea9e392fc7d0d99751aff2d9a1f7617cd290690ec542b7cbffa5e0bad0924; qa/.runtime/20261102T182447-n4f8a21c06/if0344.body sha256=77f1b46c61d1dc279a116ecc3d0df032eed2543b4c076704630cedf177e53fe5; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: 타임아웃 정책을 확인한다. 15초를 실패로 볼 합격 기준은 없다. 실제: 연결 제한 3초, 읽기 제한 40초. 15초 mock은 HTTP 201, 15.139초, DB 상태 AI_COMPLETED. 40초 읽기 제한은 걸리지 않았다. mock 컨테이너는 지우고 fastapi를 다시 시작했다. 판정 보류.

## 20261102T182447-n4f8a21c06 / IF-0348
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0348
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 로그 추적
- test_type: nonfunctional
- tool_a: Docker logs
- command_a: POST /api/assessments 1회 후 docker compose logs --since 3m spring fastapi
- result_a: BLOCKED
- tool_b: 소스 대조
- command_b: read AIClient.java ai/src/main.py
- result_b: BLOCKED
- status: BLOCKED
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: AIClient.java,ai/src/main.py
- function: analyze
- line: 36
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0348-hits.txt sha256=8994aaa096b0ef89a3ddcf4ad66708fc266b9cc1fbd0d1956d05a1d1bfff51dc; qa/.runtime/20261102T182447-n4f8a21c06/if0348.hdr sha256=cd9057abb0e28f43e1447351ca80e54ebc4cb6bf08883828120e06aca1e12344; qa/.runtime/20261102T182447-n4f8a21c06/if0348-logs.txt sha256=964dacc83a3ab6ceea67bbbb92b437bd09d7ddd34ea7f4e65c26cb35ae2dbede; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: Spring과 AI 로그를 같은 요청으로 묶을 수 있는지 본다. 식별자를 의무로 하는 정책은 없다. 실제: POST는 평가 114를 만들었다. 최근 로그에 이름 IF0348probe, 평가 번호, X-Request-Id, traceId, correlation이 없다. 성공 경로에 공통 식별자 로그가 없다. 114는 삭제했다. 판정 보류.

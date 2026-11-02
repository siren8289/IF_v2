# FAIL

## 20261102T182447-n4f8a21c06 / IF-0345
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0345
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 서비스 시작 순서
- test_type: nonfunctional
- tool_a: Docker CLI + curl
- command_a: docker compose stop spring frontend; docker compose start frontend
- result_a: FAIL
- tool_b: 소스 대조
- command_b: read web-vite/nginx.conf compose.yaml https://docs.docker.com/compose/how-tos/startup-order/
- result_b: FAIL
- status: FAIL
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: web-vite/nginx.conf,compose.yaml
- function: proxy_pass
- line: 16
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0345-ps.txt sha256=88265f1de2e85e80ccfaf62a2106db34976bda057854f4be3fb24f4bf61c78da; qa/.runtime/20261102T182447-n4f8a21c06/if0345-meta.txt sha256=2b98ac3c1342883c1afdbe85b58266aaa4c4a3dcfa6e396d25fdd5387eb19056; qa/.runtime/20261102T182447-n4f8a21c06/if0345-frontend.log sha256=3e2aaf58f7052ae3533d68638b7c2a700adb232ab0e13d7e757d30391fe5e054; qa/.runtime/20261102T182447-n4f8a21c06/if0345-api.curl sha256=f53c0f3130b03f9b3bc724e9eccd9abfca1bc6e6863f680544a05706bba1b4b9; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: Spring보다 먼저 frontend를 띄웠을 때 Nginx crash loop 여부를 본다. 실제: RestartCount 6에서 7, 상태 Restarting (1). 80번 연결이 거절됐다. 로그는 host not found in upstream "spring" in /etc/nginx/conf.d/default.conf:16. frontend에는 depends_on이 없다. Spring을 다시 시작한 뒤 GET /api/jobs는 200이었고, 마지막에는 네 서비스가 Up이다.

Expected: Spring이 꺼진 동안 frontend를 시작해도 Nginx 프로세스가 반복 종료되지 않는지 확인한다.
Actual: if-app-stack-frontend-1 상태가 Restarting (1)이다. RestartCount는 6에서 7이 됐다. curl 127.0.0.1:80은 연결이 거절됐다. Spring을 다시 시작한 뒤 GET /api/jobs는 200이다.
Input: docker compose stop spring frontend 다음 docker compose start frontend. 12초 대기.
Error: nginx: [emerg] host not found in upstream "spring" in /etc/nginx/conf.d/default.conf:16
Repro: docker compose stop spring frontend && docker compose start frontend && docker compose ps -a
Cause: proxy_pass http://spring:8080 은 기동 시 이름을 해석한다. Spring 컨테이너가 없으면 Docker DNS에 spring이 없다. compose.yaml frontend에는 depends_on이 없다. Docker Compose 시작 순서는 depends_on이 있을 때만 맞춘다.
Location: web-vite/nginx.conf proxy_pass 16행. compose.yaml frontend 57-64행. 수정하지 않음. 재검증 RUN_ID 없음.

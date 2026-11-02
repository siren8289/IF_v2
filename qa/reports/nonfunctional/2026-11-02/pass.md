# PASS

## 20261102T182447-n4f8a21c06 / IF-0343
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0343
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 평가 동시 요청
- test_type: nonfunctional
- tool_a: python ThreadPoolExecutor
- command_a: POST /api/assessments 5건 동시
- result_a: PASS
- tool_b: SQL
- command_b: select assessment_id, status, display_name where display_name like IF0343%
- result_b: PASS
- status: PASS
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: AssessmentService.java
- function: createAndAnalyze
- line: 86
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0343.json sha256=cdb6a6ef9e675987c6e398af116a86312e9d10ce02d84c578dc32560cc2fa431; qa/.runtime/20261102T182447-n4f8a21c06/if0343-db.txt sha256=51854ea705da8d2c76fd66d9bfb9c7cfbad9c42f73062b981e5c2865e3699a78; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: 2~5명이 정상 등록되고 행이 맞으며 중복이 없다. 실제: IF0343a~e 다섯 요청 모두 HTTP 201. DB는 115~119, 모두 AI_COMPLETED, 이름이 한 번씩이다. 같은 assessment_id는 없다. 검사 행은 API DELETE 204 뒤 신청자와 건강 스냅샷까지 지웠다. 평가 2는 남았다.

## 20261102T182447-n4f8a21c06 / IF-0346
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0346
- timestamp: 2026-11-02T18:24:47+09:00
- feature: DB 복원
- test_type: nonfunctional
- tool_a: pg_dump + psql
- command_a: pg_dump 후 임시 Postgres에 복구
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml volumes
- result_b: PASS
- status: PASS
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: compose.yaml
- function: postgres-data
- line: 17
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0346-meta.txt sha256=f5486c274819bd542d3e3211067886030cd77d52913ddd685a30ce8e66766056; qa/.runtime/20261102T182447-n4f8a21c06/if0346-source.txt sha256=dd5c160687a3d2af23203f7b9e6da5568f6c81ad1a28a8037d49027c0694dd76; qa/.runtime/20261102T182447-n4f8a21c06/if0346-restored.txt sha256=dd5c160687a3d2af23203f7b9e6da5568f6c81ad1a28a8037d49027c0694dd76; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: 테스트 DB 복구 결과가 원본과 같다. 운영 볼륨은 바꾸지 않았다. 실제: dump exit 0, 임시 서버 restore exit 0. 원본과 복구 모두 assessment 1, applicant 21, job 8, 평가 2는 AI_COMPLETED. 임시 컨테이너 if0346-restore는 삭제했다. Compose에는 백업 스케줄이 없고, 이 결과는 그 스케줄의 통과가 아니다. 일관성 비교 자체는 맞다.

## 20261102T182447-n4f8a21c06 / IF-0347
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0347
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 모델 메모리
- test_type: nonfunctional
- tool_a: Docker CLI
- command_a: docker compose restart fastapi; analyze; docker stats; docker inspect OOMKilled
- result_a: PASS
- tool_b: 소스 대조
- command_b: read compose.yaml fastapi
- result_b: PASS
- status: PASS
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: compose.yaml,ai/src/main.py
- function: analyze
- line: 50
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0347-oom.txt sha256=451ae1dc6e5e163ca19cd59255490d5620574e5839d361f5c94abb671a0459f0; qa/.runtime/20261102T182447-n4f8a21c06/if0347-stats.txt sha256=7c3ae13353b0acd766109eabaf6c74db624ae15edb5026ac080489dc026254cd; qa/.runtime/20261102T182447-n4f8a21c06/if0347-analyze.hdr sha256=3175c89b63c8fb8451c3ceaf52926d6545c0b9f63ca7e0f722b920001a343c89; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: OOM이 없고 자원 값을 남긴다. 메모리 상한 숫자는 없다. 실제: analyze HTTP 200. OOMKilled=false, 상태 running, RestartCount 0. 메모리 339.2MiB / 3.827GiB, CPU 2.30%. compose fastapi에는 mem_limit가 없다.

## 20261102T182447-n4f8a21c06 / IF-0349
- RUN_ID: 20261102T182447-n4f8a21c06
- TC_ID: IF-0349
- timestamp: 2026-11-02T18:24:47+09:00
- feature: 장애 이후 회귀
- test_type: nonfunctional
- tool_a: curl
- command_a: docker compose restart 후 POST GET DELETE
- result_a: PASS
- tool_b: 소스 대조
- command_b: read AssessmentController.java
- result_b: PASS
- status: PASS
- git_commit: c01e021a9e715bedc9e25b864a71f3b666743761
- dirty: True
- files: AssessmentController.java
- function: create
- line: 56
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T182447-n4f8a21c06/if0349-meta.txt sha256=4583a72c9fe6353ff291e158dc6a7f5b1884ab22fc7f7285ea1fba0e82985394; qa/.runtime/20261102T182447-n4f8a21c06/if0349-post.txt sha256=aed7996d3054f25c7138048acbb36db65f4c872ff0f7c8a91447a35d9081fc30; qa/.runtime/20261102T182447-n4f8a21c06/if0349-get.hdr sha256=c12c9ff6fd3ae05fa733b13fecf882202183f08746e3762c223cde3f43f20e32; qa/.runtime/20261102T182447-n4f8a21c06/source-review.txt sha256=62cfdcf7ad4533338a85783a116a25b144f6418f24ca52f1567afa3463a01f61

기대: 재시작 뒤 핵심 시나리오가 된다. 실제: postgres healthy 이후 GET /api/jobs 200. POST /api/assessments 201, id 121. GET /api/assessments/121/result 200. DELETE 204. 프로브 신청자는 0이고 남은 평가는 2 AI_COMPLETED다.

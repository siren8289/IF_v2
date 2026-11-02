# RISK

## 20261102T133209-b7e2c41d08
- IF-0333은 FAIL이다. 새 RISK ID는 만들지 않았다.
- 원인 위치는 BuildKit 메타데이터 단계다. web-vite/Dockerfile 2행, spring/Dockerfile 1행, ai/Dockerfile 1행이 요청한 이미지를 기한 안에 풀지 못했다. 제품 Dockerfile은 수정하지 않았다.
- 실행 중인 네 컨테이너는 빌드 실패 뒤에도 Up이다. postgres는 healthy다. GET /api/jobs 200, GET /health status ok, nginx /api/jobs 200.
- assessment_id 2는 AI_COMPLETED로 남았다. 이름 IF0305probe로 만든 평가 109부터 113은 API DELETE 204로 지웠다. 남은 신청자와 건강 스냅샷도 그 이름으로만 지웠다. 남은 프로브 신청자는 0이다.
- docker compose down은 볼륨 삭제 없이 실행했다.
- 127.0.0.1 pg_hba는 trust다. 비밀번호 불일치 판정은 컨테이너 네트워크의 scram-sha-256으로 다시 했다. 볼륨 비밀번호는 바꾸지 않았다.
- FastAPI를 다시 시작한 직후 spring은 UnknownHostException: fastapi로 502를 세 번 냈고, 네 번째 POST는 201이었다.
- Postgres가 멈춘 동안 20초 curl은 HTTP 상태를 받지 못했다. 45초 재측정은 500 INTERNAL_ERROR다. 내부 문장은 응답에 없다.
- Spring이 멈춘 동안 10초 curl은 0바이트로 끝났다. 75초 재측정은 nginx 502다.
- frontend 80:80은 0.0.0.0에 열린다. IF-0330은 8000과 8080만 본다. 새 RISK ID는 만들지 않았다.
- CPU와 메모리 숫자의 합격 기준은 compose에 없다. 측정값만 적었다.
- 공식 게이트 scripts/qa/run.py는 파일이 없어 실행하지 않았다. 이 기록을 QA 통과로 보지 않는다.
- RISK-SEC-001, RISK-LEGACY-FAILS, RISK-QA-AUTH는 이 실행에서 다시 검증하지 않았다. 상태는 그대로다.
- .github/workflows/githubactions.yml 수정은 이 검사의 변경이 아니다. dirty는 True다.
- 비밀번호와 API 키 값은 보고서와 증거 파일에 남기지 않았다. 증거 치환 건수는 0이다.

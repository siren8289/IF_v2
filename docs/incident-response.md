# 장애 대응

측정은 2026-10-31 01:43 KST, 로컬 compose 스택 `if-app-stack` 에서 했다. Postgres 와 Spring 은 멈추지 않았다. AWS 배포는 호출하지 않았다.

## 화면 프로세스 중단

절차는 `infra/fault/inject.sh` 다. `if-app-stack-frontend-1` 을 `docker stop` 한 뒤 `docker start` 한다.

| 시점 | HTTP |
|---|---|
| 중지 전 `GET /` | 200 |
| 중지 중 | 000 |
| 다시 띄운 뒤 | 1초 후 200 |

## AI 프로세스 중단

같은 스크립트가 `if-app-stack-fastapi-1` 을 멈춘다.

| 시점 | `GET /health` |
|---|---|
| 중지 전 | 200 |
| 중지 중 | 000 |
| 다시 띄운 뒤 | 6초 후 200 |

그 사이 `GET /api/jobs` 는 200 이었다. 직무 목록은 AI 를 부르지 않는다. 평가 생성 API 가 AI 부재 때 502 를 내는 경로는 이번 실행에서 호출하지 않았다. 평가 행을 만들지 않기 위해서다. 그 동작의 이전 기록은 `qa/reports/integration/2026-10-30` 의 LOG-011 이다.

원문 로그는 `docs/evidence/fault-injection.log`.

## 배포 실패

재현은 하지 않았다. `deploy.yml` 은 SSM 상태가 `Success` 가 아니면 워크플로가 실패한다. `scripts/deploy.sh` 는 프론트, Spring, FastAPI 헬스 체크가 60번 안에 되지 않으면 해당 서비스 로그를 남기고 종료 코드 1 로 끝난다. 복구는 실패한 명령을 고친 뒤 같은 SHA 의 CI 가 성공한 다음 `workflow_dispatch` 로 배포를 다시 보내는 것이다. 서버에서 컨테이너를 되돌리는 명령은 저장소에 없다.

## 한계

알림 시스템이 이 중지를 감지했는지는 확인하지 않았다. 관측용 Prometheus 는 띄우지 않았다. 사람이 받는 알림 대상도 없다.

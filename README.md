# IF_v2

고령자 직무 위험도 참고 점수를 계산하는 로컬 스택이다. 화면은 React, API 는 Spring Boot, 점수와 설명은 FastAPI, 저장은 Postgres 다. 배포는 GitHub Actions 가 EC2 한 대에 SSM 으로 `docker compose` 를 실행한다.

저장소: https://github.com/siren8289/IF_v2

## 로컬 실행

`IF_DB_PASSWORD` 가 있어야 한다.

```sh
docker compose up -d --build
```

화면은 `http://127.0.0.1/`, Spring 은 `http://127.0.0.1:8080`, FastAPI 는 `http://127.0.0.1:8000` 이다.

## 아키텍처

지금 운영 경로와 CI 그림은 `docs/ARCHITECTURE.md` 에 있다. Kubernetes 매니페스트는 같은 컨테이너의 정의이고, 클러스터에는 올리지 않았다.

| 문서 | 내용 |
|---|---|
| `docs/infrastructure.md` | Terraform, Kubernetes, 실행한 검증 |
| `docs/monitoring.md` | Prometheus 규칙. CloudWatch 는 만들지 않음 |
| `docs/security.md` | OIDC, SSM 최소 권한, Secret 참조 |
| `docs/incident-response.md` | 로컬 컨테이너 중지와 복구 |
| `docs/performance.md` | 읽기 요청 30건 측정. k6 는 미실행 |
| `docs/cost-optimization.md` | 자원 범위. 요금 API 는 호출하지 않음 |
| `docs/contributions.md` | Git 작성자 수와 이번 인프라 파일 |

## 증빙

| 파일 | 내용 |
|---|---|
| `docs/evidence/terraform-validate.txt` | `terraform validate` 성공 |
| `docs/evidence/terraform-plan.txt` | 가짜 자격 증명으로 plan. STS 403. apply 없음 |
| `docs/evidence/k8s-kinds.txt` | `kubectl kustomize` 결과 종류 |
| `docs/evidence/promtool.txt` | 알림 규칙 4개 성공 |
| `docs/evidence/manifest-tests.txt` | 매니페스트 테스트 6건 통과 |
| `docs/evidence/fault-injection.log` | 프론트·FastAPI 중지 후 복구 |
| `docs/evidence/performance.json` | 로컬 지연과 오류율 |

인프라 검증은 CI 잡 `infra-validate` 가 `python -m unittest discover -s infra/tests` 와 `terraform validate` 를 실행한다. `terraform apply` 는 없다.

## 남은 한계

AWS 계정에 역할을 만들거나 기존 EC2 를 바꾸지 않았다. Prometheus 스택은 띄우지 않아 CPU·메모리 알림이 실제로 울렸는지는 모른다. k6 바이너리가 없어 부하 스크립트는 실행하지 않았다. 평가 API 인증 부재는 그대로다.

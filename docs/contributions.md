# 기여 기록

자격증은 만들지 않았다. 아래는 `git shortlog -sn --all` 과 이번 작업 트리에 있는 파일이다.

## Git 에 기록된 작성자

| 작성자 | 커밋 수 |
|---|---:|
| jeong-yelim | 61 |
| siren8289 | 27 |
| copilot-swe-agent[bot] | 1 |

`jeong-yelim` 이름으로 잡히는 경로 상위는 `spring`, `ai`, `TC_docs`, `web-vite`, `web`, `data`, `docs` 다. 같은 커밋이 두 작성자 이름에 함께 보이는 경우가 있어, 이 표를 사람 한 명의 단독 기여로 해석하지 않는다.

최근 커밋에는 배포(`f5a63eb4` AWS 배포, `f31b5a4f` SSM, `44e2ad01` compose Postgres), 화면 프록시(`8e8b08ed`), RAG(`aebcf6ae`), 테스트 문서(`8822a4f5`, `6afaa0a4`, `9491fb1b`)가 있다.

## 이번 작업에서 추가한 영역

아직 커밋하지 않았다.

- `infra/terraform`: 기존 EC2·OIDC·SSM 권한의 코드. 적용하지 않음.
- `infra/k8s`: 네 서비스의 매니페스트.
- `infra/monitoring`: Prometheus 규칙, 대시보드 JSON, 선택 compose.
- `infra/perf`, `infra/fault`: 로컬 측정과 장애 주입.
- `infra/tests`: 매니페스트 검증.
- `.github/workflows/githubactions.yml`: `infra-validate` 잡.
- `docs/infrastructure.md` 외 이 디렉터리의 결과 문서와 `docs/evidence/`.

애플리케이션 Java, Python, React 로직과 DB 스키마는 바꾸지 않았다.

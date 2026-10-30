# 보안

## 기존 상태

`deploy.yml` 은 `permissions` 에 `contents: read`, `actions: read`, `id-token: write` 만 있다. AWS 접속은 `aws-actions/configure-aws-credentials` 의 `role-to-assume: ${{ secrets.AWS_DEPLOY_ROLE_ARN }}` 이다. 정적 `AWS_ACCESS_KEY` 는 워크플로에 없다. 배포 명령은 SSM `AWS-RunShellScript` 로 그 인스턴스에만 보낸다. DB 비밀번호는 서버 `.env` 에 있고 저장소에 없다. `scripts/deploy.sh` 가 없을 때만 서버에서 만들어 `chmod 600` 한다.

## 추가한 것

`infra/terraform/iam.tf` 는 그 역할을 최소 권한으로 적는다. 신뢰 정책은 GitHub OIDC 이고, `sub` 는 `repo:siren8289/IF_v2:ref:refs/heads/main` 만 허용한다. 권한은 `ssm:SendCommand` 를 해당 인스턴스와 `AWS-RunShellScript` 문서에만 두고, 명령 조회와 취소만 더한다. `enable_iam` 기본값은 false 라서 이 역할을 계정에 만들지 않았다.

Kubernetes Secret `if-db` 의 비밀번호 값은 `local-dev-placeholder` 다. 배포 매니페스트는 `secretKeyRef` 만 참조한다. 실제 `IF_DB_PASSWORD` 는 넣지 않았다.

Spring 과 FastAPI 이미지는 그대로다. FastAPI 이미지는 root 로 실행된다. 이미지 사용자를 바꾸면 모델 파일 권한에 영향을 줄 수 있어 Dockerfile 은 수정하지 않았다.

## 검증

`infra/tests/test_manifests.py` 가 다음을 확인한다.

- 배포 워크플로에 OIDC 와 `role-to-assume` 이 있고 `AWS_ACCESS_KEY` 가 없다.
- Deployment 안에 비밀번호 문자열이 없고 Secret 은 placeholder 만 있다.
- Terraform 기본값이 자원을 만들지 않는다.

로컬 실행 6건 통과. 기록은 `docs/evidence/manifest-tests.txt`. `actionlint` 를 `githubactions.yml` 과 `deploy.yml` 에 실행했고 종료 코드는 0 이었다.

AWS IAM 에 역할이 붙어 있는지는 호출하지 않았다. 평가 API 에 인증이 없는 기존 문제 `RISK-SEC-001` 은 이번 변경으로 고치지 않았다.

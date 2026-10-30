# 인프라

## 기존 상태

애플리케이션은 `compose.yaml` 네 서비스다. Postgres 16, Spring Boot 3.2, FastAPI, Nginx. Spring 과 FastAPI 포트는 `127.0.0.1` 에만 열린다. 화면은 80번이다.

배포 정의는 `.github/workflows/deploy.yml` 이다. 리전 `ap-northeast-2`, 인스턴스 `i-0b400ab5f6fa756af`. CI 가 그 SHA 에서 성공한 뒤에만 SSM 으로 `/home/ubuntu/IF_v2` 에서 `scripts/deploy.sh` 를 실행한다. RDS, 로드밸런서, NAT, Kubernetes 클러스터는 이 저장소에 없다.

## 추가한 것

`infra/terraform` 은 그 서버를 코드로 적는다. 기본값 `enable_iam=false`, `manage_ec2=false` 라서 계획을 적용해도 인스턴스나 IAM 을 만들지 않는다. `manage_ec2` 를 켜면 Ubuntu 24.04, gp3 30GB, IMDSv2 를 요구하는 인스턴스 정의가 들어간다. 그 스위치는 꺼 두었다.

`infra/k8s` 는 같은 네 프로세스를 Deployment, Service, ConfigMap, Secret 참조, readiness, liveness 로 적는다. 이미지는 지금 로컬 태그 `if-spring:local`, `if-fastapi:local`, `if-frontend:local`, `postgres:16-alpine` 이다. Postgres 데이터는 `emptyDir` 이다. 운영 데이터는 EC2 의 Docker 볼륨에 있고, 이 매니페스트를 그 서버에 올리지 않았다.

## 명령과 결과

```sh
terraform -chdir=infra/terraform init -backend=false
terraform -chdir=infra/terraform validate
kubectl kustomize infra/k8s
```

`terraform validate` 결과는 `Success! The configuration is valid.` 다. 기록은 `docs/evidence/terraform-validate.txt`.

`kubectl kustomize` 가 만든 종류는 Namespace 1, ConfigMap 1, Secret 1, Deployment 4, Service 4 다. 기록은 `docs/evidence/k8s-kinds.txt`.

로컬 `kubectl apply --dry-run=client` 는 이 컴퓨터의 kubeconfig 가 가리키는 API 가 `unknown` 을 돌려줘서 서버 검증까지 가지 못했다. 클러스터에 적용하지 않았다.

가짜 AWS 키로 `terraform plan -var-file=environments/local.tfvars` 를 실행했다. 출력에 `apply_creates_resources = false` 가 있고, STS `GetCallerIdentity` 가 403 `InvalidClientTokenId` 로 끝났다. `terraform apply` 는 실행하지 않았다. 기록은 `docs/evidence/terraform-plan.txt`.

## 한계

실제 계정에 OIDC 역할이 있는지는 AWS API 로 확인하지 않았다. `deploy.yml` 은 `secrets.AWS_DEPLOY_ROLE_ARN` 을 읽는다. 역할 ARN 값은 저장소에 없다. Kubernetes 는 정의만 있고 클러스터는 없다.

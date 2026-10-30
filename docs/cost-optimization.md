# 비용

Cost Explorer 와 AWS 요금 API 는 호출하지 않았다. 달러 금액은 측정값이 아니다.

## 저장소에 있는 자원

운영 정의는 EC2 한 대에서 네 컨테이너를 돌린다. RDS, ALB, NAT Gateway, GPU 인스턴스는 정의되어 있지 않다. FastAPI 이미지는 CPU 용 PyTorch 를 설치한다. Spring 과 FastAPI 포트는 호스트의 `127.0.0.1` 에만 묶여 있다. 배포 스크립트는 메모리가 작을 때 2GB swap 파일을 만든다.

Terraform 기본 계획은 자원을 추가하지 않는다. `enable_iam` 과 `manage_ec2` 가 false 다. Kubernetes 매니페스트의 CPU·메모리 requests 는 클러스터에 올리지 않았으므로 클라우드 청구로 이어지지 않는다. 관측용 컨테이너도 띄우지 않았다.

## 적용하지 않은 절감

인스턴스 크기는 저장소에 없다. 더 작은 타입으로 바꾸는 작업은 서버를 멈추므로 하지 않았다. 사용하지 않는 EBS 나 탄력 IP 가 있는지는 조회하지 않았다. gp3 와 IMDSv2 는 `manage_ec2=true` 일 때의 정의로만 있고, 기존 디스크를 수정하지 않았다.

지운 AWS 자원은 없다.

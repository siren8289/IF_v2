#!/usr/bin/env bash
# EC2 서버에서 실행하는 배포 스크립트. (GitHub Actions → SSM → root 권한으로 이 파일 실행)
# 1) 서버 준비  2) 이미지 빌드  3) 컨테이너 실행  4) 헬스 체크
set -euo pipefail

cd /home/ubuntu/IF_v2

# ubuntu 계정으로 docker compose 실행
compose() {
  runuser -u ubuntu -- docker compose -f compose.yaml "$@"
}

echo "=== 1. 서버 준비 ==="
# Docker가 없으면 설치
if ! command -v docker > /dev/null; then
  echo "Docker 설치 중..."
  apt-get update -q
  apt-get install -y -q docker.io docker-compose-v2
  systemctl enable --now docker
fi
usermod -aG docker ubuntu
docker --version

# DB 비밀번호가 없으면 한 번만 만들어서 .env에 저장 (이후 계속 같은 값 사용)
touch .env
if ! grep -q '^IF_DB_PASSWORD=.' .env; then
  echo "IF_DB_PASSWORD=$(openssl rand -hex 16)" >> .env
  echo ".env 에 IF_DB_PASSWORD 생성"
fi
chown ubuntu:ubuntu .env
chmod 600 .env

# 메모리가 작은 서버라 swap 추가
if ! swapon --show | grep -q .; then
  fallocate -l 2G /swapfile || dd if=/dev/zero of=/swapfile bs=1M count=2048
  chmod 600 /swapfile
  mkswap /swapfile
  swapon /swapfile
fi
free -h

compose config --quiet

echo "=== 2. 이미지 빌드 (하나씩) ==="
compose build frontend
compose build spring
compose build fastapi

echo "=== 3. 컨테이너 실행 ==="
compose up -d --remove-orphans
compose ps

echo "=== 4. 헬스 체크 ==="
wait_http() {
  local url="$1"
  local name="$2"
  local service="$3"
  for i in $(seq 1 60); do
    if curl -fsS --max-time 5 "$url" > /dev/null 2>&1; then
      echo "$name OK"
      return 0
    fi
    sleep 3
  done
  echo "ERROR: $name 응답 없음 ($url)"
  compose logs --tail=60 "$service"
  return 1
}

wait_http http://127.0.0.1:8000/health FastAPI fastapi
wait_http http://127.0.0.1:8080/api/jobs Spring spring
wait_http http://127.0.0.1:8089/ Frontend frontend

docker image prune -f > /dev/null
echo "DEPLOYMENT SUCCESS"

#!/usr/bin/env bash
# EC2 서버에서 실행하는 배포 스크립트. (GitHub Actions → SSM → 이 파일)
# 1) DB 준비 확인  2) 이미지 빌드  3) 컨테이너 교체  4) 헬스 체크
set -euo pipefail

cd /home/ubuntu/IF_v2

DB_CONTAINER=if_portfolio-postgres-1
NETWORK=if-app-network

# ubuntu 계정으로 docker compose 실행
compose() {
  runuser -u ubuntu -- docker compose -f compose.yaml "$@"
}

echo "=== 1. DB 준비 확인 ==="
if ! docker network inspect "$NETWORK" > /dev/null 2>&1; then
  echo "ERROR: Docker 네트워크 '$NETWORK' 가 없습니다."
  exit 1
fi
echo "네트워크 OK: $NETWORK"

if [ "$(docker inspect -f '{{.State.Running}}' "$DB_CONTAINER" 2>/dev/null)" != "true" ]; then
  echo "ERROR: DB 컨테이너 '$DB_CONTAINER' 가 실행 중이 아닙니다."
  docker ps -a --format '{{.Names}}  {{.Status}}'
  exit 1
fi
echo "DB 컨테이너 OK: $DB_CONTAINER"

if ! grep -q '^IF_DB_PASSWORD=.' .env 2>/dev/null; then
  echo "ERROR: /home/ubuntu/IF_v2/.env 에 IF_DB_PASSWORD 가 없습니다."
  exit 1
fi
echo ".env OK"

if ! docker exec "$DB_CONTAINER" pg_isready -d if_spring > /dev/null; then
  echo "ERROR: DB가 연결을 받지 않습니다."
  exit 1
fi
echo "DB 응답 OK"

echo "=== 2. 메모리 확보 ==="
if ! swapon --show | grep -q .; then
  fallocate -l 2G /swapfile || dd if=/dev/zero of=/swapfile bs=1M count=2048
  chmod 600 /swapfile
  mkswap /swapfile
  swapon /swapfile
fi
free -h

echo "=== 3. 이미지 빌드 (하나씩) ==="
compose build frontend
compose build spring
compose build fastapi

echo "=== 4. 컨테이너 교체 ==="
compose up -d --force-recreate spring fastapi frontend
compose ps

echo "=== 5. 헬스 체크 ==="
wait_http() {
  local url="$1"
  local name="$2"
  for i in $(seq 1 40); do
    if curl -fsS --max-time 5 "$url" > /dev/null 2>&1; then
      echo "$name OK"
      return 0
    fi
    sleep 3
  done
  echo "ERROR: $name 응답 없음 ($url)"
  compose logs --tail=60 "$3"
  return 1
}

wait_http http://127.0.0.1:8000/health FastAPI fastapi
wait_http "http://127.0.0.1:8080/api/assessments?size=1" Spring spring
wait_http http://127.0.0.1:8089/ Frontend frontend

docker image prune -f > /dev/null
echo "DEPLOYMENT SUCCESS"

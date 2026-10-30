#!/bin/sh
# 로컬 compose 스택에서만 컨테이너를 멈췄다가 다시 띄운다.
# Postgres 와 Spring 은 멈추지 않는다. 끝나면 항상 기동을 되돌린다.
set -u
FRONTEND=if-app-stack-frontend-1
FASTAPI=if-app-stack-fastapi-1
LOG=${1:-docs/evidence/fault-injection.log}

restore() {
  docker start "$FRONTEND" "$FASTAPI" >/dev/null 2>&1 || true
}
trap restore EXIT INT TERM

mkdir -p "$(dirname "$LOG")"
: > "$LOG"

note() {
  printf '%s\n' "$1" | tee -a "$LOG"
}

http_code() {
  curl -sS -o /dev/null -w '%{http_code}' --max-time 5 "$1" 2>>"$LOG" || true
}

note "start $(date '+%Y-%m-%dT%H:%M:%S%z')"
note "frontend before $(http_code http://127.0.0.1/)"
docker stop "$FRONTEND" >>"$LOG" 2>&1
note "frontend stopped $(http_code http://127.0.0.1/)"
docker start "$FRONTEND" >>"$LOG" 2>&1
i=0
while [ "$i" -lt 30 ]; do
  code=$(http_code http://127.0.0.1/)
  if [ "$code" = "200" ]; then
    break
  fi
  i=$((i + 1))
  sleep 1
done
note "frontend restored $code after ${i}s"

note "fastapi before $(http_code http://127.0.0.1:8000/health)"
docker stop "$FASTAPI" >>"$LOG" 2>&1
note "fastapi stopped $(http_code http://127.0.0.1:8000/health)"
docker start "$FASTAPI" >>"$LOG" 2>&1
i=0
while [ "$i" -lt 40 ]; do
  code=$(http_code http://127.0.0.1:8000/health)
  if [ "$code" = "200" ]; then
    break
  fi
  i=$((i + 1))
  sleep 1
done
note "fastapi restored $code after ${i}s"
note "spring still $(http_code http://127.0.0.1:8080/api/jobs)"
note "end $(date '+%Y-%m-%dT%H:%M:%S%z')"

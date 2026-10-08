#!/usr/bin/env bash
# data/storage/operational + external + analytics SQL을 순서대로 적용한다 (로드맵: 설계 → 인덱스 → 제약 → 집계 → 분석).
#
# 사용법 (레포 루트 기준):
#   ./data/storage/apply-schema.sh
#   ./data/storage/apply-schema.sh --seed      # 개발 시드 포함
#   ./data/storage/apply-schema.sh --pipeline # 스키마 + 파이프라인 1회 실행

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DB_NAME="${DB_NAME:-if_spring}"
DB_USER="${DB_USER:-if_user}"
PG_HOST="${PGHOST:-localhost}"
PG_PORT="${PGPORT:-5432}"
PGPASSWORD="${PGPASSWORD:-change-me}"
export PGPASSWORD

RUN_SEED=false
RUN_PIPELINE=false
for arg in "$@"; do
  case "$arg" in
    --seed) RUN_SEED=true ;;
    --pipeline) RUN_PIPELINE=true ;;
  esac
done

run_sql() {
  local file="$1"
  echo "==> $(basename "$file")"
  psql -h "$PG_HOST" -p "$PG_PORT" -U "$DB_USER" -d "$DB_NAME" -v ON_ERROR_STOP=1 -f "$file"
}

echo "==> DB 스키마 적용 (${DB_USER}@${PG_HOST}:${PG_PORT}/${DB_NAME})"

# 기존 Hibernate DB에 updated_at 컬럼 보강 (마이그레이션)
run_sql "$SCRIPT_DIR/migrations/001_add_updated_at.sql" || true

for f in "$SCRIPT_DIR"/operational/0*.sql; do
  [[ -f "$f" ]] || continue
  if [[ "$(basename "$f")" == "05_seed_dev.sql" ]] && [[ "$RUN_SEED" != true ]]; then
    continue
  fi
  run_sql "$f"
done

for f in "$SCRIPT_DIR"/external/0*.sql; do
  [[ -f "$f" ]] || continue
  run_sql "$f"
done

run_sql "$SCRIPT_DIR/analytics/01_star_schema.sql"
run_sql "$SCRIPT_DIR/analytics/02_refresh_fact.sql"
run_sql "$SCRIPT_DIR/analytics/03_kpi_views.sql"

if [[ "$RUN_PIPELINE" == true ]]; then
  echo "==> 파이프라인 실행"
  run_sql "$DATA_DIR/pipelines/refresh_summary.sql"
  psql -h "$PG_HOST" -p "$PG_PORT" -U "$DB_USER" -d "$DB_NAME" -v ON_ERROR_STOP=1 \
    -c "INSERT INTO pipeline_run_log (job_name, finished_at, processed_row_count, status)
        SELECT 'apply_schema_bootstrap', now(), (SELECT count(*) FROM analytics.fact_assessment), 'SUCCESS';"
fi

echo ""
echo "완료. 검증:"
echo "  psql ... -f data/storage/verify-db-efficiency.sql"
echo "  psql ... -f data/quality/checks.sql"
echo "  psql ... -f data/quality/external_checks.sql"
echo "  psql ... -f data/quality/analytics_checks.sql"

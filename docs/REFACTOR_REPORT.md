# IF_v2 리팩토링 결과

요청한 storage·pipelines·notebooks·docs 구조로 통합했습니다. 현재 작업 폴더명 IF_portfolio는 유지합니다.

[전체 폴더 트리](STRUCTURE_FULL.txt), [데이터 실행 안내](../data/README.md).

수집 코드는 clients/public_api.py와 collectors/external_public.py로, 정제 코드는 parsers/external_payload.py와 transforms/external_normalization.py로 분리했습니다. 이전 Python 모듈은 import/CLI 호환 진입점으로 유지합니다.

DB SQL은 storage/, 갱신 스크립트는 pipelines/, DB 품질 검사는 quality/로 이동했습니다. 기존 ALTER 문은 migrations/001_add_updated_at.sql로 추출해 기존 best-effort 실행을 유지합니다. 자동 migration 이력 관리는 도입하지 않았습니다. 기존 notebook은 없어 EDA 작업 위치와 안내를 추가했습니다.

루트에서 이미 삭제된 AI/BE/ML/QA 문서는 Git 원본을 docs/에 보존했으며 루트 파일은 다시 만들지 않았습니다. 기존 Gradle lock 변경은 작업 목록에서 제외했습니다.

## 원본 파일 이동

| 원본 | 최종 위치 |
| --- | --- |
| `da/DA.md` | `docs/analytics/DA.md` |
| `da/DATA.md` | `docs/analytics/DATA.md` |
| `da/README.md` | `docs/analytics/README.md` |
| `db/README.md` | `docs/storage.md` |
| `db/analytics/01_star_schema.sql` | `data/storage/analytics/01_star_schema.sql` |
| `db/analytics/02_refresh_fact.sql` | `data/storage/analytics/02_refresh_fact.sql` |
| `db/analytics/03_kpi_views.sql` | `data/storage/analytics/03_kpi_views.sql` |
| `db/apply-schema.sh` | `data/storage/apply-schema.sh` |
| `db/docker-init.sh` | `data/storage/docker-init.sh` |
| `db/init-db.sh` | `data/storage/init-db.sh` |
| `db/operational/01_tables.sql` | `data/storage/operational/01_tables.sql` |
| `db/operational/02_indexes.sql` | `data/storage/operational/02_indexes.sql` |
| `db/operational/03_constraints.sql` | `data/storage/operational/03_constraints.sql` |
| `db/operational/04_summary.sql` | `data/storage/operational/04_summary.sql` |
| `db/operational/05_seed_dev.sql` | `data/storage/operational/05_seed_dev.sql` |
| `db/pipeline/refresh_summary.sql` | `data/pipelines/refresh_summary.sql` |
| `db/pipeline/run_all.sh` | `data/pipelines/run_all.sh` |
| `db/quality/analytics_checks.sql` | `data/quality/analytics_checks.sql` |
| `db/quality/checks.sql` | `data/quality/checks.sql` |
| `db/verify-db-efficiency.sql` | `data/storage/verify-db-efficiency.sql` |
| `de/DE.md` | `docs/ingestion/DE.md` |
| `de/README.md` | `docs/ingestion/README.md` |
| `de/data/external/.gitignore` | `data/ingestion/snapshots/external/.gitignore` |
| `de/data/external/.gitkeep` | `data/ingestion/snapshots/external/.gitkeep` |
| `de/etl/__init__.py` | `data/ingestion/__init__.py` |
| `de/etl/external_public_ingestion.py` | `data/ingestion/external_public_ingestion.py` |
| `de/etl/external_sources.json` | `data/ingestion/external_sources.json` |
| `de/external/01_reference_schema.sql` | `data/storage/external/01_reference_schema.sql` |
| `de/external/02_indexes_constraints.sql` | `data/storage/external/02_indexes_constraints.sql` |
| `de/external/03_seed_sources.sql` | `data/storage/external/03_seed_sources.sql` |
| `de/quality/external_checks.sql` | `data/quality/external_checks.sql` |
| `de/requirements.txt` | `data/requirements.txt` |
| `de/tests/__init__.py` | `data/tests/__init__.py` |
| `de/tests/test_external_public_ingestion.py` | `data/tests/test_external_public_ingestion.py` |
| `AI.md` | `docs/AI.md` |
| `BE.md` | `docs/BE.md` |
| `ML.md` | `docs/ML.md` |
| `QA.md` | `docs/QA.md` |

## 기존 파일 수정

- `.github/workflows/githubactions.yml`
- `.gitignore`
- `README.md`
- `ai/README.md`
- `ai/ml/README.md`
- `docker-compose.yml`
- `spring/BACKEND_STRUCTURE.md`
- `spring/bin/main/application.yml`
- `spring/bin/main/schema.sql`
- `spring/src/main/resources/application.yml`
- `spring/src/main/resources/schema.sql`

## 추가 파일 (위 이동 파일 제외)

- `data/.env.example`
- `data/README.md`
- `data/__init__.py`
- `data/ingestion/clients/__init__.py`
- `data/ingestion/clients/public_api.py`
- `data/ingestion/collectors/__init__.py`
- `data/ingestion/collectors/external_public.py`
- `data/notebooks/README.md`
- `data/pipelines/README.md`
- `data/processing/__init__.py`
- `data/processing/external_normalization.py`
- `data/processing/parsers/__init__.py`
- `data/processing/parsers/external_payload.py`
- `data/processing/transforms/__init__.py`
- `data/processing/transforms/external_normalization.py`
- `data/quality/README.md`
- `data/quality/__init__.py`
- `data/quality/external_validation.py`
- `data/storage/migrations/001_add_updated_at.sql`
- `data/storage/migrations/README.md`
- `data/tests/fixtures/sample_region.xml`
- `docs/README.md`
- `docs/STRUCTURE_FULL.txt`
- `docs/processing.md`
- `web-vite/README.md`
- `docs/REFACTOR_REPORT.md`

## 검증 결과

- Vite 빌드 성공, 테스트 14개 통과.
- Spring 빌드 성공, 테스트 16개 통과.
- 데이터 unittest 4개·AI unittest 11개 통과.
- 새 collector CLI와 이전 CLI를 샘플 XML로 실행: SUCCESS, 재실행 후 manifest 하나 유지.
- Python compileall, 셸 bash -n, Docker Compose config 검사 통과.
- 로컬 schema·DB pipeline·Docker init의 SQL 경로 26개 확인. psql mock과 Docker mount 경로 대응으로 검사했으며 실제 SQL 적용 검증은 아님.
- 원본 SQL·source JSON 보존 검사 통과 (경로 참조 주석 제외).
- 문서 로컬 링크와 git diff --check 검사 통과.

Python은 /tmp/if-data-refactor-venv의 기존 requirements를 사용했습니다. Spring은 ./gradlew build test --no-daemon --project-cache-dir /tmp/if-data-refactor-gradle-cache로 확인했습니다.

공공 API 실호출·PostgreSQL 실제 적재·Docker 전체 기동은 검증하지 않았습니다. 공공 수집은 파일·Parquet serving까지 제공하며, 공공 Parquet → PostgreSQL 자동 적재는 기존과 동일하게 미구현입니다.

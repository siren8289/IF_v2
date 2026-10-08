# DB

PostgreSQL 운영·분석 스키마와 파이프라인의 **단일 소스**입니다.

공공 Reference(DDL·DQ)는 DE 역할 폴더 [`../data/`](../data/) 에 있습니다.
`./data/storage/apply-schema.sh` 가 `data/storage/` + `data/storage/external/` 을 함께 적용합니다.

## 구조

```text
data/storage/
├── operational/           # OLTP 테이블·인덱스·제약·Summary MV
├── analytics/             # Star Schema · KPI 뷰 (DA)
├── external/              # 공공 reference 테이블
├── migrations/            # 기존 컬럼 보강 SQL
├── apply-schema.sh
├── init-db.sh
├── docker-init.sh
└── verify-db-efficiency.sql
```

| 영역 | 경로 | 역할 |
| --- | --- | --- |
| 운영 OLTP | `data/storage/operational/` | 테이블·인덱스·제약·Summary MV |
| 분석 Star Schema | `data/storage/analytics/` | dim/fact · KPI 뷰 |
| 품질 검사 | `data/quality/` | 운영 / analytics DQ |
| 파이프라인 | `data/pipelines/` | 증분 적재 · MV 갱신 |
| 공공 Reference (DE) | [`../data/storage/external/`](../data/storage/external/) | Source Catalog · raw · serving |
| DE DQ | [`../data/quality/external_checks.sql`](../data/quality/external_checks.sql) | external_ref only |

## 관련 스펙

- Data Engineering (DE-01~05): [`../docs/ingestion/DE.md`](../docs/ingestion/DE.md)
- Data Analytics (DA-01~04): [`../docs/analytics/DA.md`](../docs/analytics/DA.md)
- 저장소·연결 요약: [`../docs/analytics/DATA.md`](../docs/analytics/DATA.md)

## 빠른 시작

```bash
# 레포 루트에서
chmod +x data/storage/*.sh data/pipelines/*.sh
./data/storage/init-db.sh                  # 최초: DB 생성 + 스키마
./data/storage/apply-schema.sh             # 스키마만 갱신
./data/pipelines/run_all.sh         # 적재 → 품질 → MV
```

검증:

```bash
PGPASSWORD=change-me psql -h localhost -U if_user -d if_spring -f data/quality/checks.sql
PGPASSWORD=change-me psql -h localhost -U if_user -d if_spring -f data/quality/external_checks.sql
PGPASSWORD=change-me psql -h localhost -U if_user -d if_spring -f data/quality/analytics_checks.sql
```

# Pipelines

`run_all.sh`는 PostgreSQL의 증분 fact 적재 → 품질 검사 → MV 갱신 → 실행 로그를 수행합니다. `refresh_summary.sql`은 기존 요약 갱신 SQL입니다.

저장소 루트에서:

```bash
./data/storage/apply-schema.sh
python -m data.ingestion.collectors.external_public --help
./data/pipelines/run_all.sh
```

공공 API → 파일·Parquet 수집과 DB 분석 갱신은 현재 별도 단계입니다. 공공 Parquet → PostgreSQL 자동 적재 기능은 아직 구현되지 않았습니다.

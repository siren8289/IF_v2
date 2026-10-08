# IF 데이터 파이프라인

공공데이터 API → 수집 → 정제·품질 검사 → PostgreSQL → 분석/AI → Spring API → Vite 시각화

| 단계 | 위치 | 책임 |
| --- | --- | --- |
| 수집 | `ingestion/clients/`, `ingestion/collectors/` | API/파일 입력, source catalog, immutable raw, manifest/lineage |
| 정제 | `processing/parsers/`, `processing/transforms/` | XML/JSON/CSV 파싱, field mapping, 타입 정규화, natural key 중복 제거 |
| 품질 | `quality/` | Python DQ gate, PostgreSQL external_ref 검사 |
| PostgreSQL | `storage/` | 운영·분석 SQL, 공공 reference DDL, schema 적용·갱신 |
| 분석 | `../docs/analytics/`, `storage/analytics/` | KPI/grain 정의, star schema와 KPI view |
| AI | `../ai/` | 기존 전처리·위험도 계산·설명 서비스 |
| API | `../spring/` | PostgreSQL과 AI를 연결하는 서비스 API |
| 시각화 | `../web-vite/` | 대시보드 요약·평가 목록·위험도 결과 화면 |

`ai/`, `spring/`, `web-vite/`는 기존 구조를 유지하며 DB 기능은 `storage/`로 통합합니다. `dv/`는 만들지 않습니다.

## 실행 (저장소 루트)

```bash
python3 -m venv data/.venv
source data/.venv/bin/activate
pip install -r data/requirements.txt
python -m data.ingestion.collectors.external_public --help
python -m data.ingestion.collectors.external_public \
  --source self_support_region_code \
  --input-file data/tests/fixtures/sample_region.xml \
  --idempotency-key 2026-08
python -m unittest discover -s data/tests -v
./data/storage/apply-schema.sh
./data/pipelines/run_all.sh
```

산출물 기본 경로는 `ingestion/snapshots/external/`입니다. 기존 산출물 경로를 계속 쓸 때는 `IF_EXTERNAL_DATA_DIR`로 지정합니다. 실행 위치와 무관하게 카탈로그와 기본 산출물 경로를 모듈 파일 기준으로 찾습니다.

현재 공공 ingestion은 파일 snapshot/parquet를 생성하고, PostgreSQL DDL·source catalog와 SQL 품질 검사는 별도로 실행합니다. 공공 parquet를 PostgreSQL에 자동 적재하거나 새 Spring 분석 API를 제공하는 기능은 이번 폴더 리팩토링에서 추가하지 않았습니다. 외부 reference는 개인 점수의 정답 label로 사용하지 않습니다.

상세: [수집 설계](../docs/ingestion/DE.md), [수집 설명](../docs/ingestion/README.md), [분석 스펙](../docs/analytics/DA.md), [저장소 연결](../docs/analytics/DATA.md), [DB 실행](../docs/storage.md).

설정 예시: `.env.example`. `.env`를 복사한 뒤 `set -a; source data/.env; set +a`로 셸에 적용합니다. 문서는 [docs/](../docs/README.md), EDA 실험은 [notebooks/](analytics/notebooks/README.md)에 모읍니다.

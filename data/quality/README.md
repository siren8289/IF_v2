# Quality

`external_validation.py`는 정제 결과의 row count, 필수 식별자, natural key와 KOSIS grain을 검증합니다. 실패 시 수집 모듈이 serving snapshot 반영을 차단합니다.

`external_checks.sql`은 PostgreSQL `external_ref` 품질 검사입니다. 운영·분석 DB 검사는 기존 `data/quality/`에 유지합니다.

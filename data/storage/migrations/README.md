# Migrations

`001_add_updated_at.sql`은 기존 schema 적용 스크립트에 있던 `updated_at` 컬럼 보강 SQL입니다. `apply-schema.sh`가 기존과 동일하게 best-effort로 실행합니다. `ADD COLUMN IF NOT EXISTS`로 재실행 가능합니다.

Flyway/Liquibase 또는 migration 이력 테이블은 사용하지 않습니다. 새 migration은 번호와 적용 순서를 명시하고 schema 적용 스크립트에 추가해야 합니다.

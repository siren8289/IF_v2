
-- ============================================================
-- IF_v2 | Job 외부 공고 ID 추가
-- ============================================================
--
-- 목적:
-- Spring Job 내부 PK와 공공데이터 원본 공고 ID 연결
--
-- Spring:
--   job.id -> BIGINT
--
-- FastAPI:
--   job_id -> VARCHAR
--   예: KJ21062610080016
--
-- 기존 테이블 및 데이터 유지
-- ============================================================


-- 1. 외부 공고 ID 컬럼 추가
-- 이미 존재하면 건너뛴다.
ALTER TABLE job
ADD COLUMN IF NOT EXISTS external_job_id VARCHAR(100);


-- 2. 외부 공고 ID 중복 방지
-- NULL은 허용하므로 수동 등록 일자리도 저장 가능하다.
CREATE UNIQUE INDEX IF NOT EXISTS
    ux_job_external_job_id
ON job (external_job_id)
WHERE external_job_id IS NOT NULL;


-- 3. 컬럼 설명
COMMENT ON COLUMN job.external_job_id IS
'공공데이터 원본 공고 ID. FastAPI F-002/F-003 job_id 매핑에 사용';


-- 3-1. 적재된 공공데이터 구인공고(PUB-012)를 job 테이블에 연결
-- staging.public_api_raw 의 jobId 를 external_job_id 로 저장한다.
-- 이미 연결된 공고는 건너뛰므로 여러 번 실행해도 안전하다.
-- 상세 업무 설명·근무시간은 원천 API에 없어 NULL 로 둔다.
DO $$
BEGIN
    IF to_regclass('staging.public_api_raw') IS NOT NULL THEN
        INSERT INTO job (
            external_job_id,
            job_title,
            workplace,
            created_at
        )
        SELECT
            r.payload ->> 'jobId',
            NULLIF(TRIM(r.payload ->> 'recrtTitle'), ''),
            NULLIF(TRIM(r.payload ->> 'workPlcNm'), ''),
            COALESCE(r.collected_at, NOW())
        FROM staging.public_api_raw r
        WHERE r.dataset_code = 'PUB-012'
          AND NULLIF(TRIM(r.payload ->> 'jobId'), '') IS NOT NULL
        ORDER BY r.source_row_number
        ON CONFLICT (external_job_id)
            WHERE external_job_id IS NOT NULL
        DO NOTHING;
    END IF;
END
$$;


-- 4. 변경 결과 확인
SELECT
    column_name,
    data_type,
    character_maximum_length,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'job'
  AND column_name = 'external_job_id';


-- 5. 기존 데이터 유지 및 연결 결과 확인
SELECT
    COUNT(*) AS total_jobs,
    COUNT(external_job_id) AS linked_jobs
FROM job;

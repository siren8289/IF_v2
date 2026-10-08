SELECT
    source_id,
    COUNT(*) AS record_count
FROM external_ref.public_record
GROUP BY source_id;

SELECT
    run_id,
    source_id,
    status,
    record_count,
    started_at
FROM external_ref.etl_run
ORDER BY run_id DESC
LIMIT 10;

"""
AI-F-001 데이터 전처리 단위 테스트.

실제 PostgreSQL 연결 없이 실행한다.
"""

import pandas as pd

from src.features.f001_job_task.data import (
    normalize_code,
    normalize_text,
    prepare_job_context,
    build_quality_report,
)


def test_normalize_code():
    assert normalize_code("00123") == "00123"
    assert normalize_code("123.0") == "123"
    assert normalize_code(None) is None


def test_normalize_text():
    assert normalize_text(" 서울   강남 ") == "서울 강남"
    assert normalize_text(None) is None


def test_prepare_job_context():
    raw = pd.DataFrame([
        {
            "source_record_key": "1",
            "features": {
                "dataset_code": "PUB-001",
                "region_code": "00123",
                "region_name": " 서울  강남 ",
                "raw_attributes": {
                    "dstrcd": "00123",
                    "dstrname": " 서울  강남 ",
                },
            },
        }
    ])

    result = prepare_job_context(raw)

    assert len(result) == 1
    assert result.iloc[0]["region_code"] == "00123"
    assert result.iloc[0]["region_name"] == "서울 강남"


def test_organization_mapping():
    raw = pd.DataFrame([
        {
            "source_record_key": "2",
            "features": {
                "dataset_code": "PUB-002B",
                "organization_code": "00099",
                "organization_name": " 행복 센터 ",
                "raw_attributes": {
                    "orgcd": "00099",
                    "orgname": " 행복 센터 ",
                },
            },
        }
    ])

    result = prepare_job_context(raw)

    assert result.iloc[0][
        "organization_code"
    ] == "00099"

    assert result.iloc[0][
        "organization_name"
    ] == "행복 센터"


def test_quality_report():
    df = pd.DataFrame([
        {
            "dataset_code": "PUB-001",
            "source_record_key": "1",
            "region_code": "00123",
        },
        {
            "dataset_code": "PUB-001",
            "source_record_key": "1",
            "region_code": "00123",
        },
    ])

    report = build_quality_report(df)

    assert report["total_rows"] == 2
    assert report["duplicate_source_keys"] == 1

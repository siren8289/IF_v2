
"""
AI-F-001 전처리 단위 테스트.
실제 DB 연결 없이 실행 가능.
"""

import pandas as pd

from src.data.job_context import (
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
            "dataset_id": 1,
            "features": {
                "dataset_code": "PUB-001",
                "dstrcd": "00123",
                "dstrname": " 서울  강남 ",
            },
        }
    ])

    result = prepare_job_context(raw)

    assert len(result) == 1
    assert result.iloc[0]["dstrcd"] == "00123"
    assert result.iloc[0]["dstrname"] == "서울 강남"


def test_quality_report():
    df = pd.DataFrame([
        {
            "dataset_id": 1,
            "dataset_code": "PUB-001",
            "dstrcd": "00123",
        },
        {
            "dataset_id": 1,
            "dataset_code": "PUB-001",
            "dstrcd": "00123",
        },
    ])

    report = build_quality_report(df)

    assert report["row_count"] == 2
    assert report["duplicate_rows"] == 1

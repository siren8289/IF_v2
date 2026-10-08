from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"


def profile_jobs(df: pd.DataFrame):
    """실제 API 응답의 컬럼별 품질 현황 분석."""

    if df.empty:
        raise ValueError("수집된 데이터가 없습니다.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 공백 문자열도 결측으로 취급하되 원본 df는 변경하지 않음
    data = df.copy().replace(r"^\s*$", pd.NA, regex=True)

    rows = []

    for col in data.columns:
        series = data[col]

        rows.append({
            "source_column": col,
            "pandas_dtype": str(series.dtype),
            "total_count": len(series),
            "null_count": int(series.isna().sum()),
            "null_rate_pct": round(series.isna().mean() * 100, 2),
            "unique_count": int(series.nunique(dropna=True)),
            "sample_values": " | ".join(
                series.dropna().astype(str).unique()[:5]
            ),
        })

    profile = pd.DataFrame(rows)

    # 원본 데이터 보존
    df.to_csv(
        OUTPUT_DIR / "raw_jobs.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # 컬럼별 품질 분석 결과
    profile.to_csv(
        OUTPUT_DIR / "column_profile.csv",
        index=False,
        encoding="utf-8-sig"
    )

    return profile
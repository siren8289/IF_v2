
"""AI-F-002: 위험도 분석용 데이터 구조.

현재 Baseline은 산업재해 통계 근거를 조회하는 단계다.
개인별 위험 확률이나 검증되지 않은 위험 점수를 반환하지 않는다.
"""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True)
class RiskEvidence:
    feature_id: str
    job_id: str
    title: str
    candidate_category: str
    industry_candidate: Optional[str]
    mapping_status: str
    mapping_audit: str
    evidence_status: str
    evidence_year: Optional[int]
    industry_accident_count: Optional[float]
    evidence_usable: bool = False
    risk_score: Optional[float] = None

    def to_dict(self) -> dict:
        return asdict(self)

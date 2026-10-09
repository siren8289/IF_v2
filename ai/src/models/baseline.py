"""
AI-F-001 직무 작업 특성 분석
규칙 기반 Baseline v0.1

관련 요구사항:
AI-FR-001: 작업 특성 분류
AI-FR-002: 입력 검증
AI-FR-004: 결과 구조
AI-FR-005: 검토 필요 처리
AI-FR-006: 원문 근거 검증

주의:
이 코드는 학습된 AI 모델이 아니다.
confidence를 임의로 계산하지 않으며 모든 결과는 검토 대상으로 반환한다.
"""

import re
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


MODEL_VERSION = "keyword-baseline-v0.1"


class JobInput(BaseModel):
    """직무 분석 입력 데이터."""

    model_config = ConfigDict(extra="forbid", strict=True)

    jobId: int = Field(gt=0)
    jobTitle: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=10000)
    workHours: int = Field(gt=0, le=24)

    @field_validator("jobTitle", "description")
    @classmethod
    def validate_text(cls, value: str) -> str:
        """공백 문자열을 제거하고 빈 입력을 거부한다."""
        value = value.strip()

        if not value:
            raise ValueError("빈 문자열은 허용하지 않습니다.")

        return value


TASK_PATTERNS = {
    "OUTDOOR": [
        r"공원",
        r"야외",
        r"실외",
        r"거리",
        r"순찰",
    ],
    "HEAVY_LIFTING": [
        r"중량물",
        r"무거운\s*물건",
        r"무거운\s*짐",
        r"상하차",
    ],
    "REPETITIVE_MOTION": [
        r"반복",
        r"조립",
        r"포장",
        r"분류\s*작업",
    ],
    "WALKING": [
        r"걷",
        r"걸어\s*다니",
        r"보행",
        r"도보",
    ],
    "CLEANING": [
        r"청소",
        r"쓰레기",
        r"환경\s*정비",
        r"미화",
    ],
}


def extract_evidence(
    description: str,
    patterns: list[str],
) -> list[dict[str, Any]]:
    """정규식에 일치하는 원문 구절과 위치를 추출한다."""

    evidence = []
    seen = set()

    for pattern in patterns:
        for match in re.finditer(
            pattern,
            description,
            flags=re.IGNORECASE,
        ):
            start, end = match.span()

            if (start, end) in seen:
                continue

            seen.add((start, end))

            evidence.append({
                "text": description[start:end],
                "start": start,
                "end": end,
            })

    return sorted(
        evidence,
        key=lambda item: (item["start"], item["end"]),
    )


def verify_evidence(
    description: str,
    evidence: list[dict[str, Any]],
) -> bool:
    """근거 구절과 원문의 문자 위치가 일치하는지 확인한다."""

    for item in evidence:
        start = item["start"]
        end = item["end"]
        text = item["text"]

        if not (0 <= start < end <= len(description)):
            return False

        if description[start:end] != text:
            return False

    return True


def analyze_job(job: JobInput) -> dict[str, Any]:
    """직무 설명에서 여러 작업 특성을 추출한다."""

    task_tags = []
    evidence = []

    for tag, patterns in TASK_PATTERNS.items():
        matches = extract_evidence(
            job.description,
            patterns,
        )

        if not matches:
            continue

        if not verify_evidence(job.description, matches):
            continue

        task_tags.append(tag)

        for match in matches:
            evidence.append({
                "tag": tag,
                **match,
            })

    return {
        "jobId": job.jobId,
        "taskTags": task_tags,
        "confidence": {},
        "evidence": evidence,
        "reviewRequired": True,
        "modelVersion": MODEL_VERSION,
        "status": "REVIEW_REQUIRED",
    }


if __name__ == "__main__":
    import json

    sample = JobInput(
        jobId=1,
        jobTitle="공원 환경관리",
        description="공원에서 걸어 다니며 쓰레기를 수거하고 청소한다.",
        workHours=4,
    )

    result = analyze_job(sample)

    print(json.dumps(result, ensure_ascii=False, indent=2))
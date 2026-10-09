
"""AI-F-003: 산업재해 통계의 근거 기반 설명.

F-002가 검증한 통계만 사용한다.
업종 후보는 확정 산업분류가 아니다.
재해 건수를 개인별 사고 확률로 변환하지 않는다.
"""

from src.features.f002_risk.service import (
    get_combined_risk_evidence,
)


def explain_risk(
    job_id: str,
    year: int | None = None,
) -> dict:
    """F-002 근거를 읽고 검증 가능한 설명을 생성한다."""

    # 이미 구현·테스트된 F-002 서비스 재사용
    data = get_combined_risk_evidence(
        job_id=job_id,
        year=year,
    )

    job = data["job"]
    age = data["age_reference"]

    title = str(job["title"])
    industry = job.get("industry_candidate")
    mapping_audit = job.get("mapping_audit")

    evidence = []
    limitations = []

    # 1. 산업별 통계 근거
    count = job.get("industry_accident_count")
    evidence_year = job.get("evidence_year")

    if (
        industry
        and count is not None
        and evidence_year is not None
    ):
        count = float(count)

        evidence.append({
            "type": "INDUSTRY_ACCIDENT_COUNT",
            "label": "산업별 사고재해자수 집계",
            "industry": industry,
            "year": int(evidence_year),
            "value": count,
            "unit": "명",
            "source_dataset": (
                "external_ref.accident_industry_stat"
            ),
            "verification": "PROVISIONAL_MAPPING",
        })

        industry_text = (
            f"산업분류 후보인 '{industry}'의 "
            f"{int(evidence_year)}년 사고재해자수 "
            f"집계는 {count:,.0f}명입니다. "
            "다만 해당 직무가 이 산업에 속하는지는 "
            "검증되지 않았습니다."
        )
    else:
        industry_text = (
            "해당 직무에 연결할 수 있는 "
            "산업별 통계 근거가 아직 없습니다."
        )

    # 2. 연령별 통계는 개인 나이와 무관한 참고자료
    age_items = age.get("age_statistics", [])

    age_reference = {
        "statistic_year": age["statistic_year"],
        "metric_name": age["metric_name"],
        "age_groups": len(age_items),
        "source_dataset": (
            "external_ref.accident_age_stat"
        ),
        "is_personalized": False,
    }

    # 실제 출처를 추적할 수 있도록 설명 근거 기록
    evidence.append({
        "type": "AGE_REFERENCE",
        "label": "연령별 재해자수 참고 통계",
        "year": int(age["statistic_year"]),
        "value": None,
        "unit": "명",
        "age_statistics": age_items,
        "source_dataset": (
            "external_ref.accident_age_stat"
        ),
        "verification": "AGGREGATED_STATISTICS",
    })

    # 3. 매핑 오류·불명확한 근거 경고
    if mapping_audit == "POSSIBLE_MISMATCH":
        limitations.append(
            "직무명과 산업분류 후보가 충돌할 "
            "가능성이 있어 확인이 필요합니다."
        )
    elif mapping_audit == "MULTIPLE_SIGNALS":
        limitations.append(
            "직무명에서 여러 산업 신호가 발견되어 "
            "단일 산업으로 확정할 수 없습니다."
        )

    limitations.extend([
        "직무군 분류는 검수 전 후보 라벨입니다.",
        "산업별 통계와 연령별 통계는 "
        "서로 다른 집계 자료입니다.",
        "재해 건수만으로 개인의 사고 확률을 "
        "계산할 수 없습니다.",
    ])

    summary = (
        f"'{title}' 직무에 대한 산업재해 "
        f"통계 근거를 확인했습니다. "
        f"{industry_text} "
        f"연령별 {age['statistic_year']}년 통계는 "
        "일반적인 참고자료로만 제공합니다."
    )

    return {
        "feature_id": "AI-F-003",
        "job_id": str(job["job_id"]),
        "title": title,
        "summary": summary,
        "industry_mapping_status": "REVIEW_REQUIRED",
        "mapping_audit": mapping_audit,
        "age_reference": age_reference,
        "evidence": evidence,
        "limitations": limitations,
        "risk_score": None,
        "risk_probability": None,
        "explanation_method": "RULE_BASED",
        "explanation_status": "EVIDENCE_ONLY",
    }



# ============================================================
# AI-F-003 Gemini 하이브리드 설명
# ============================================================

import json
import logging
import os
import re
import threading
import time

from datetime import datetime, timezone

from pydantic import BaseModel, Field, ValidationError


logger = logging.getLogger(__name__)


class GeminiExtra(BaseModel):
    """Gemini는 통계 수치를 제외한 보충 설명만 생성."""

    extra_explanation: str = Field(
        min_length=10,
        max_length=300,
    )


# 개발용 로컬 사용량 제한.
# 서버 재시작·다중 서버에선 초기화되므로
# 배포용 전역 한도는 Redis 등으로 별도 구현 필요.
_usage_lock = threading.Lock()
_usage_day = None
_usage_count = 0



# ============================================================
# F-003 Redis 캐시 / Gemini 사용량 제한
# ============================================================

import hashlib
import json
import os
from datetime import datetime, timezone
from functools import lru_cache


@lru_cache(maxsize=1)
def _get_redis():
    """Redis 클라이언트를 생성하고 재사용한다."""
    import redis

    url = os.getenv("REDIS_URL")
    if not url:
        return None

    return redis.Redis.from_url(
        url,
        decode_responses=True,
        socket_connect_timeout=2,
        socket_timeout=2,
        health_check_interval=30,
    )


def _cache_key(job: dict, summary: str) -> str:
    """데이터와 모델이 변경되면 캐시 키도 바뀐다."""
    payload = {
        "job_id": job.get("job_id"),
        "industry": job.get("industry_candidate"),
        "audit": job.get("mapping_audit"),
        "evidence_year": job.get("evidence_year"),
        "accident_count": job.get("industry_accident_count"),
        "summary": summary,
        "model": os.getenv("F003_LLM_MODEL"),
        "version": "f003-extra-v1",
    }

    raw = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=False,
        default=str,
    )

    digest = hashlib.sha256(raw.encode()).hexdigest()
    return f"if:f003:extra:{digest}"


def _get_cached_extra(key: str) -> str | None:
    """검증된 Gemini 보충 설명을 캐시에서 조회한다."""
    client = _get_redis()
    if client is None:
        return None

    value = client.get(key)

    if value and _check_extra_explanation(value):
        return value

    return None


def _save_cached_extra(key: str, value: str) -> None:
    """검증된 결과만 TTL과 함께 저장한다."""
    if not _check_extra_explanation(value):
        raise ValueError("검증되지 않은 설명은 저장할 수 없습니다.")

    client = _get_redis()
    if client is None:
        return

    ttl = max(
        1,
        int(os.getenv("F003_CACHE_TTL_SECONDS", "86400")),
    )

    client.set(key, value, ex=ttl)


# 분당·일일 한도를 하나의 원자적 Redis 작업으로 검사
_QUOTA_SCRIPT = """
local minute_count = tonumber(redis.call('GET', KEYS[1]) or '0')
local daily_count = tonumber(redis.call('GET', KEYS[2]) or '0')

if minute_count >= tonumber(ARGV[1])
   or daily_count >= tonumber(ARGV[2]) then
    return 0
end

redis.call('INCR', KEYS[1])
redis.call('EXPIRE', KEYS[1], 120)

redis.call('INCR', KEYS[2])
redis.call('EXPIRE', KEYS[2], 172800)

return 1
"""


def _reserve_llm_request() -> bool:
    """Redis에서 Gemini 호출 슬롯을 원자적으로 예약한다."""
    client = _get_redis()

    # 로컬 개발에서는 Redis 없이도 실험 가능
    # 공개 배포에서는 F003_REQUIRE_REDIS=true로 차단
    if client is None:
        return False

    now = datetime.now(timezone.utc)
    minute = now.strftime("%Y%m%d%H%M")
    day = now.strftime("%Y%m%d")

    per_minute = max(
        0,
        int(os.getenv("F003_MAX_REQUESTS_PER_MINUTE", "3")),
    )
    per_day = max(
        0,
        int(os.getenv("F003_MAX_REQUESTS_PER_DAY", "100")),
    )

    result = client.eval(
        _QUOTA_SCRIPT,
        2,
        f"if:f003:quota:minute:{minute}",
        f"if:f003:quota:day:{day}",
        per_minute,
        per_day,
    )

    return int(result) == 1



def _check_extra_explanation(value: str) -> bool:
    """허위 통계·위험도 표현을 최소한으로 차단."""

    if not value or not value.strip():
        return False

    # 연도·수치·비율을 Gemini가 생성하지 못하게 차단
    if re.search(r"\d", value):
        return False

    # 검증되지 않은 위험 판단 금지
    forbidden = [
        "안전합니다",
        "위험합니다",
        "사고 확률",
        "사고확률",
        "위험 점수",
        "위험점수",
        "위험도가 높",
        "위험도가 낮",
        "사고가 발생할",
        "사고가 발생하지",
        "반드시",
        "확실히",
    ]

    return not any(word in value for word in forbidden)


def _gemini_extra_explanation(job: dict) -> str:
    """Gemini API로 수치 없는 설명 생성."""

    from google import genai
    from google.genai import types

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY가 없습니다.")

    model = os.getenv("F003_LLM_MODEL", "").strip()

    if not model:
        raise RuntimeError("F003_LLM_MODEL이 없습니다.")

    # 직무명·직무ID·개인정보는 전송하지 않음
    payload = {
        "has_industry_candidate": bool(
            job.get("industry_candidate")
        ),
        "mapping_audit": job.get("mapping_audit"),
        "evidence_status": job.get("evidence_status"),
    }

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=model,
            contents=json.dumps(payload, ensure_ascii=False),
            config=types.GenerateContentConfig(
                system_instruction=(
                    "너는 산업재해 통계 해석을 돕는 설명자다. "
                    "한국어로 짧고 보수적인 설명을 작성해라. "
                    "주어진 분류 상태만 설명하고 실제 직무 위험을 "
                    "판단하거나 업종을 확정하지 마라. "
                    "숫자, 연도, 백분율, 사고 건수, 재해자수, "
                    "확률, 위험점수를 절대 쓰지 마라. "
                    "사업장 산업분류가 검증되지 않았다는 점과 "
                    "추가 확인이 필요하다는 점만 설명해라."
                ),
                response_mime_type="application/json",
                response_schema=GeminiExtra,
                temperature=0,
                max_output_tokens=300,
            ),
        )

        if not response.text:
            raise ValueError("Gemini 응답이 비어 있습니다.")

        parsed = GeminiExtra.model_validate_json(
            response.text
        )

        return parsed.extra_explanation.strip()

    finally:
        client.close()



def explain_risk_hybrid(
    job_id: str,
    year: int | None = None,
) -> dict:
    """캐시 → 호출 제한 → Gemini → 검증 → fallback."""

    # 1. 항상 기존 규칙 기반 결과를 먼저 확보한다.
    # 잘못된 직무 ID나 연도 오류는 그대로 전달한다.
    result = explain_risk(job_id=job_id, year=year)

    result["explanation_method"] = "RULE_BASED"
    result["verification_status"] = "PASS"
    result["llm_used"] = False

    if os.getenv("F003_LLM_ENABLED", "false").lower() != "true":
        result["llm_status"] = "DISABLED"
        return result

    if not os.getenv("GEMINI_API_KEY"):
        result["llm_status"] = "NO_API_KEY"
        return result

    try:
        # 2. 기존 F-002 데이터를 재사용
        source = get_combined_risk_evidence(
            job_id=job_id,
            year=year,
        )
        job = source["job"]

        key = _cache_key(job, result["summary"])

        # 3. 캐시 조회 — 호출 횟수를 소비하지 않음
        cached = _get_cached_extra(key)

        if cached is not None:
            result["extra_explanation"] = cached
            result["explanation_method"] = "HYBRID"
            result["llm_used"] = True
            result["llm_status"] = "CACHE_HIT"
            return result

        # 4. Redis에서 호출 한도 확인
        if not _reserve_llm_request():
            result["llm_status"] = "LOCAL_LIMIT"
            return result

        # 5. Gemini 호출
        extra = _gemini_extra_explanation(job)

        # 6. 생성된 설명의 숫자·위험 판단 차단
        if not _check_extra_explanation(extra):
            result["llm_status"] = "VALIDATION_FAILED"
            return result

        # 7. 검증된 보충 설명만 캐시에 저장
        # 저장 오류는 응답 자체를 실패 처리하지 않음
        try:
            _save_cached_extra(key, extra)
        except Exception as cache_exc:
            logger.warning(
                "F-003 캐시 저장 실패: %s",
                type(cache_exc).__name__,
            )

        result["extra_explanation"] = extra
        result["explanation_method"] = "HYBRID"
        result["llm_used"] = True
        result["llm_status"] = "SUCCESS"

        return result

    except Exception as exc:
        logger.warning(
            "F-003 Gemini/Redis fallback: %s",
            type(exc).__name__,
        )
        result["llm_status"] = "FALLBACK"
        return result

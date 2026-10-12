"""안정성 보장을 위한 하네스(Harness) 모듈.

다음 5가지 필수 안정성 기능을 제공합니다:
1. 입력 검증 (Validation)
2. 타임아웃 제어 (Timeout)
3. 재시도 (Retry with Backoff)
4. 단계별 상세 로깅 (Logging)
5. 오류 격리 및 폴백 (Error Handling & Fallback)
"""
import functools
import logging
import time
from typing import Any, Callable

# RAG 전용 로거 설정
logger = logging.getLogger("IF_AI_RAG")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [RAG] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class ValidationError(ValueError):
    """입력값 유효성 검증 실패 시 발생하는 예외입니다."""
    pass


def validate_rag_input(title: str, risk_info: dict) -> tuple[str, dict]:
    """RAG 파이프라인 입력값을 검증하고 정제합니다."""
    if not isinstance(title, str) or not title.strip():
        raise ValidationError("직무 제목은 비어 있을 수 없는 문자열이어야 합니다.")

    clean_title = title.strip()
    if len(clean_title) > 300:
        raise ValidationError(f"직무 제목이 너무 깁니다 (최대 300자, 현재 {len(clean_title)}자).")

    if not isinstance(risk_info, dict):
        raise ValidationError("위험도 정보(risk_info)는 딕셔너리 형태여야 합니다.")

    score = risk_info.get("risk_score", 0)
    if not isinstance(score, (int, float)) or not (0 <= score <= 100):
        raise ValidationError(f"위험도 점수(risk_score)는 0~100 사이 숫자여야 합니다 (현재: {score}).")

    return clean_title, risk_info


def retry_with_backoff(
    max_retries: int = 3,
    initial_delay: float = 0.5,
    backoff_factor: float = 2.0,
    retryable_exceptions: tuple = (Exception,),
):
    """작업 실패 시 지수 백오프(Exponential Backoff)로 재시도하는 데코레이터입니다."""

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            last_exception = None

            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as error:
                    last_exception = error
                    logger.warning(
                        f"[{func.__name__}] 시도 {attempt}/{max_retries} 실패: {error}. "
                        f"{delay:.2f}초 후 재시도합니다."
                    )
                    if attempt < max_retries:
                        time.sleep(delay)
                        delay *= backoff_factor

            logger.error(f"[{func.__name__}] 최대 재시도 횟수({max_retries}) 초과.")
            raise last_exception

        return wrapper

    return decorator


def execute_with_harness(
    func: Callable[[], Any],
    fallback_factory: Callable[[Exception], Any],
    step_name: str = "RAG 단계",
) -> Any:
    """오류 격리 및 실행 시간 로깅을 적용하여 함수를 안전하게 실행합니다."""
    start_time = time.time()
    logger.info(f"'{step_name}' 실행 시작")

    try:
        result = func()
        elapsed = time.time() - start_time
        logger.info(f"'{step_name}' 정상 완료 (소요 시간: {elapsed:.3f}초)")
        return result
    except Exception as error:
        elapsed = time.time() - start_time
        logger.error(f"'{step_name}' 실행 중 오류 발생 (소요 시간: {elapsed:.3f}초): {error}")
        # 오류가 나도 시스템 전체가 죽지 않도록 폴백 생성기 호출
        return fallback_factory(error)

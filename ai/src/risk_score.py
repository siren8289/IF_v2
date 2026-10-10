"""개인 입력과 ML/DL 작업 특성 점수로 0~100점 참고 지수를 계산한다.

사고 확률이 아니라, 정해 둔 규칙(가중치)으로 더한 참고용 점수다.
"""

# 작업 특성별 가중치. 모델 점수(0~1)에 곱해서 더한다. 합계는 최대 30점.
TASK_WEIGHTS = {
    "DRIVING": 10,
    "NIGHT_SHIFT": 8,
    "WALKING": 8,
    "CLEANING_TASK": 8,
    "CARE_TASK": 6,
    "FACILITY_MAINTENANCE": 8,
}

TASK_NAMES = {
    "DRIVING": "운전",
    "NIGHT_SHIFT": "야간 근무",
    "WALKING": "장시간 보행",
    "CLEANING_TASK": "청소",
    "CARE_TASK": "돌봄",
    "FACILITY_MAINTENANCE": "시설 관리",
}


def age_points(age):
    """60세 이하 0점, 90세 이상 20점, 그 사이는 나이에 비례한다."""
    if age <= 60:
        return 0
    if age >= 90:
        return 20
    return (age - 60) * 20 / 30


def health_points(physical_level):
    """건강 상태 1(좋음)~5(나쁨) → 0~25점"""
    return (physical_level - 1) * 25 / 4


def chronic_points(chronic_disease):
    """만성질환이 있으면 15점"""
    return 15 if chronic_disease else 0


def work_hour_points(work_hour_limit):
    """하루 8시간 이상 일할 수 있으면 0점, 1시간이면 10점"""
    if work_hour_limit >= 8:
        return 0
    return (8 - work_hour_limit) * 10 / 7


def task_points(ml_scores, dl_scores):
    """ML과 DL 점수의 평균에 가중치를 곱해서 더한다. 최대 30점."""
    total = 0
    details = []
    for label, weight in TASK_WEIGHTS.items():
        ml = ml_scores.get(label, 0)
        dl = dl_scores.get(label, 0)
        average = (ml + dl) / 2
        total += average * weight
        details.append({
            "label": label,
            "name": TASK_NAMES[label],
            "ml_score": ml,
            "dl_score": dl,
            "points": round(average * weight, 2),
        })
    return min(total, 30), details


def grade_of(score):
    if score <= 40:
        return "LOW"
    if score <= 60:
        return "MID"
    return "HIGH"


def calculate_score(age, physical_level, chronic_disease, work_hour_limit, ml_scores, dl_scores):
    task_total, task_details = task_points(ml_scores, dl_scores)

    factors = [
        {"name": "나이", "points": round(age_points(age), 2), "max": 20},
        {"name": "건강 상태", "points": round(health_points(physical_level), 2), "max": 25},
        {"name": "만성질환", "points": chronic_points(chronic_disease), "max": 15},
        {"name": "근무 가능 시간", "points": round(work_hour_points(work_hour_limit), 2), "max": 10},
        {"name": "작업 특성 (ML+DL)", "points": round(task_total, 2), "max": 30},
    ]

    total = sum(factor["points"] for factor in factors)
    score = int(round(total))
    score = max(0, min(100, score))

    return {
        "risk_score": score,
        "risk_grade": grade_of(score),
        "factors": factors,
        "task_scores": task_details,
    }

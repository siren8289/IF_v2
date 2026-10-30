"""개인 입력과 ML/DL 작업 특성 점수로 0~100점 참고 지수를 계산한다.

사고 확률이 아니라, 정해 둔 규칙(가중치)으로 더한 참고용 점수다.
다섯 칸을 더하면 최대 100점이다.

  나이 20 + 건강 25 + 만성질환 15 + 근무시간 10 + 작업 특성 30 = 100
"""

# 작업 특성별 가중치. 모델이 준 0~1 점수에 이 숫자를 곱한다.
# 예: 운전 점수가 1.0(확실)이면 10점, 0.5면 5점.
# 여섯 가중치를 다 더하면 48이지만, 나중에 30점을 넘지 않게 자른다.
# 사무(OFFICE_TASK)는 여기 없다. 위험 가점으로 보지 않기 때문이다.
TASK_WEIGHTS = {
    "DRIVING": 10,              # 운전
    "NIGHT_SHIFT": 8,           # 야간 근무
    "WALKING": 8,               # 장시간 보행
    "CLEANING_TASK": 8,         # 청소
    "CARE_TASK": 6,             # 돌봄
    "FACILITY_MAINTENANCE": 8,  # 시설 관리
}

# 화면과 설명 문장에 보여줄 한국어 이름. 모델은 영어 코드만 안다.
TASK_NAMES = {
    "DRIVING": "운전",
    "NIGHT_SHIFT": "야간 근무",
    "WALKING": "장시간 보행",
    "CLEANING_TASK": "청소",
    "CARE_TASK": "돌봄",
    "FACILITY_MAINTENANCE": "시설 관리",
}


def age_points(age):
    """60세 이하 0점, 90세 이상 20점, 그 사이는 나이에 비례한다.

    61세는 20/30점, 75세는 10점, 90세는 20점이다.
    (나이 - 60) / 30 * 20 과 같다.
    """
    if age <= 60:
        return 0
    if age >= 90:
        return 20
    # 60세와 90세 사이 30년을 0~20점에 고르게 나눈다.
    return (age - 60) * 20 / 30


def health_points(physical_level):
    """건강 상태 1(좋음)~5(나쁨)를 0~25점으로 바꾼다.

    1 → 0점, 2 → 6.25점, 3 → 12.5점, 4 → 18.75점, 5 → 25점.
    """
    return (physical_level - 1) * 25 / 4


def chronic_points(chronic_disease):
    """만성질환이 있으면 15점, 없으면 0점. 중간 값은 없다."""
    return 15 if chronic_disease else 0


def work_hour_points(work_hour_limit):
    """하루 8시간 이상 일할 수 있으면 0점, 1시간이면 10점.

    일할 수 있는 시간이 짧을수록 부담이 크다고 보고 점수를 올린다.
    7시간 차이(8-1)를 10점에 나눠, 1시간 줄 때마다 약 1.43점이다.
    """
    if work_hour_limit >= 8:
        return 0
    return (8 - work_hour_limit) * 10 / 7


def task_points(ml_scores, dl_scores):
    """ML과 DL 점수의 평균에 가중치를 곱해서 더한다. 최대 30점.

    모델이 어떤 특성을 빠뜨려도 .get(..., 0) 때문에 0점으로 처리한다.
    """
    total = 0
    details = []
    for label, weight in TASK_WEIGHTS.items():
        # 두 모델이 같은 특성에 준 점수. 없으면 0.
        ml = ml_scores.get(label, 0)
        dl = dl_scores.get(label, 0)
        # 한쪽에만 치우치지 않게 평균을 쓴다.
        average = (ml + dl) / 2
        total += average * weight
        # 결과 화면의 "직무 특성" 표에 넣을 상세 값.
        details.append({
            "label": label,
            "name": TASK_NAMES[label],
            "ml_score": ml,
            "dl_score": dl,
            "points": round(average * weight, 2),
        })
    # 가중치 합은 48까지 갈 수 있으므로, 이 칸의 상한인 30으로 자른다.
    return min(total, 30), details


def grade_of(score):
    """점수를 세 등급으로 나눈다. LOW 0~40, MID 41~60, HIGH 61~100."""
    if score <= 40:
        return "LOW"
    if score <= 60:
        return "MID"
    return "HIGH"


def calculate_score(age, physical_level, chronic_disease, work_hour_limit, ml_scores, dl_scores):
    """다섯 항목을 더해 최종 점수와 등급을 만든다. main.py가 이 함수를 부른다."""
    task_total, task_details = task_points(ml_scores, dl_scores)

    # 화면의 "점수 구성" 막대그래프가 이 목록을 그대로 그린다.
    # points는 실제로 받은 점수, max는 그 칸의 만점.
    factors = [
        {"name": "나이", "points": round(age_points(age), 2), "max": 20},
        {"name": "건강 상태", "points": round(health_points(physical_level), 2), "max": 25},
        {"name": "만성질환", "points": chronic_points(chronic_disease), "max": 15},
        {"name": "근무 가능 시간", "points": round(work_hour_points(work_hour_limit), 2), "max": 10},
        {"name": "작업 특성 (ML+DL)", "points": round(task_total, 2), "max": 30},
    ]

    # 다섯 칸을 더한다. 반올림해서 정수 점수로 만든다.
    total = sum(factor["points"] for factor in factors)
    score = int(round(total))
    # 계산 실수로 0 미만이나 100 초과가 나와도 화면 범위 안에 가둔다.
    score = max(0, min(100, score))

    return {
        "risk_score": score,          # 0~100 정수
        "risk_grade": grade_of(score),  # LOW / MID / HIGH
        "factors": factors,           # 항목별 점수
        "task_scores": task_details,  # 특성별 ML/DL 점수
    }

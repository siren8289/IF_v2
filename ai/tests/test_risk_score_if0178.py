# IF-0178~IF-0246. risk_score 순수 함수만 호출한다. DB에는 연결하지 않는다.
from src.risk_score import (
    age_points,
    calculate_score,
    chronic_points,
    grade_of,
    health_points,
    task_points,
    work_hour_points,
)

LABELS = (
    "DRIVING",
    "NIGHT_SHIFT",
    "WALKING",
    "CLEANING_TASK",
    "CARE_TASK",
    "FACILITY_MAINTENANCE",
)


def near8(actual, expected):
    """시트에 적힌 소수 8자리와 같은지 본다."""
    assert f"{float(actual):.8f}" == f"{float(expected):.8f}"


def bind(tc_id, fn):
    name = "test_" + tc_id.replace("-", "_")
    fn.__name__ = name
    globals()[name] = fn


def _age(age, expected):
    def test_case():
        near8(age_points(age), expected)

    return test_case


for tc_id, age, expected in (
    ("IF-0178", 0, 0),
    ("IF-0179", 1, 0),
    ("IF-0180", 59, 0),
    ("IF-0181", 60, 0),
    ("IF-0182", 61, 0.66666667),
    ("IF-0183", 72, 8),
    ("IF-0184", 89, 19.33333333),
    ("IF-0185", 90, 20),
    ("IF-0186", 91, 20),
    ("IF-0187", 120, 20),
):
    bind(tc_id, _age(age, expected))


def _health(level, expected):
    def test_case():
        near8(health_points(level), expected)

    return test_case


for tc_id, level, expected in (
    ("IF-0188", 1, 0.0),
    ("IF-0189", 2, 6.25),
    ("IF-0190", 3, 12.5),
    ("IF-0191", 4, 18.75),
    ("IF-0192", 5, 25.0),
):
    bind(tc_id, _health(level, expected))


def _chronic(value, expected):
    def test_case():
        near8(chronic_points(value), expected)

    return test_case


bind("IF-0193", _chronic(False, 0))
bind("IF-0194", _chronic(True, 15))


def _hours(hours, expected):
    def test_case():
        near8(work_hour_points(hours), expected)

    return test_case


for tc_id, hours, expected in (
    ("IF-0195", 1, 10),
    ("IF-0196", 2, 8.57142857),
    ("IF-0197", 6, 2.85714286),
    ("IF-0198", 7, 1.42857143),
    ("IF-0199", 8, 0),
    ("IF-0200", 9, 0),
    ("IF-0201", 24, 0),
):
    bind(tc_id, _hours(hours, expected))


def _task(label, ml, dl, expected):
    def test_case():
        ml_scores = {name: 0 for name in LABELS}
        dl_scores = {name: 0 for name in LABELS}
        ml_scores[label] = ml
        dl_scores[label] = dl
        total, details = task_points(ml_scores, dl_scores)
        points = {row["label"]: row["points"] for row in details}
        assert set(points) == set(LABELS)
        near8(points[label], expected)
        for name in LABELS:
            if name != label:
                near8(points[name], 0)
        # 나머지 라벨은 0이라 라벨 점수와 전체 점수가 같다. 상한 30 미만이다.
        near8(total, expected)
        assert total < 30

    return test_case


_TASK_ROWS = (
    ("DRIVING", 0, 0, 0),
    ("DRIVING", 1, 0, 5),
    ("DRIVING", 0, 1, 5),
    ("DRIVING", 0.2, 0.8, 5),
    ("DRIVING", 1, 1, 10),
    ("NIGHT_SHIFT", 0, 0, 0),
    ("NIGHT_SHIFT", 1, 0, 4),
    ("NIGHT_SHIFT", 0, 1, 4),
    ("NIGHT_SHIFT", 0.2, 0.8, 4),
    ("NIGHT_SHIFT", 1, 1, 8),
    ("WALKING", 0, 0, 0),
    ("WALKING", 1, 0, 4),
    ("WALKING", 0, 1, 4),
    ("WALKING", 0.2, 0.8, 4),
    ("WALKING", 1, 1, 8),
    ("CLEANING_TASK", 0, 0, 0),
    ("CLEANING_TASK", 1, 0, 4),
    ("CLEANING_TASK", 0, 1, 4),
    ("CLEANING_TASK", 0.2, 0.8, 4),
    ("CLEANING_TASK", 1, 1, 8),
    ("CARE_TASK", 0, 0, 0),
    ("CARE_TASK", 1, 0, 3),
    ("CARE_TASK", 0, 1, 3),
    ("CARE_TASK", 0.2, 0.8, 3),
    ("CARE_TASK", 1, 1, 6),
    ("FACILITY_MAINTENANCE", 0, 0, 0),
    ("FACILITY_MAINTENANCE", 1, 0, 4),
    ("FACILITY_MAINTENANCE", 0, 1, 4),
    ("FACILITY_MAINTENANCE", 0.2, 0.8, 4),
    ("FACILITY_MAINTENANCE", 1, 1, 8),
)

for offset, row in enumerate(_TASK_ROWS):
    bind(f"IF-{202 + offset:04d}", _task(*row))


def _grade(score, expected):
    def test_case():
        assert grade_of(score) == expected

    return test_case


for tc_id, score, expected in (
    ("IF-0232", 0, "LOW"),
    ("IF-0233", 39, "LOW"),
    ("IF-0234", 40, "LOW"),
    ("IF-0235", 41, "MID"),
    ("IF-0236", 59, "MID"),
    ("IF-0237", 60, "MID"),
    ("IF-0238", 61, "HIGH"),
    ("IF-0239", 100, "HIGH"),
):
    bind(tc_id, _grade(score, expected))


def _total(age, health, chronic, hours, task_value, factors, score, grade):
    def test_case():
        same = {name: task_value for name in LABELS}
        result = calculate_score(age, health, chronic, hours, same, same)
        got = [item["points"] for item in result["factors"]]
        assert len(got) == len(factors)
        for actual, expected in zip(got, factors):
            near8(actual, expected)
        assert result["risk_score"] == score
        assert result["risk_grade"] == grade

    return test_case


for tc_id, args in (
    ("IF-0240", (60, 1, False, 8, 0, (0, 0, 0, 0, 0), 0, "LOW")),
    ("IF-0241", (60, 3, False, 8, 0, (0, 12.5, 0, 0, 0), 12, "LOW")),
    ("IF-0242", (60, 1, True, 8, 0, (0, 0, 15, 0, 0), 15, "LOW")),
    ("IF-0243", (90, 1, False, 8, 0, (20, 0, 0, 0, 0), 20, "LOW")),
    ("IF-0244", (90, 5, True, 1, 0, (20, 25, 15, 10, 0), 70, "HIGH")),
    ("IF-0245", (60, 1, False, 8, 1, (0, 0, 0, 0, 30), 30, "LOW")),
    ("IF-0246", (90, 5, True, 1, 1, (20, 25, 15, 10, 30), 100, "HIGH")),
):
    bind(tc_id, _total(*args))


import pytest

from src.features.f001_job_task.predict_f001 import predict_f001


def test_integrated_prediction():
    result = predict_f001("야간 배송기사 모집")

    assert result["feature_id"] == "AI-F-001"
    assert result["title"] == "야간 배송기사 모집"
    assert result["job_classification"]["category"] == "DRIVING"

    tasks = result["task_analysis"]["task_characteristics"]
    candidates = {
        item["label"]
        for item in tasks
        if item["candidate"]
    }

    assert "DRIVING" in candidates
    assert "NIGHT_SHIFT" in candidates
    assert result["experimental"] is True
    assert result["review_required"] is True


@pytest.mark.parametrize("title", ["", "   "])
def test_empty_title(title):
    with pytest.raises(ValueError):
        predict_f001(title)


def test_output_structure():
    result = predict_f001("요양보호사 채용")

    assert "job_classification" in result
    assert "task_analysis" in result

    classification = result["job_classification"]

    assert classification["score_type"] == "decision_function"
    assert len(classification["alternatives"]) == 3

    tasks = result["task_analysis"]["task_characteristics"]

    assert len(tasks) == 7
    assert all(
        0 <= item["score"] <= 1
        for item in tasks
    )

# IF-0256~IF-0268. 실제 task_ml.joblib, task_cnn.pt는 열거나 바꾸지 않는다.
import logging
from pathlib import Path

import pytest
import torch

import src.dl_model as dl_model
import src.ml_model as ml_model
from src.dl_model import TaskCNN, encode_title

REAL_MODELS = (ml_model.MODEL_PATH, dl_model.MODEL_PATH)


@pytest.fixture(autouse=True)
def isolate_model_cache(monkeypatch):
    monkeypatch.setattr(ml_model, "_models", None)
    monkeypatch.setattr(dl_model, "_model", None)
    monkeypatch.setattr(dl_model, "_vocab", None)
    monkeypatch.setattr(dl_model, "_labels", None)


@pytest.fixture(scope="module", autouse=True)
def real_model_files_stay():
    before = {
        path: (path.stat().st_size, path.stat().st_mtime_ns)
        for path in REAL_MODELS
    }
    yield
    for path, (size, mtime) in before.items():
        assert path.is_file()
        assert (path.stat().st_size, path.stat().st_mtime_ns) == (size, mtime)


class FakeClassifier:
    def __init__(self, positive):
        self.positive = positive
        self.titles = []

    def predict_proba(self, titles):
        self.titles.extend(titles)
        return [[1 - self.positive, self.positive]]


def test_IF_0256_ml_loads_once(monkeypatch):
    calls = []

    def fake_load(path):
        calls.append(path)
        return {"models": {"DRIVING": FakeClassifier(0.2)}}

    monkeypatch.setattr(ml_model.joblib, "load", fake_load)
    loaded = ml_model.load_ml_models()
    assert len(calls) == 1
    assert loaded is ml_model._models
    assert "DRIVING" in loaded


def test_IF_0257_ml_second_call_uses_cache(monkeypatch):
    calls = []

    def fake_load(path):
        calls.append(path)
        return {"models": {"DRIVING": FakeClassifier(0.2)}}

    monkeypatch.setattr(ml_model.joblib, "load", fake_load)
    first = ml_model.load_ml_models()
    second = ml_model.load_ml_models()
    assert first is second
    assert len(calls) == 1


def test_IF_0258_ml_probabilities_stay_in_unit_interval(monkeypatch):
    driving = FakeClassifier(0.75)
    night = FakeClassifier(0.0)

    def fake_load(path):
        return {"models": {"DRIVING": driving, "NIGHT_SHIFT": night}}

    monkeypatch.setattr(ml_model.joblib, "load", fake_load)
    scores = ml_model.predict_ml("운전기사")
    assert driving.titles == ["운전기사"]
    assert night.titles == ["운전기사"]
    assert set(scores) == {"DRIVING", "NIGHT_SHIFT"}
    assert scores["DRIVING"] == 0.75
    assert scores["NIGHT_SHIFT"] == 0.0
    assert all(0 <= value <= 1 for value in scores.values())


def test_IF_0259_missing_ml_file(monkeypatch, caplog):
    missing = Path("/tmp/if-v2-if0259-task_ml.joblib")
    missing.unlink(missing_ok=True)
    monkeypatch.setattr(ml_model, "MODEL_PATH", missing)
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(FileNotFoundError):
            ml_model.load_ml_models()
    assert ml_model._models is None
    assert caplog.records, "시트 기대는 오류와 함께 로그다"


def _checkpoint():
    vocab = {"가": 2}
    labels = ["DRIVING"]
    model = TaskCNN(vocab_size=len(vocab) + 2, num_labels=len(labels))
    return {
        "vocab": vocab,
        "labels": labels,
        "model_state_dict": model.state_dict(),
    }


def test_IF_0260_empty_title_pads_to_100():
    encoded = encode_title("", {"가": 2})
    assert encoded == [0] * 100
    assert len(encoded) == 100


def test_IF_0261_one_char_and_99_padding():
    encoded = encode_title("가", {"가": 5})
    assert encoded == [5] + [0] * 99
    assert len(encoded) == 100


def test_IF_0262_100_chars_keep_length():
    encoded = encode_title("가" * 100, {"가": 5})
    assert encoded == [5] * 100
    assert len(encoded) == 100


def test_IF_0263_101st_char_is_cut():
    title = ("가" * 100) + "나"
    encoded = encode_title(title, {"가": 5, "나": 6})
    assert len(title) == 101
    assert encoded == [5] * 100
    assert 6 not in encoded


def test_IF_0264_unknown_char_is_id_1():
    encoded = encode_title("Z", {"가": 5})
    assert encoded[0] == 1
    assert encoded[1:] == [0] * 99


def test_IF_0265_dl_loads_once_then_eval(monkeypatch):
    calls = []
    evals = []
    original_eval = TaskCNN.eval

    def fake_load(path, map_location=None, weights_only=None):
        calls.append((path, map_location, weights_only))
        return _checkpoint()

    def counting_eval(self):
        evals.append(self)
        return original_eval(self)

    monkeypatch.setattr(dl_model.torch, "load", fake_load)
    monkeypatch.setattr(TaskCNN, "eval", counting_eval)
    model, vocab, labels = dl_model.load_dl_model()
    assert len(calls) == 1
    assert calls[0][1] == "cpu"
    assert calls[0][2] is True
    assert evals == [model]
    assert model.training is False
    assert vocab == {"가": 2}
    assert labels == ["DRIVING"]


def test_IF_0266_dl_second_call_keeps_cache(monkeypatch):
    calls = []

    def fake_load(path, map_location=None, weights_only=None):
        calls.append(path)
        return _checkpoint()

    monkeypatch.setattr(dl_model.torch, "load", fake_load)
    first = dl_model.load_dl_model()
    second = dl_model.load_dl_model()
    assert first[0] is second[0]
    assert first[1] is second[1]
    assert first[2] is second[2]
    assert len(calls) == 1


def test_IF_0267_dl_sigmoid_stays_in_unit_interval(monkeypatch):
    logits = torch.tensor([[1.0, -1.0]])

    class Net(torch.nn.Module):
        def forward(self, x):
            return logits

    def fake_load():
        return Net(), {char: index + 2 for index, char in enumerate("운전기사")}, ["DRIVING", "CARE_TASK"]

    monkeypatch.setattr(dl_model, "load_dl_model", fake_load)
    scores = dl_model.predict_dl("운전기사")
    expected = [round(value, 4) for value in torch.sigmoid(logits)[0].tolist()]
    assert scores == {"DRIVING": expected[0], "CARE_TASK": expected[1]}
    assert all(0 <= value <= 1 for value in scores.values())


def test_IF_0268_missing_dl_file(monkeypatch, caplog):
    missing = Path("/tmp/if-v2-if0268-task_cnn.pt")
    missing.unlink(missing_ok=True)
    monkeypatch.setattr(dl_model, "MODEL_PATH", missing)
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(FileNotFoundError):
            dl_model.load_dl_model()
    assert dl_model._model is None
    assert caplog.records, "시트 기대는 서버 오류 기록이다"

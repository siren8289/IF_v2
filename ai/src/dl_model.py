"""DL 모델: PyTorch 문자 단위 CNN으로 직무 제목에서 작업 특성 점수를 예측한다."""
from pathlib import Path

import torch
from torch import nn

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "task_cnn.pt"
MAX_LENGTH = 100


class TaskCNN(nn.Module):
    """학습할 때 쓴 구조와 똑같아야 저장된 가중치를 불러올 수 있다."""

    def __init__(self, vocab_size, num_labels):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 64, padding_idx=0)
        self.conv = nn.Conv1d(64, 128, kernel_size=3, padding=1)
        self.activation = nn.ReLU()
        self.classifier = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, num_labels),
        )

    def forward(self, x):
        x = self.embedding(x)        # (배치, 글자수, 64)
        x = x.transpose(1, 2)        # (배치, 64, 글자수)
        x = self.activation(self.conv(x))
        x = torch.amax(x, dim=2)     # 글자 방향으로 가장 큰 값만 남긴다
        return self.classifier(x)


def encode_title(title, vocab):
    """글자를 숫자로 바꾸고 길이를 MAX_LENGTH로 맞춘다. 모르는 글자는 1, 빈칸은 0."""
    numbers = [vocab.get(char, 1) for char in title[:MAX_LENGTH]]
    numbers += [0] * (MAX_LENGTH - len(numbers))
    return numbers


_model = None
_vocab = None
_labels = None


def load_dl_model():
    global _model, _vocab, _labels
    if _model is None:
        checkpoint = torch.load(MODEL_PATH, map_location="cpu", weights_only=True)
        _vocab = checkpoint["vocab"]
        _labels = checkpoint["labels"]
        _model = TaskCNN(vocab_size=len(_vocab) + 2, num_labels=len(_labels))
        _model.load_state_dict(checkpoint["model_state_dict"])
        _model.eval()
    return _model, _vocab, _labels


def predict_dl(title):
    """라벨별 점수(0~1)를 딕셔너리로 돌려준다."""
    model, vocab, labels = load_dl_model()
    x = torch.tensor([encode_title(title, vocab)], dtype=torch.long)

    with torch.no_grad():
        logits = model(x)
        probabilities = torch.sigmoid(logits)[0].tolist()

    scores = {}
    for label, probability in zip(labels, probabilities):
        scores[label] = round(float(probability), 4)
    return scores

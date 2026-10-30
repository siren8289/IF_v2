"""DL 모델: PyTorch 문자 단위 CNN으로 직무 제목에서 작업 특성 점수를 예측한다.

DL은 Deep Learning이다. ML과 같은 질문(이 제목에 운전이 있나?)을
글자 하나하나를 보는 신경망으로 다시 답한다.
두 답을 나중에 평균 내서 한쪽 모델만 믿지 않는다.

저장된 가중치 파일은 ai/models/task_cnn.pt 이다.
"""
from pathlib import Path

import torch
# nn: 신경망 층을 조립하는 파이토치 도구 모음.
from torch import nn

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "task_cnn.pt"
# 제목은 앞에서 100글자만 본다. 더 짧으면 뒤를 0으로 채운다.
MAX_LENGTH = 100


class TaskCNN(nn.Module):
    """학습할 때 쓴 구조와 똑같아야 저장된 가중치를 불러올 수 있다.

    글자 → 숫자 벡터 → 주변 글자를 함께 보는 필터 → 특성별 점수.
    """

    def __init__(self, vocab_size, num_labels):
        super().__init__()
        # 글자 번호마다 64칸짜리 숫자 벡터를 둔다. 0번은 빈칸(패딩)이라 학습하지 않는다.
        self.embedding = nn.Embedding(vocab_size, 64, padding_idx=0)
        # 이웃한 3글자를 함께 보고 128개의 특징을 뽑는 필터.
        self.conv = nn.Conv1d(64, 128, kernel_size=3, padding=1)
        # 음수는 0으로 지워서, "있는 특징"만 다음 층으로 넘긴다.
        self.activation = nn.ReLU()
        # 128개 특징을 줄여 라벨 개수만큼의 점수로 바꾼다.
        # Dropout은 학습 때 일부를 일부러 빼는 장치다. 예측 때는 꺼진다.
        self.classifier = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, num_labels),
        )

    def forward(self, x):
        """숫자로 바뀐 제목 한 묶음을 받아 라벨별 원점수를 낸다."""
        x = self.embedding(x)        # (배치, 글자수, 64)
        x = x.transpose(1, 2)        # Conv1d는 (배치, 채널, 길이) 순서를 원한다.
        x = self.activation(self.conv(x))
        # 글자 위치마다 나온 값 중 가장 큰 것만 남긴다.
        # "제목 어딘가에 그 특징이 있으면" 잡히게 하려는 처리다.
        x = torch.amax(x, dim=2)
        return self.classifier(x)


def encode_title(title, vocab):
    """글자를 숫자로 바꾸고 길이를 MAX_LENGTH로 맞춘다.

    vocab에 있는 글자는 그 번호, 모르는 글자는 1, 모자란 자리는 0이다.
    """
    numbers = [vocab.get(char, 1) for char in title[:MAX_LENGTH]]
    numbers += [0] * (MAX_LENGTH - len(numbers))
    return numbers


# 처음 예측 때 한 번만 채운다. 요청마다 파일을 다시 읽지 않는다.
_model = None
_vocab = None
_labels = None


def load_dl_model():
    """가중치, 글자 사전, 라벨 목록을 파일에서 읽는다."""
    global _model, _vocab, _labels
    if _model is None:
        # map_location="cpu": GPU 없이 학습한 파일이어도 이 컴퓨터 CPU에서 연다.
        # weights_only=True: 가중치만 읽고, 파일 안의 임의 코드는 실행하지 않는다.
        checkpoint = torch.load(MODEL_PATH, map_location="cpu", weights_only=True)
        _vocab = checkpoint["vocab"]
        _labels = checkpoint["labels"]
        # +2는 0(빈칸)과 1(모르는 글자) 자리를 사전 크기 밖에 두었기 때문이다.
        _model = TaskCNN(vocab_size=len(_vocab) + 2, num_labels=len(_labels))
        _model.load_state_dict(checkpoint["model_state_dict"])
        # eval(): 드롭아웃을 끄고 예측 모드로 전환한다.
        _model.eval()
    return _model, _vocab, _labels


def predict_dl(title):
    """라벨별 점수(0~1)를 딕셔너리로 돌려준다. ML 결과와 같은 모양이다."""
    model, vocab, labels = load_dl_model()
    # 제목 1건을 텐서(숫자 표)로 만든다. 배치 차원이 필요해서 리스트로 한 번 감싼다.
    x = torch.tensor([encode_title(title, vocab)], dtype=torch.long)

    # 예측만 하므로 기울기(학습용 계산)는 만들지 않는다.
    with torch.no_grad():
        logits = model(x)
        # 시그모이드는 어떤 실수든 0~1 사이 확률처럼 눌러 준다.
        # 라벨이 여러 개라, 한 제목이 운전이면서 야간일 수도 있다.
        probabilities = torch.sigmoid(logits)[0].tolist()

    scores = {}
    for label, probability in zip(labels, probabilities):
        scores[label] = round(float(probability), 4)
    return scores

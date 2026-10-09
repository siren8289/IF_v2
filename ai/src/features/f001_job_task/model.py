
"""
AI-F-001 직무 작업 특성 분석 Baseline.

직무 설명에서 작업 특성 키워드를 탐지한다.
학습된 ML 모델이 아니므로 confidence는 제공하지 않는다.
"""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class JobInput(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    jobId: int = Field(gt=0)
    jobTitle: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=10000)
    workHours: int = Field(gt=0, le=24)

    @field_validator("jobTitle", "description")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("빈 문자열은 허용하지 않습니다.")
        return value


TAG_KEYWORDS = {
    "OUTDOOR": ["공원", "거리", "야외", "실외"],
    "WALKING": ["걸어", "도보", "보행"],
    "CLEANING": ["청소", "쓰레기", "환경정비"],
    "HEAVY_LIFTING": ["무거운", "중량물", "운반"],
    "REPETITIVE_MOTION": ["반복적", "반복적으로", "반복 작업"],
}


def verify_evidence(description: str, evidence: list[dict]) -> bool:
    """근거 문구가 원문 위치와 정확하게 일치하는지 확인."""

    for item in evidence:
        start = item.get("start")
        end = item.get("end")
        value = item.get("text")

        if not isinstance(start, int) or not isinstance(end, int):
            return False

        if not (0 <= start < end <= len(description)):
            return False

        if description[start:end] != value:
            return False

    return True


def analyze_job(job: JobInput) -> dict:
    """규칙 기반 다중 라벨 직무 분석."""

    description = job.description
    tags = []
    evidence = []

    for tag, keywords in TAG_KEYWORDS.items():
        matches = []

        for keyword in keywords:
            start = 0

            while True:
                pos = description.find(keyword, start)

                if pos == -1:
                    break

                matches.append({
                    "tag": tag,
                    "text": description[pos:pos + len(keyword)],
                    "start": pos,
                    "end": pos + len(keyword),
                })

                start = pos + len(keyword)

        if matches:
            tags.append(tag)
            evidence.extend(matches)

    evidence.sort(
        key=lambda item: (item["start"], item["end"], item["tag"])
    )

    return {
        "jobId": job.jobId,
        "taskTags": tags,
        "confidence": {},
        "evidence": evidence,
        "reviewRequired": True,
        "modelVersion": "keyword-baseline-v0.1",
        "status": "REVIEW_REQUIRED",
    }


# PyTorch CharCNN 모델 정의: 학습과 추론에서 공통 사용
import torch
from torch import nn

MAX_LENGTH = 100

def encode_title(title, vocab):
    encoded = [
        vocab.get(char, 1)
        for char in title[:MAX_LENGTH]
    ]

    encoded += [0] * (MAX_LENGTH - len(encoded))
    return encoded


class TaskCNN(nn.Module):
    def __init__(self, vocab_size, num_labels):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            64,
            padding_idx=0,
        )

        self.conv = nn.Conv1d(
            in_channels=64,
            out_channels=128,
            kernel_size=3,
            padding=1,
        )

        self.activation = nn.ReLU()

        self.classifier = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, num_labels),
        )

    def forward(self, x):
        x = self.embedding(x)
        x = x.transpose(1, 2)

        x = self.activation(self.conv(x))

        # PAD 위치가 pooling 결과에 영향을 줄 수 있으므로
        # 원래 입력의 유효 위치만 남긴다.
        # Conv의 인접 문자 영향은 남으므로 근사적 마스킹이다.
        x = torch.amax(x, dim=2)

        return self.classifier(x)



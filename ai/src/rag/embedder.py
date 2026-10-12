"""텍스트 임베딩(Embedding) 모듈.

텍스트를 의미 기반의 숫자 벡터(vector)로 변환합니다.
GEMINI_API_KEY가 있으면 Gemini 임베딩 모델(text-embedding-004)을 사용하고,
API 키가 없거나 테스트 환경에서는 일관된 로컬 벡터 변환기(Fallback)를 사용합니다.
"""
import hashlib
import os
import numpy as np


def _local_fallback_embedding(text: str, dimension: int = 768) -> list[float]:
    """API 키가 없을 때 사용하는 로컬 결정론적 임베딩 생성기입니다.
    
    문장의 형태소 및 단어 해시를 기반으로 768차원의 단위 벡터를 생성합니다.
    같은 문장은 항상 같은 벡터를 돌려주며, 키워드가 겹치는 문장은 코사인 유사도가 높게 나옵니다.
    """
    clean = text.strip().lower()
    vector = np.zeros(dimension, dtype=np.float32)

    words = clean.split()
    if not words:
        return vector.tolist()

    for word in words:
        # 단어 해시값으로 벡터 인덱스들을 결정하여 값을 누적
        seed = int(hashlib.md5(word.encode("utf-8")).hexdigest(), 16)
        index = seed % dimension
        vector[index] += 1.0
        # 인접 인덱스에도 약간의 분산 효과 부여
        vector[(index + 1) % dimension] += 0.5

    # L2 정규화 (길이가 1인 단위 벡터로 변환)
    norm = np.linalg.norm(vector)
    if norm > 0:
        vector = vector / norm

    return vector.tolist()


def embed_text(text: str) -> list[float]:
    """한 줄의 텍스트를 임베딩 벡터로 변환합니다.
    
    반환값:
        768차원 부동소수점 리스트 [0.012, -0.045, ...]
    """
    api_key = os.getenv("GEMINI_API_KEY", "")
    if api_key:
        try:
            from google import genai

            client = genai.Client(api_key=api_key)
            result = client.models.embed_content(
                model="text-embedding-004",
                contents=text,
            )
            # Gemini 응답에서 임베딩 벡터 추출
            if hasattr(result, "embedding") and hasattr(result.embedding, "values"):
                return [float(v) for v in result.embedding.values]
            if hasattr(result, "embeddings") and result.embeddings:
                return [float(v) for v in result.embeddings[0].values]
        except Exception as error:
            print(f"Gemini 임베딩 호출 실패, 로컬 임베딩을 사용합니다: {error}")

    return _local_fallback_embedding(text)


def embed_texts(texts: list[str]) -> list[list[float]]:
    """여러 텍스트를 한 번에 임베딩 벡터 목록으로 변환합니다."""
    return [embed_text(t) for t in texts]


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    """두 벡터 사이의 코사인 유사도를 계산합니다 (-1.0 ~ 1.0)."""
    a = np.array(vector_a, dtype=np.float32)
    b = np.array(vector_b, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))

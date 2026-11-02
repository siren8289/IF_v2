"""텍스트 임베딩(Embedding) 모듈.

임베딩은 문장을 긴 숫자 목록(벡터)으로 바꾸는 일이다.
뜻이 비슷한 문장은 숫자도 비슷해져서, 나중에 "이 질문과 가까운 지침"을 찾을 수 있다.

GEMINI_API_KEY가 있으면 Gemini 임베딩 모델(text-embedding-004)을 사용하고,
API 키가 없거나 호출이 실패하면 같은 문장은 항상 같은 숫자가 나오는
로컬 변환기를 쓴다. 로컬 변환기는 진짜 의미 분석이 아니라 단어 일치에 가깝다.
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
        # 같은 단어는 항상 같은 칸에 1을 더한다. md5는 단어를 고정된 숫자로 바꾸는 함수다.
        seed = int(hashlib.md5(word.encode("utf-8"), usedforsecurity=False).hexdigest(), 16)
        index = seed % dimension
        vector[index] += 1.0
        # 바로 옆 칸에도 조금 더해, 완전히 한 칸에만 몰리지 않게 한다.
        vector[(index + 1) % dimension] += 0.5

    # 벡터 길이를 1로 맞춘다. 그래야 긴 문장이 짧다는 이유만으로 점수가 커지지 않는다.
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
    """두 벡터가 같은 방향을 가리키는 정도. 1에 가까우면 비슷하고, 0이면 관계없다.

    길이는 무시하고 방향만 본다. 단어가 겹치는 문장일수록 값이 커진다.
    """
    a = np.array(vector_a, dtype=np.float32)
    b = np.array(vector_b, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))

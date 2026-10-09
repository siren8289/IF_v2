FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .

# 기본 torch는 GPU(CUDA) 파일까지 받아 수 GB가 되므로 CPU 버전만 설치한다.
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir \
      --index-url https://download.pytorch.org/whl/cpu \
      "torch>=2.6,<3"

COPY models ./models
COPY src ./src

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

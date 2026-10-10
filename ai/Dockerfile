# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# torch는 가장 크고 거의 바뀌지 않아서 먼저 따로 설치한다. (캐시 재사용)
RUN pip install --no-cache-dir \
      --index-url https://download.pytorch.org/whl/cpu \
      "torch>=2.6,<3"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY models ./models
COPY src ./src

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.docker.txt .

# CPU torch only — default PyPI torch pulls multi-GB CUDA wheels and OOMs t3.small.
RUN pip install --no-cache-dir -r requirements.docker.txt \
    && pip install --no-cache-dir \
      --index-url https://download.pytorch.org/whl/cpu \
      "torch>=2.6,<3"

COPY src ./src

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

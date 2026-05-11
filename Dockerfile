FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    streamlit \
    httpx \
    pydantic-settings \
    loguru

EXPOSE 8000
EXPOSE 8501
FROM node:20.14.0-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3 python3-venv python3-dev \
       gcc g++ gfortran \
       libsndfile1-dev libffi-dev \
       git \
    && python3 -m venv /opt/venv \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt
RUN pip install --no-cache-dir pytest==8.2.2

COPY . .

FROM python:3.11-slim

# Установить системные зависимости сразу в одном RUN
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libcairo2-dev \
    gdal-bin \
    libgdal-dev \
    libxml2-dev \
    libxslt-dev \
    pkg-config \
    python3-dev \
    libopenblas-dev \
    liblapack-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только requirements.txt отдельно
COPY requirements.txt .

# Установим сначала только Cython и numpy
RUN pip install --upgrade pip \
 && pip install Cython numpy

# Потом установим остальные зависимости
RUN pip install -r requirements.txt

# Копируем остальной код проекта
COPY . .

EXPOSE 8080

CMD ["gunicorn", "beckend_for_education.wsgi:application", "--bind", "0.0.0.0:8080"]
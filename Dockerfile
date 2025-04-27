FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
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

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install "setuptools<66"
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "beckend_for_education.wsgi:application", "--bind", "0.0.0.0:8080"]
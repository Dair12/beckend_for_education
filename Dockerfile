FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install "setuptools<66"
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "beckend_for_education.wsgi:application", "--bind", "0.0.0.0:8080"]
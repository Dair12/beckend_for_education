FROM python:3.10-slim

# Установка всех нужных системных библиотек
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    python3-dev \
    libsqlite3-dev \
    libjpeg-dev \
    zlib1g-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    cmake \
    && apt-get clean

# Копируем проект
COPY . .

# Устанавливаем Python зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8080

# Запуск приложения
CMD ["gunicorn", "beckend_for_education.wsgi:application", "--bind", "0.0.0.0:8080"]
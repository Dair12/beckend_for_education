# Используем официальный образ Python в качестве базового
FROM python:3.11-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install "setuptools<66"
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . /app/

# Открываем порт 8080
EXPOSE 8080

# Команда по умолчанию для запуска приложения
CMD ["gunicorn", "beckend_for_education.wsgi:application", "--bind", "0.0.0.0:8080"]

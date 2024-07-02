# Используем официальный образ Python
FROM python:3.8-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости проекта в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

# Запускаем приложение
CMD ["python", "./simple_server.py"]

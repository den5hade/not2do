# Not2Do API

REST API на базе FastAPI для приложения Not2Do, предоставляющий надежный бэкенд-сервис для управления задачами и отслеживания прогресса пользователей.

## 🚀 Возможности

- REST API на базе FastAPI с автоматической документацией OpenAPI
- Интеграция с MongoDB с использованием Beanie ODM
- Контейнеризация с помощью Docker для простого развертывания
- Поддержка CORS middleware
- Комплексная обработка ошибок и валидация
- Модели для отслеживания пользователей и прогресса

## 🛠️ Технический стек

- **Framework**: FastAPI
- **Database**: MongoDB
- **ORM**: Beanie (MongoDB ODM)
- **Containerization**: Docker & Docker Compose
- **API Documentation**: OpenAPI (Swagger UI)
- **Development Server**: Uvicorn

## 📋 Требования

- Docker и Docker Compose
- Python 3.8+ (для локальной разработки)

## 🚀 Начало работы

### Использование Docker (Рекомендуется)

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd not2do/api
```

2. Запустите приложение с помощью Docker Compose:
```bash
docker-compose up --build
```

API будет доступен по адресу `http://localhost:8000`
Документация API будет доступна по адресу `http://localhost:8000/api/v1/docs`

### Локальная разработка

1. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Запустите сервер разработки:
```bash
uvicorn app:app --reload
```

## 📁 Структура проекта

```
not2do/api/
├── api/            # Маршруты и эндпоинты API
├── core/           # Основные конфигурации и настройки
├── models/         # Модели базы данных
├── schemas/        # Pydantic схемы
├── services/       # Бизнес-логика и сервисы
├── app.py          # Основной файл приложения
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 🔧 Конфигурация

Приложение использует переменные окружения для конфигурации. Создайте файл `.env` в корневой директории со следующими переменными:

```
PROJECT_NAME=Not2Do
API_V1_STR=/api/v1
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
```

## 📚 Документация API

После запуска приложения вы можете получить доступ к:
- Swagger UI: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

## 🧪 Разработка

Приложение использует hot-reload для разработки, поэтому любые изменения в коде автоматически перезапускают сервер.

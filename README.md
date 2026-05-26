# Tourist Routes API

REST API для туристических маршрутов.

## Функционал

- CRUD для городов
- CRUD для маршрутов
- CRUD для отзывов
- Swagger документация
- Фильтрация маршрутов

## Технологии

- Python
- Django
- Django REST Framework
- drf-spectacular
- SQLite

## Эндпоинты

### Города

GET:
```text
/api/v1/cities/
```

POST:
```text
/api/v1/cities/
```

PATCH:
```text
/api/v1/cities/{id}/
```

DELETE:
```text
/api/v1/cities/{id}/
```

---

### Маршруты

GET:
```text
/api/v1/routes/
```

POST:
```text
/api/v1/routes/
```

PATCH:
```text
/api/v1/routes/{id}/
```

DELETE:
```text
/api/v1/routes/{id}/
```

---

### Отзывы

GET:
```text
/api/v1/reviews/
```

POST:
```text
/api/v1/reviews/
```

PATCH:
```text
/api/v1/reviews/{id}/
```

DELETE:
```text
/api/v1/reviews/{id}/
```

---

## Swagger

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## Установка проекта

Создание виртуального окружения:

```bash
python -m venv venv
```

Активация:

```bash
source venv/Scripts/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Миграции:

```bash
python manage.py migrate
```

Запуск проекта:

```bash
python manage.py runserver
```
# AWS-SECURE-BASELINE

Secure deployment pipeline in the cloud (AWS) for a Python Application.


## API skeleton

Django 5.2 + Django REST Framework API with a health check and CRUD endpoints for `Item`.

### Setup

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Configuration is read from the environment: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, and `DJANGO_DB_NAME`. With `DJANGO_DEBUG=0`, `DJANGO_SECRET_KEY` is required.

### Endpoints

- `GET /api/health/`
- `GET`, `POST /api/items/`
- `GET`, `PUT`, `PATCH`, `DELETE /api/items/<id>/`

### Tests

```bash
.venv/bin/python manage.py test
```

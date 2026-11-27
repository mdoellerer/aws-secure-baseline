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

---

## Dockerized version

Instead of installing/running locally we can run in dev or a (fake) prod using Dockerfile and docker compose

The commands to run only dev, only prod or both are shown below (choose one):

```bash

docker compose --build -d

docker compose -f compose.prod.yaml --env-file .env.prod up --build -d

docker compose -f compose.yaml -f compose.prod.yaml --env-file .env.prod up --build -d
```

Run the migrations

```bash
docker compose exec web python manage.py migrate
```

Collect static files

```bash
docker compose exec web python manage.py collectstatic --noinput
```

You can inspect the running container:

```bash
docker compose -f compose.yaml -f compose.prod.yaml ps
```


And view logs:

```bash
docker compose -f compose.yaml -f compose.prod.yaml logs -f web
```

---
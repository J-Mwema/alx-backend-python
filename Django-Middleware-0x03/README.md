# Django middleware and chat API

[Back to the repository overview](../README.md)

This Django REST Framework project is a chat API exercise. It models users,
conversations, and messages, and includes request middleware, authentication
helpers, permissions, filtering, pagination, API views, and smoke tests.

## Project layout

- [`chats/`](./chats/) — application code, models, API endpoints, middleware,
  permissions, and tests.
- [`messaging_app/`](./messaging_app/) — Django project configuration and URL
  routing.
- [`manage.py`](./manage.py) — Django management entry point.
- [`post_man-Collections`](./post_man-Collections) — Postman collection for
  trying the API.
- [`chats/tests.py`](./chats/tests.py) — API smoke tests.

## Run and test

Install Django and the Django REST Framework in a virtual environment, then
run commands from this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install django djangorestframework
python3 manage.py migrate
python3 manage.py runserver
```

Run the Django tests with:

```bash
python3 manage.py test
```

## Related project

The separate [messaging app project](../messaging_app/README.md) expands on
the chat API with its own tests and container/deployment configuration.

[All repository tasks](../README.md#project-map)

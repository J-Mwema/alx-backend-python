# Django messaging app

[Back to the repository overview](../README.md)

This project is a Django REST Framework API for user conversations and
messages. It includes a custom user model, conversation and message
endpoints, JWT-related helpers, participant permissions, filtering,
pagination, automated tests, and Docker/Kubernetes/CI configuration.

## Project layout

- [`chats/`](./chats/) — user, conversation, and message models; serializers;
  API views; permissions; filters; and tests.
- [`messaging_app/`](./messaging_app/README.md) — Django configuration and
  additional deployment/CI assets.
- [`manage.py`](./manage.py) — Django management entry point.
- [`requirements.txt`](./requirements.txt) — Python dependencies.
- [`pytest.ini`](./pytest.ini) — pytest and Django test configuration.
- [`docker-compose.yml`](./docker-compose.yml) and
  [`Dockerfile`](./Dockerfile) — container setup.
- [`Jenkinsfile`](./Jenkinsfile) and the
  [deployment manifests](./) — CI/CD and Kubernetes-related configuration.
- [`post_man-Collections`](./post_man-Collections) — Postman API requests.

## Run locally

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r messaging_app/requirements.txt
cd messaging_app
python3 manage.py migrate
python3 manage.py runserver
```

Run the test suite from the `messaging_app` directory:

```bash
pytest
```

The Compose setup is also available from this directory with
`docker compose up --build`. Consult the Compose file and Django settings for
the environment required by the selected database configuration. Do not
commit local secrets, virtual environments, or database files.

## Related project

- [Django middleware and chat API](../Django-Middleware-0x03/README.md)
- [All repository tasks](../README.md#project-map)

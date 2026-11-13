# Messaging app project configuration

[Back to the messaging app guide](../README.md) ·
[Back to the repository overview](../../README.md)

This directory contains the Django project package and additional deployment
and automation assets for the messaging API. The application code is in the
sibling [`chats/`](../chats/) directory.

## Contents

- [`settings.py`](./settings.py), [`urls.py`](./urls.py), [`asgi.py`](./asgi.py),
  and [`wsgi.py`](./wsgi.py) — Django project configuration and entry points.
- [`.github/workflows/`](./.github/workflows/) — GitHub Actions workflows.
- [`Dockerfile`](./Dockerfile) and
  [`docker-compose.yml`](./docker-compose.yml) — container configuration.
- [`Jenkinsfile`](./Jenkinsfile) — Jenkins pipeline configuration.
- [`deployment.yaml`](./deployment.yaml),
  [`blue_deployment.yaml`](./blue_deployment.yaml), and
  [`kubctl-0x01`](./kubctl-0x01) — deployment-related assets.
- [`post_man-Collections`](./post_man-Collections) — API request collection.

For installation, API usage, and the main application setup, see the
[messaging app guide](../README.md).

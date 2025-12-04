# messaging_app (Django project)

This folder contains the Django project for the Messaging App.

Key files:

- `Dockerfile` - defines the application image (base `python:3.10-slim`).
- `docker-compose.yml` - Compose file used to run the `web` and `db` services together.
- `.env` - environment variables used by Compose and Django (do not commit).
- `settings.py` - reads DB and secret config from environment variables when provided.

Docker usage (from this folder):

```bash
# ensure you have a local .env file (copy the provided .env template)
docker compose up --build

# run detached
docker compose up -d --build

# run a management command inside the running web container
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Persistence:
- The MySQL service mounts a named volume `mysql_data` to `/var/lib/mysql` so database data survives container restarts.

Environment / secrets:
- Keep secrets in `messaging_app/.env` (or a local `.env` not committed). The top-level README explains how to remove `.env` from git history if already pushed.

Troubleshooting tips:
- If migrations fail because the DB is not ready, check `docker compose logs db` for errors and ensure the `wait_for_db` management command is present (it is included in `chats/management/commands/wait_for_db.py`).
- If you change `requirements.txt`, rebuild the image: `docker compose build --no-cache web`.

If you want, I can also add a small `Makefile` or `entrypoint.sh` to simplify common tasks (migrate, collectstatic, createsuperuser).

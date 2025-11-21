# Messaging App (Django REST)

Lightweight messaging API built with Django and Django REST Framework. This app provides simple conversations and messages between users using a custom UUID-based `User` model.

## Overview

- Custom `User` model based on `AbstractUser` with UUID primary key, role, phone number and timestamps.
- `Conversation` model with many-to-many `participants` (users).
- `Message` model with UUID primary key, `sender` (FK to `User`), `conversation` (FK to `Conversation`), `message_body` and timestamp.

API endpoints are exposed under the `/api/` path (see `messaging_app/urls.py`).

## Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework

It's recommended to create an isolated virtual environment rather than committing `env/` to the repo.

## Quick setup

From the project root:

```bash
# create virtualenv (if you don't have one)
python3 -m venv .venv
source .venv/bin/activate

# install minimal deps
pip install django djangorestframework

# (optional) create a requirements.txt for reproducibility
pip freeze > requirements.txt

# make and apply migrations
python manage.py makemigrations
python manage.py migrate

# create a superuser to access the admin
python manage.py createsuperuser

# run the dev server
python manage.py runserver
```

## API routes (summary)

- List/create conversations: GET/POST /api/conversations/
- Retrieve/update/delete a conversation: GET/PUT/PATCH/DELETE /api/conversations/{id}/
- Add participants to a conversation (custom action): POST /api/conversations/{id}/add_participants/ with JSON body: `{"user_ids": ["<uuid>", ...]}`
- List/create messages: GET/POST /api/messages/
- Retrieve/update/delete a message: GET/PUT/PATCH/DELETE /api/messages/{id}/

Notes:
- To post a message, send POST /api/messages/ with JSON: `{"conversation": "<conversation-uuid>", "message_body": "Hello"}`. The current implementation uses `request.user` as the sender, so the request should be authenticated.
- Authentication and permission configuration is up to you (session, token, JWT). If you expect anonymous posting, adjust `MessageViewSet.create()` or permissions accordingly.

## Development notes

- `AUTH_USER_MODEL = 'chats.User'` is set in `messaging_app/settings.py`.
- The project currently uses SQLite (`db.sqlite3`) for development.
- `rest_framework` and `chats` are registered under `INSTALLED_APPS`.

## Git / repository hygiene

Do NOT commit the following (they are included in `.gitignore`):

- `env/`, `venv/` (virtual environments)
- `db.sqlite3` (local DB)
- `__pycache__/`, `*.py[cod]` (bytecode)
- `.env` (local secrets)

If `env/` or `db.sqlite3` were already committed, remove them from history before pushing publically (I can provide the commands if needed).

## Testing the API quickly (example)

You can use `curl` or a tool like HTTPie/Postman. Example (using session auth or a token as configured):

```bash
# create an empty conversation
curl -X POST http://127.0.0.1:8000/api/conversations/ -u username:password

# add participants to a conversation
curl -X POST http://127.0.0.1:8000/api/conversations/<conv-uuid>/add_participants/ \
	-H "Content-Type: application/json" \
	-d '{"user_ids":["<user-uuid1>","<user-uuid2>"]}' -u username:password

# send a message (authenticated)
curl -X POST http://127.0.0.1:8000/api/messages/ \
	-H "Content-Type: application/json" \
	-d '{"conversation":"<conv-uuid>","message_body":"Hello world"}' -u username:password
```

## Next steps / improvements

- Add API authentication (Token or JWT) and apply `IsAuthenticated` permissions where appropriate.
- Add tests for viewsets and serializers.
- Harden settings for production (move `SECRET_KEY` to environment variables, set `DEBUG=False`, configure allowed hosts, static/media storage).

## Postman collection

There is a Postman collection file `post_man-Collections.json` included at the project root to help testing the API endpoints.

How to use
- Import `post_man-Collections.json` into Postman (File → Import → choose the file).
- Set the collection variables or an environment with:
	- `base_url` (default `http://127.0.0.1:8000`)
	- `username` / `password` (your user credentials)
	- `access_token` / `refresh_token` (will be filled after obtaining tokens)

Steps
1. Create a superuser if you haven't already:

```bash
source env/bin/activate
python manage.py createsuperuser
```

2. Obtain JWT tokens using the "Auth - Obtain Token" request in Postman (POST `/api/token/`).
	 Copy `access` into `access_token` and `refresh` into `refresh_token`.

3. Use the collection requests (Conversations / Messages) — they include an `Authorization: Bearer {{access_token}}` header.

Quick curl examples
- Obtain token:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
	-H "Content-Type: application/json" \
	-d '{"username":"admin","password":"yourpassword"}'
```

- Create a conversation (authenticated):

```bash
curl -X POST http://127.0.0.1:8000/api/conversations/ \
	-H "Content-Type: application/json" \
	-H "Authorization: Bearer <ACCESS_TOKEN>" \
	-d '{}'
```

Notes
- The Postman collection is a convenience for manual testing. I can add Postman test scripts to automatically extract tokens into variables if you want.


## License & contact

This repository template has no license specified. Add a `LICENSE` file if you want to open-source this project.

If you want, I can also:
- add a `requirements.txt` from the current virtualenv,
- remove committed `env/` and `db.sqlite3` from git history,
- add basic API auth and permissions,
- or create a small test suite and run it.

---


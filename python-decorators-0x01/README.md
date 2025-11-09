# Python decorators exercises (0x01)

This directory contains a set of small exercises that demonstrate using Python decorators to manage common database-related concerns when working with sqlite3:

- `0-log_queries.py` — Implement a decorator to log SQL queries before execution.
- `1-with_db_connection.py` — Implement a decorator that opens and closes a sqlite3 connection and passes it to the wrapped function.
- `2-transactional.py` — Implement a decorator that wraps a DB operation in a transaction (commit on success, rollback on exception).
- `3-retry_on_failure.py` — Implement a decorator factory that retries a database operation a configurable number of times with delay.
- `4-cache_query.py` — Implement a decorator that caches query results (by query string) to avoid redundant database calls.
- `setup_database.py` — Helper script that creates a `users` table and inserts sample users (only inserts if table is empty).

How to run

1. Ensure you have Python 3 installed.
2. From the repository root, create the sample database:

```bash
python3 python-decorators-0x01/setup_database.py
```

3. Run any exercise file. Example:

```bash
python3 python-decorators-0x01/0-log_queries.py
python3 python-decorators-0x01/1-with_db_connection.py
python3 python-decorators-0x01/2-transactional.py
python3 python-decorators-0x01/3-retry_on_failure.py
python3 python-decorators-0x01/4-cache_query.py
```

What to expect

- The decorators are small, self-contained, and intended for learning. Each script prints output demonstrating the decorator behavior (for example logging SQL queries, successful commits, or cache hits/misses).

Notes and suggestions

- The `setup_database.py` script is idempotent: it will not insert duplicates if the `users` table already contains rows.
- Consider adding tests (pytest) to verify decorator behavior automatically.
- For production code, prefer connection context managers and stronger error handling.

License

This repository is provided for learning and practice purposes.
(The file `/home/gikonyo/ALX_PRODEV_BACKEND/alx-backend-python/python-decorators-0x01/README.md` exists, but is empty)
# Python decorators exercises (0x01)

This directory contains a set of small exercises that demonstrate using Python decorators to manage common database-related concerns when working with sqlite3:

- `0-log_queries.py` — Implement a decorator to log SQL queries before execution.
- `1-with_db_connection.py` — Implement a decorator that opens and closes a sqlite3 connection and passes it to the wrapped function.
- `2-transactional.py` — Implement a decorator that wraps a DB operation in a transaction (commit on success, rollback on exception).
- `3-retry_on_failure.py` — Implement a decorator factory that retries a database operation a configurable number of times with delay.
- `4-cache_query.py` — Implement a decorator that caches query results (by query string) to avoid redundant database calls.
- `setup_database.py` — Helper script that creates a `users` table and inserts sample users (only inserts if table is empty).

How to run

1. Ensure you have Python 3 installed.
2. From the repository root, create the sample database:

```bash
python3 python-decorators-0x01/setup_database.py
```

3. Run any exercise file. Example:

```bash
python3 python-decorators-0x01/0-log_queries.py
python3 python-decorators-0x01/1-with_db_connection.py
python3 python-decorators-0x01/2-transactional.py
python3 python-decorators-0x01/3-retry_on_failure.py
python3 python-decorators-0x01/4-cache_query.py
```

What to expect

- The decorators are small, self-contained, and intended for learning. Each script prints output demonstrating the decorator behavior (for example logging SQL queries, successful commits, or cache hits/misses).

Notes and suggestions

- The `setup_database.py` script is idempotent: it will not insert duplicates if the `users` table already contains rows.
- Consider adding tests (pytest) to verify decorator behavior automatically.
- For production code, prefer connection context managers and stronger error handling.

License

This repository is provided for learning and practice purposes.


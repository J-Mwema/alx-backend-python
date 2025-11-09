
# alx-backend-python

Collection of small Python exercises and utilities used while learning backend development concepts for the ALX program. This repository focuses on sqlite3 database handling, decorators, and small helper scripts used in course tasks.

## Structure

- `python-decorators-0x01/` — Exercises that implement decorators for database operations (logging, connection management, transactions, retrying, and caching). Each task is a standalone script (0-4) and includes a `setup_database.py` helper to create a test `users.db`.

## Quick start !


1. Create the sample database (creates `users.db` in the working directory):

```bash
python3 python-decorators-0x01/setup_database.py
```

2. Run any task script. Example:

```bash
python3 python-decorators-0x01/0-log_queries.py
python3 python-decorators-0x01/1-with_db_connection.py
python3 python-decorators-0x01/2-transactional.py
```

Note: the directory `python-decorators-0x01` contains a README with details on each exercise.

## Notes
- These scripts are intentionally small and self-contained for learning purposes.
- If you re-run `setup_database.py`, it will not insert duplicate sample rows (it only inserts when the `users` table is empty).

## Contributions
Feel free to open issues or submit PRs with improvements, tests, or additional exercises.

---

Created/maintained for the ALX backend Python learning path.

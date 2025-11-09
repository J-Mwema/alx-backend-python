# Context managers & async operations (0x02)

This folder contains exercises demonstrating class-based context managers for
database connections and asynchronous database queries using `aiosqlite`.

Files
- `0-databaseconnection.py` — `DatabaseConnection` class-based context manager that opens/closes a sqlite3 connection.
- `1-execute.py` — `ExecuteQuery` context manager that executes a provided query and returns results.
- `3-concurrent.py` — Asynchronous concurrent queries using `aiosqlite` and `asyncio.gather`.

Requirements
- Python 3.8+
- `aiosqlite` (only required for `3-concurrent.py`):

```bash
python3 -m pip install --user aiosqlite
```

How to run

1. Ensure the sample database `users.db` exists in the repository root. You can create it with the provided setup script:

```bash
python3 python-decorators-0x01/setup_database.py
```

2. Run the scripts:

```bash
python3 python-context-async-perations-0x02/0-databaseconnection.py
python3 python-context-async-perations-0x02/1-execute.py
# For async concurrent queries (requires aiosqlite):
python3 python-context-async-perations-0x02/3-concurrent.py
```

Notes
- `3-concurrent.py` requires `aiosqlite`; if it's not installed you'll get ModuleNotFoundError. Install with pip as shown above.

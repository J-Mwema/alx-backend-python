# Python decorators and database operations

[Back to the repository overview](../README.md)

This task demonstrates Python decorators for common SQLite database concerns:
logging queries, managing connections, controlling transactions, retrying
failures, and caching query results.

## Exercises

- [`0-log_queries.py`](./0-log_queries.py) — log SQL queries before execution.
- [`1-with_db_connection.py`](./1-with_db_connection.py) — open and close a
  database connection around a function call.
- [`2-transactional.py`](./2-transactional.py) — commit successful operations
  and roll back failed ones.
- [`3-retry_on_failure.py`](./3-retry_on_failure.py) — retry a database
  operation after failures.
- [`4-cache_query.py`](./4-cache_query.py) — cache query results.
- [`setup_database.py`](./setup_database.py) — create the sample users
  database.

## Run

From the repository root, create the sample database and run an exercise:

```bash
python3 python-decorators-0x01/setup_database.py
python3 python-decorators-0x01/0-log_queries.py
```

Each exercise is a standalone learning example; use the corresponding script
path to run another one.

## Other tasks

- [Generators](../python-generators-0x00/README.md)
- [Context managers and async operations](../python-context-async-perations-0x02/README.md)
- [All repository tasks](../README.md#project-map)

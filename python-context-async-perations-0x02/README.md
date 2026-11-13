# Context managers and asynchronous operations

[Back to the repository overview](../README.md)

This task explores reusable database context managers and asynchronous
database access. The examples open and close SQLite connections reliably,
execute a query inside a context, and run independent queries concurrently
with `asyncio`.

## Exercises

- [`0-databaseconnection.py`](./0-databaseconnection.py) — a class-based
  context manager for a SQLite connection.
- [`1-execute.py`](./1-execute.py) — a context manager that executes a query
  and exposes its results.
- [`3-concurrent.py`](./3-concurrent.py) — concurrent asynchronous queries
  using `aiosqlite`.

## Requirements and running

Use Python 3.8 or newer. The concurrent example additionally requires
`aiosqlite`:

```bash
python3 -m pip install aiosqlite
```

The examples use the sample `users.db` database. Create it from the repository
root if needed, then run an exercise:

```bash
python3 python-decorators-0x01/setup_database.py
python3 python-context-async-perations-0x02/0-databaseconnection.py
```

Run `1-execute.py` or `3-concurrent.py` by substituting its path above.

## Other tasks

- [Generators](../python-generators-0x00/README.md)
- [Decorators](../python-decorators-0x01/README.md)
- [All repository tasks](../README.md#project-map)

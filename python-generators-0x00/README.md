# Python generators and data streaming

[Back to the repository overview](../README.md)

This task practices generator-based data access: consume user records
incrementally, process them in batches, paginate lazily, and work with ages
without loading an entire result set into memory.

## Exercises

- [`0-stream_users.py`](./0-stream_users.py) — stream user records from the
  database.
- [`1-batch_processing.py`](./1-batch_processing.py) — process records in
  batches.
- [`2-lazy_paginate.py`](./2-lazy_paginate.py) — fetch paginated results
  lazily.
- [`4-stream_ages.py`](./4-stream_ages.py) — stream ages for aggregate
  processing.
- [`seed.py`](./seed.py) — prepare sample data for the exercises.

Run each exercise from the repository root with Python 3, following any
database setup required by the script.

## Other tasks

- [Decorators](../python-decorators-0x01/README.md)
- [Context managers and async operations](../python-context-async-perations-0x02/README.md)
- [All repository tasks](../README.md#project-map)

# Unit and integration testing

[Back to the repository overview](../README.md)

This task builds confidence in Python code by testing utility functions and a
GitHub organization client. It covers nested mapping access, JSON retrieval,
memoization, client properties, and integration behavior with test fixtures.

## Files

- [`utils.py`](./utils.py) — utility functions under test.
- [`client.py`](./client.py) — the GitHub organization client.
- [`test_utils.py`](./test_utils.py) — unit tests for the utilities.
- [`test_client.py`](./test_client.py) — unit and integration test cases for
  the client.
- [`fixtures.py`](./fixtures.py) — fixture data used by the tests.

Run the tests from this directory with the Python standard-library test
runner:

```bash
python3 -m unittest
```

## Other tasks

- [Django middleware project](../Django-Middleware-0x03/README.md)
- [Messaging app project](../messaging_app/README.md)
- [All repository tasks](../README.md#project-map)

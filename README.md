# ALX Backend Python

This repository is a collection of backend Python learning projects and ALX
exercises. It covers generators, decorators, database access, asynchronous
programming, automated testing, and Django REST APIs. The folders are separate
tasks and projects rather than one installable application.

## Project map

| Area | What it covers | Guide |
|---|---|---|
| [Python generators](./python-generators-0x00/README.md) | Stream and process user records lazily in batches and pages | [Task files](./python-generators-0x00/) |
| [Python decorators](./python-decorators-0x01/README.md) | Apply logging, connection management, transactions, retries, and caching to SQLite operations | [Task files](./python-decorators-0x01/) |
| [Context managers and async](./python-context-async-perations-0x02/README.md) | Manage database connections with context managers and run asynchronous queries concurrently | [Task files](./python-context-async-perations-0x02/) |
| [Unit and integration tests](./0x03-Unittests_and_integration_tests/README.md) | Test utility functions and a GitHub organization client with mocks and fixtures | [Task files](./0x03-Unittests_and_integration_tests/) |
| [Django middleware project](./Django-Middleware-0x03/README.md) | Build a Django REST chat API with middleware and supporting API features | [Project files](./Django-Middleware-0x03/) |
| [Messaging app](./messaging_app/README.md) | Develop, test, containerize, and deploy a Django REST messaging API | [Project files](./messaging_app/) |

## Accomplished work

- Implemented iterator and generator exercises for streaming, batching,
  pagination, and age-based filtering.
- Practiced SQLite decorator patterns, database context managers, and
  concurrent asynchronous queries.
- Added unit and integration test exercises around utility functions and a
  GitHub API client.
- Built Django chat/messaging APIs with users, conversations, and messages;
  the projects include supporting tests, API collections, and deployment
  assets.
- Added Docker, CI/CD, and Kubernetes-related configuration to the
  [messaging app project](./messaging_app/README.md).

## Getting started

Start with the README in the task or project you want to explore. Most
exercises can be run independently; Django projects have their own dependency
and setup instructions. Generated databases and local environment files are
development artifacts and should not be treated as shared project data.

## Navigation

- [Generators](./python-generators-0x00/README.md)
- [Decorators](./python-decorators-0x01/README.md)
- [Context managers and async](./python-context-async-perations-0x02/README.md)
- [Unit and integration tests](./0x03-Unittests_and_integration_tests/README.md)
- [Django middleware](./Django-Middleware-0x03/README.md)
- [Messaging app and deployment](./messaging_app/README.md)

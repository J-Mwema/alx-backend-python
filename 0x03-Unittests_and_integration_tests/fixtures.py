#!/usr/bin/env python3
"""Fixtures for integration tests"""
from typing import List, Dict

TEST_PAYLOAD = [
    (
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        [
            {
                "id": 7697149,
                "name": "episodes.dart",
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 1342004,
                },
                "fork": False,
                "forks": 0,
                "forks_count": 0,
                "created_at": "2013-01-19T00:31:37Z",
                "updated_at": "2019-09-23T11:53:58Z",
                "pushed_at": "2019-09-23T11:53:58Z",
                "homepage": "https://developers.google.com/open-source/gsoc/2012/showcase",
                "language": "Dart",
                "forks_count": 0,
                "stargazers_count": 0,
                "default_branch": "master",
                "open_issues_count": 0,
                "topics": ["dart", "episodes", "google"],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "visibility": "public",
                "license": {
                    "key": "bsd-3-clause",
                    "name": "BSD 3-Clause \"New\" or \"Revised\" License",
                    "spdx_id": "BSD-3-Clause",
                    "url": "https://api.github.com/licenses/bsd-3-clause",
                    "node_id": "MDc6TGljZW5zZTU="
                }
            },
            {
                "id": 8566971,
                "name": "dagger",
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 1342004,
                },
                "fork": False,
                "forks": 0,
                "forks_count": 0,
                "created_at": "2013-03-04T17:23:32Z",
                "updated_at": "2020-01-29T14:10:04Z",
                "pushed_at": "2019-05-03T20:54:36Z",
                "homepage": "https://dagger.dev",
                "language": "Java",
                "forks_count": 0,
                "stargazers_count": 0,
                "default_branch": "master",
                "open_issues_count": 0,
                "topics": ["dagger", "dependency-injection", "java"],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "visibility": "public",
                "license": {
                    "key": "apache-2.0",
                    "name": "Apache License 2.0",
                    "spdx_id": "Apache-2.0",
                    "url": "https://api.github.com/licenses/apache-2.0",
                    "node_id": "MDc6TGljZW5zZW1pdGVy"
                }
            }
        ],
        ['episodes.dart', 'dagger'],
        ['dagger']
    )
]

import pathlib

import pytest

pytest_plugins = [
    'spinta.testing.pytest',
]


@pytest.fixture(scope='session')
def spinta_test_config():
    return {
        'backends': {
            'default': {
                'backend': 'spinta.backends.postgresql:PostgreSQL',
                'dsn': 'postgresql://admin:admin123@localhost:54321/spinta_tests',
            },
        },
        'manifests': {
            'default': {
                'path': pathlib.Path() / 'manifest',
            },
        },
    }

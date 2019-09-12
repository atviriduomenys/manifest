import pathlib
import pprint

import pytest
import snoop
import pprintpp

# See: https://github.com/alexmojaki/snoop
snoop.install(
    # Force colors, since pytest captures all output by default.
    color=True,
)

# pprintpp produces much more readable output.
pprint.pformat = pprintpp.pformat

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

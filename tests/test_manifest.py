import datetime
from pathlib import Path

from admanifest.manifest import Loader


def test_vprops_fill_main_prop():
    obj = {
        'since': None,
        'until': None,
        'stars': 3,
    }

    properties = {
        'test:tag': {
            'stars': 4,
        },
    }

    manifest = Loader(Path())
    assert manifest._load_properties(properties, obj) == {
        'test': {
            'since': None,
            'source': None,
            'stars': 4,
            'type': None,
            'until': None,
            'vprops': {
                'tag': {
                    'since': None,
                    'source': None,
                    'stars': 4,
                    'type': None,
                    'until': None,
                },
            },
        },
    }

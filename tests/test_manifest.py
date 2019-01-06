from pathlib import Path

from admanifest.manifest import Loader


def test_vprops_fill_main_prop():
    obj = {
        'version': 1,
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
            'source': None,
            'stars': 4,
            'type': None,
            'version': 1,
            'vprops': {
                'tag': {
                    'source': None,
                    'stars': 4,
                    'type': None,
                    'version': 1,
                },
            },
        },
    }

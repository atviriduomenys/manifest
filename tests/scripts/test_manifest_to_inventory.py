import pathlib

from spinta.testing.utils import create_manifest_files

from lodam.testing import inventory
from lodam.services.inventory import manifest_to_inventory


def test_pkey(tmpdir):
    create_manifest_files(tmpdir, {
        'datasets/rc/geo.yml': {
            'type': 'dataset',
            'name': 'rc/geo',
            'resources': {
                'sql': {
                    'type': 'sql',
                    'objects': {
                        '': {
                            'country': {
                                'source': 'COUNTRIES',
                                'properties': {
                                    '_id': {
                                        'type': 'pk',
                                        'source': 'ID',
                                    },
                                    'name': {
                                        'type': 'string',
                                        'source': 'NAME',
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    })

    table = manifest_to_inventory(pathlib.Path(tmpdir))

    assert inventory(table) == '''\
    d | r | b | m | property | source    | prepare | type    | ref | level | access | title | description
    rc/geo                   |           |         |         |     |       |        |       |
      | sql                  |           |         | sql     |     |       |        |       |
      |   |                  |           |         |         |     |       |        |       |
      |   |   | country      | COUNTRIES |         |         | id  |       |        |       |
      |   |   |   | id       | ID        |         | integer |     |       |        |       |
      |   |   |   | name     | NAME      |         | string  |     |       |        |       |
    '''


def test_multiple_pkeys(tmpdir):
    create_manifest_files(tmpdir, {
        'datasets/rc/geo.yml': {
            'type': 'dataset',
            'name': 'rc/geo',
            'resources': {
                'sql': {
                    'type': 'sql',
                    'objects': {
                        '': {
                            'country': {
                                'source': 'COUNTRIES',
                                'properties': {
                                    '_id': {
                                        'type': 'pk',
                                        'source': ['ID1', 'ID2'],
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    })

    table = manifest_to_inventory(pathlib.Path(tmpdir))

    assert inventory(table) == '''\
    d | r | b | m | property | source    | prepare | type    | ref      | level | access | title | description
    rc/geo                   |           |         |         |          |       |        |       |
      | sql                  |           |         | sql     |          |       |        |       |
      |   |                  |           |         |         |          |       |        |       |
      |   |   | country      | COUNTRIES |         |         | id1, id2 |       |        |       |
      |   |   |   | id1      | ID1       |         | integer |          |       |        |       |
      |   |   |   | id2      | ID2       |         | integer |          |       |        |       |
    '''


def test_multiple_model_sources(tmpdir):
    create_manifest_files(tmpdir, {
        'datasets/rc/geo.yml': {
            'type': 'dataset',
            'name': 'rc/geo',
            'resources': {
                'sql': {
                    'type': 'sql',
                    'objects': {
                        '': {
                            'country': {
                                'source': [
                                    'COUNTRIES_1',
                                    'COUNTRIES_2',
                                ],
                                'properties': {
                                    '_id': {
                                        'type': 'pk',
                                        'source': 'ID',
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    })

    table = manifest_to_inventory(pathlib.Path(tmpdir))

    assert inventory(table) == '''\
    d | r | b | m | property | source      | prepare | type    | ref | level | access | title | description
    rc/geo                   |             |         |         |     |       |        |       |
      | sql                  |             |         | sql     |     |       |        |       |
      |   |                  |             |         |         |     |       |        |       |
      |   |   | country      | COUNTRIES_1 |         |         | id  |       |        |       |
      |   |   | country      | COUNTRIES_2 |         |         | id  |       |        |       |
      |   |   |   | id       | ID          |         | integer |     |       |        |       |
    '''

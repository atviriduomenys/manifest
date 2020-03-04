import csv
import pathlib

from ruamel.yaml import YAML
from spinta.utils.path import is_ignored

yaml = YAML(typ='safe')


DEFAULTS = {
    'dataset': '',
    'resource': '',
    'base': '',
    'model': '',
    'property': '',
    'source': '',
    'prepare': '',
    'type': '',
    'ref': '',
    'level': '',
    'access': '',
    'title': '',
    'description': '',
}


def manifest_to_inventory(path: pathlib.Path):
    ignore = [
        '.travis.yml',
        '/prefixes.yml',
        '/schema/',
        '/env/',
    ]

    for file in path.glob('**/*.yml'):
        if is_ignored(ignore, path, file):
            continue

        data = next(yaml.load_all(file.read_text()))

        if data['type'] == 'dataset':
            yield from dataset_to_inventory(data)


def dataset_to_inventory(data):
    yield {
        **DEFAULTS,
        'dataset': data['name'],
    }
    for k, v in data.get('resources', {}).items():
        yield from resource_to_inventory(k, v)


def resource_to_inventory(name, data):
    yield {
        **DEFAULTS,
        'resource': name,
        'type': data.get('type'),
    }
    for origin, objects in data.get('objects', {}).items():
        for k, v in objects.items():
            yield {**DEFAULTS}
            yield from model_to_inventory(k, v)


def model_to_inventory(name, data):
    props = data.get('properties', {})
    if '_id' in props:
        source = props['_id'].get('source', [])
        if not isinstance(source, list):
            source = [source]
        ref = ', '.join(s.lower() for s in source)
    else:
        ref = ''

    sources = data.get('source', [])
    if not isinstance(sources, list):
        sources = [sources]
    for source in sources:
        yield {
            **DEFAULTS,
            'model': name,
            'source': source,
            'ref': ref,
        }
    for k, v in props.items():
        if k == '_id':
            source = v.get('source', [])
            if not isinstance(source, list):
                source = [source]
            for s in filter(None, source):
                k = s.lower()
                if k not in props:
                    yield from prop_to_inventory(k, {**v, 'type': 'integer', 'source': s})
        else:
            yield from prop_to_inventory(k, v)


def prop_to_inventory(name, data):
    yield {
        **DEFAULTS,
        'property': name,
        'type': data.get('type'),
        'source': data.get('source'),
    }


def writecsv(f, rows):
    writer = csv.DictWriter(f, [
        'dataset',
        'resource',
        'base',
        'model',
        'property',
        'source',
        'prepare',
        'type',
        'ref',
        'level',
        'access',
        'title',
        'description',
    ])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

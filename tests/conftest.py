import itertools
import pathlib
import textwrap

import pytest

from admanifest.manifest import Loader


class ManifestFactory:

    def __init__(self, tmpdir):
        self.tmpdir = tmpdir
        self.path = pathlib.Path(str(tmpdir))
        self.loader = Loader(self.path, pathlib.Path('schema'))
        self.loader.load_schema_files()
        self.fixtures = {
            'provider': {
                'counter': ('p%d' % x for x in itertools.count(1)),
                'depends': [],
                'default': {
                    'id': 'p1',
                    'type': 'provider',
                    'title': 'Provider {id}'.format,
                    'sector': 'public',
                },
            },
            'dataset': {
                'counter': ('d%d' % x for x in itertools.count(1)),
                'depends': ['provider'],
                'default': {
                    'id': 'd1',
                    'type': 'dataset',
                    'title': 'Dataset {id}'.format,
                    'since': '2018-01-01',
                    'provider': 'p1',
                },
            },
            'project': {
                'counter': ('r%d' % x for x in itertools.count(1)),
                'depends': [],
                'default': {
                    'id': 'r1',
                    'type': 'project',
                    'since': '2018-01-01',
                },
            },
            'object': {
                'counter': ('o%d' % x for x in itertools.count(1)),
                'depends': ['provider', 'dataset', 'project'],
                'default': {
                    'id': 'o1',
                    'since': None
                },
            },
            'field': {
                'counter': ('f%d' % x for x in itertools.count(1)),
                'depends': ['provider', 'dataset', 'project', 'object'],
                'default': {
                    'id': 'f1',
                    'since': None
                },
            },
        }

    def __call__(self, files=None):
        if files:
            for path, content in files.items():
                self.tmpdir.join(path).write_text(textwrap.dedent(content), 'utf-8', ensure=True)
            self.loader.load_yaml_files()
        self.loader.errors = [next(iter(e.splitlines()), '').replace(str(self.tmpdir) + '/', '') for e in self.loader.errors]
        return self.loader

    def add(self, type, **data):
        assert type in self.fixtures
        data[type] = {k: v for k, v in data.items() if k not in self.fixtures}
        data = {k: v for k, v in data.items() if k in self.fixtures}

        target = 'project' if 'project' in data else 'dataset'

        self.loader.fail = True
        for name in self.fixtures[type]['depends']:
            if name in ('dataset', 'project') and target != name:
                continue

            namep = name + 's'
            value = data.get(name)
            params = dict(self.fixtures[name]['default'])

            if value is None or value is True:
                pass
            elif isinstance(value, str):
                params['id'] = value
            else:
                params.update(value)
                if 'id' not in value:
                    params['id'] = next(self.fixtures[name]['counter'])

            for k, v in params.items():
                if callable(v):
                    params[k] = v(**params)

            if name == 'object':
                data[name] = self._add_object(data[target], params)
            elif name == 'field':
                data[name] = self._add_field(data['object'], params)
            else:
                if params['id'] not in self.loader.objects[name]:
                    self.loader.load(params, self.path / namep / (params['id'] + '.yml'))
                data[name] = self.loader.objects[name][params['id']]

        self.loader.fail = False
        return data[type]

    def _add_object(self, target, params):
        print(target)
        if 'objects' not in target:
            target['objects'] = {}

        if params['id'] not in target['objects']:
            target['objects'][params['id']] = self.loader._load_object(params, target)

        return target['objects'][params['id']]

    def _add_field(self, target, params):
        if 'properties' not in target:
            target['properties'] = {}

        if params['id'] not in target['params']:
            target['properties'][params['id']] = self.loader._load_property(params, target)

        return target['properties'][params['id']]


@pytest.fixture
def manifest(tmpdir):
    return ManifestFactory(tmpdir)

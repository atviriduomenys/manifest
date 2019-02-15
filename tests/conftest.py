import itertools
import pathlib
import textwrap

import pytest

from admanifest.manifest import Loader


class ManifestFactory:

    def __init__(self, tmpdir):
        self.tmpdir = tmpdir
        self.path = pathlib.Path(str(tmpdir))
        self.loader = Loader(self.path)
        self.loader.load_schema(pathlib.Path('schema'))
        self.fixtures = {
            'owner': {
                'counter': ('p%d' % x for x in itertools.count(1)),
                'depends': [],
                'default': {
                    'name': 'p1',
                    'type': 'owner',
                    'title': 'Owner {id}'.format,
                    'sector': 'public',
                },
            },
            'dataset': {
                'counter': ('d%d' % x for x in itertools.count(1)),
                'depends': ['owner'],
                'default': {
                    'name': 'd1',
                    'type': 'dataset',
                    'title': 'Dataset {id}'.format,
                    'owner': 'p1',
                    'version': 1,
                    'date': '2018-01-01',
                },
            },
            'project': {
                'counter': ('r%d' % x for x in itertools.count(1)),
                'depends': [],
                'default': {
                    'name': 'r1',
                    'type': 'project',
                    'version': 1,
                    'date': '2018-01-01',
                },
            },
            'object': {
                'counter': ('o%d' % x for x in itertools.count(1)),
                'depends': ['owner', 'dataset', 'project'],
                'default': {
                    'id': 'o1',
                },
            },
            'field': {
                'counter': ('f%d' % x for x in itertools.count(1)),
                'depends': ['owner', 'dataset', 'project', 'object'],
                'default': {
                    'id': 'f1',
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
        if 'objects' not in target:
            target['objects'] = {}

        if ':' in params['id']:
            name, tag = params['id'].split(':', 1)
        else:
            name, tag = params['id'], ''

        if name not in target['objects']:
            target['objects'][name] = {}

        if tag not in target['objects'][name]:
            target['objects'][name][tag] = self.loader._load_object(params, target)

        return target['objects'][name][tag]

    def _add_field(self, target, params):
        if 'properties' not in target:
            target['properties'] = {}

        if params['id'] not in target['params']:
            target['properties'][params['id']] = self.loader._load_property(params, target)

        return target['properties'][params['id']]


@pytest.fixture
def manifest(tmpdir):
    return ManifestFactory(tmpdir)

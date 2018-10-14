import datetime
import contextlib
from pathlib import Path
from urllib.parse import urlparse

from jsonschema import Draft4Validator, SchemaError, ValidationError, RefResolutionError, validate
from ruamel.yaml import YAML

yaml = YAML(typ='safe')


class Loader:

    def __init__(self, path: Path, schema_path: Path, fail: bool = False):
        self.path = path
        self.schema_path = schema_path or (path / 'schema')
        self.schemas = {}
        self.objects = {
            'vocabulary': {},
            'provider': {},
            'source': {},
            'project': {},
        }
        self.fail = fail
        self.errors = []
        self.loaders = {
            'vocabulary': self.load_vocabulary,
            'source': self.load_source,
            'provider': self.load_provider,
            'project': self.load_project,
        }
        self.stack = []

    def _load_schema_refs(self, value, definitions):
        if isinstance(value, dict):
            if '$ref' in value and value['$ref'].endswith('.yml'):
                with self.push(value['$ref']):
                    return self.load_schema(self.schema_path / value['$ref'], definitions)
            else:
                return {
                    k: self._load_schema_refs(v, definitions)
                    for k, v in value.items()
                }
        if isinstance(value, list):
            return [self._load_schema_refs(v, definitions) for v in value]

        return value

    def _parse_date(self, value):
        if isinstance(value, datetime.date):
            return value
        if value is not None:
            try:
                return datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError as e:
                self.error(str(e))

    def _parse_source(self, value):
        if value is None:
            return

        if isinstance(value, str):
            value = {'type': 'csv', 'dsn': value}

        if value['type'] == 'csv':
            return {
                'dsn': value['dsn'],
                'type': value['type'],
            }
        else:
            self.error("Unknown source type: %s.", value['type'])

    @contextlib.contextmanager
    def push(self, *items):
        n = len(items)
        self.stack.extend(items)
        try:
            yield
        finally:
            self.stack = self.stack[:-n]

    def call(self, name, func, *args, **kwargs):
        name = name if isinstance(name, tuple) else (name,)
        with self.push(*name):
            return func(*args, **kwargs)

    def error(self, message, *args):
        message = str(message)
        if self.stack:
            message = ': '.join([str(x) for x in self.stack] + [message])
        if args:
            self.errors.append(message % args)
        else:
            self.errors.append(message)
        if self.fail:
            raise Exception(self.errors[-1])

    def load_schema_files(self):
        for path in self.schema_path.glob('**/*'):
            if not path.is_file():
                continue
            if path.suffix != '.yml':
                self.error("Only .yml files are supported, found unsupported %s file.", path)
                continue
            with self.push(str(path.relative_to(self.schema_path))):
                self.load_schema(path)

    def load_schema(self, path: Path, definitions=None):
        data = yaml.load(path.read_text())

        if definitions is None:
            main = True
            definitions = {}
            data = self._load_schema_refs(data, definitions)
            if definitions:
                data['definitions'] = definitions
        else:
            main = False
            definitions.update(data.pop('definitions', {}))
            data = self._load_schema_refs(data, definitions)

        try:
            Draft4Validator.check_schema(data)
        except (SchemaError, RefResolutionError) as e:
            self.error(e)
        else:
            if main:
                self.schemas[path.stem] = data
            return data

    def load_yaml_files(self):
        for name in ['vocabulary', 'providers', 'sources', 'projects']:
            for path in self.path.glob('%s/**/*' % name):
                if not path.is_file():
                    continue
                if path.suffix != '.yml':
                    self.error("Only .yml files are supported, found unsupported %s file.", path)
                    continue
                with self.push(str(path.relative_to(self.path))):
                    data = yaml.load(path.read_text())
                    self.load(data, path)

    def load(self, data: dict, path: Path):
        try:
            self.validate(data)
        except (ValidationError, RefResolutionError) as e:
            self.error("Error while reading %s: %s" % (path.relative_to(self.path), e))
        else:
            self.objects[data['type']][data['id']] = self.loaders[data['type']](data)

    def load_source(self, data):
        source = {
            'id': data['id'],
            'title': data['title'],
            'description': data.get('description', ''),
            'type': data['type'],
            'provider': data['provider'],
            'since': self.call('since', self._parse_date, data['since']),
            'until': self.call('until', self._parse_date, data.get('until', datetime.date.today())),
            'stars': data.get('stars'),
            'source': self.call('source', self._parse_source, data.get('source')),
        }
        source['objects'] = self.call('objects', self._load_objects, data.get('objects', {}), source)
        return source

    def _load_objects(self, objects, source):
        return {
            name: self.call(name, self._load_object, data, source)
            for name, data in objects.items()
        }

    def _load_object(self, data, source):
        obj = {
            'since': self.call('since', self._parse_date, data.get('since', source['since'])),
            'until': self.call('until', self._parse_date, data.get('until', source['since'])),
            'stars': data.get('stars', source['stars']),
            'source': self.call('source', self._parse_source, data.get('source')),
        }
        obj['properties'] = self.call('properties', self._load_properties, data.get('properties', {}), obj)
        return obj

    def _load_properties(self, props, obj):
        return {
            name: self.call(name, self._load_property, data, obj)
            for name, data in props.items()
        }

    def _load_property(self, data, obj):
        prop = {
            'type': data['type'],
            'since': self.call('since', self._parse_date, data.get('since', obj['since'])),
            'until': self.call('until', self._parse_date, data.get('until', obj['since'])),
            'stars': data.get('stars', obj['stars']),
            'source': self.call('source', self._parse_source, data.get('source')),
        }
        if prop['stars'] is None:
            with self.push('stars'):
                self.error("stars parameter is required, you can specify it on dataset, object or field scope.")
        return prop

    def load_vocabulary(self, data):
        return data

    def load_provider(self, data):
        return data

    def load_project(self, data):
        return data

    def validate(self, data: dict):
        if not isinstance(data, dict):
            raise ValidationError("Incorrect type, expected dict got %s." % type(data))

        if 'type' not in data:
            self.error("Type is not given.")

        if data['type'] not in self.objects:
            raise ValidationError("Type %s is not one of: %s." % (data['type'], ', '.join(sorted(self.objects.keys()))))

        schema = self.schemas[data['type']]
        validate(data, schema)

        if data['type'] in ('project', 'source'):
            self.validate_vocabulary(data)

        if data['type'] == 'project':
            self.validate_project_refs(data)

        if data['type'] == 'provider':
            self.validate_media_path('providers', data['id'], data.get('logo'))

    def validate_vocabulary(self, data):
        for obj_name, obj in data.get('objects', {}).items():
            if obj_name not in self.objects['vocabulary']:
                with self.push('objects'):
                    self.error("Unknown object name %s. You can only use names defined in vocabulary.", obj_name)
                continue
            for field_name, field in obj.get('properties', {}).items():
                if field_name not in self.objects['vocabulary'][obj_name]['properties']:
                    with self.push('objects', obj_name, 'properties'):
                        self.error("Unknown field name %s in %s object. You can only use names defined in vocabulary.",
                                   field_name, obj_name)

    def validate_project_refs(self, data):
        for obj_name, obj in data.get('objects', {}).items():
            for field_name, field in obj.get('properties', {}).items():
                with self.push('objects', obj_name, 'properties', field_name, 'source'):
                    self.validate_source_ref(obj_name, field_name, field.get('source'))

    def validate_source_refs(self, data):
        with self.push('provider'):
            self.validate_provider_ref(data.get('provider'))
        with self.push('source'):
            self.validate_source_uri(data.get('source'))
        for obj_name, obj in data.get('objects', {}).items():
            with self.push('objects', obj_name, 'source'):
                self.validate_source_uri(obj.get('source'))
            for field_name, field in obj.get('properties', {}).items():
                with self.push('objects', obj_name, 'properties', field_name, 'source'):
                    self.validate_source_uri(field.get('source'))

    def validate_source_uri(self, obj_name, field_name, source):
        if source is None:
            return

        if isinstance(source, list):
            for s in source:
                self.validate_source_uri(s)
            return

        if '://' in source:
            uri = urlparse(source)
            schemes = ('http', 'https')
            if uri.scheme not in schemes:
                self.error("Unknown source uri scheme %s. Known schemes are %s.", uri.scheme, ', '.join(schemes))
            return

        if ':' in source:
            func, source = source.split(':', 1)
            funcs = ('xml', 'xpath', 'css', 'field')
            if func not in funcs:
                self.error("Unknown source function %s. Known functions are %s.", func, ', '.join(funcs))
            return

        self.validate_source_ref(obj_name, field_name, source)

    def validate_source_ref(self, obj_name, field_name, source):
        if source is None:
            return

        if source not in self.objects['source']:
            self.error("Unknown source %s id, referenced in %s.%s.", source, obj_name, field_name)

        if obj_name not in self.objects['source'][source].get('objects', {}):
            self.error("Unknown source %s object name, referenced in %s.%s.", source, obj_name, field_name)

        if field_name not in self.objects['source'][source]['objects'][obj_name].get('properties', {}):
            self.error("Unknown source %s field name, referenced in %s.%s.", source, obj_name, field_name)

    def validate_provider_ref(self, provider):
        if provider is None:
            return

        if provider not in self.objects['provider']:
            self.error("Unknown provider %s id.", provider)

    def validate_media_path(self, type, id, name):
        if name is None:
            return

        path = self.path / 'media' / type / id / name
        if not path.exists():
            self.error("Can't find media file %s.", path)


def load_manifest_data(base_path: Path = None, schema_path: Path = None, loader: Loader = None):
    loader = loader or Loader(base_path, schema_path)
    loader.load_schema_files()
    loader.load_yaml_files()
    return loader

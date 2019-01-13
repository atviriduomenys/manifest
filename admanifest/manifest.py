import datetime
import contextlib
from pathlib import Path
from urllib.parse import urlparse

from jsonschema import ValidationError, RefResolutionError, validate
from ruamel.yaml import YAML

from admanifest.schema import SchemaLoader

yaml = YAML(typ='safe')


class Loader:

    def __init__(self, path: Path, fail: bool = False):
        self.path = path
        self.objects = {
            'vocabulary': {},
            'provider': {},
            'dataset': {},
            'project': {},
        }
        self.fail = fail
        self.errors = []
        self.loaders = {
            'vocabulary': self.load_vocabulary,
            'dataset': self.load_dataset,
            'provider': self.load_provider,
            'project': self.load_project,
        }
        self.stack = []
        self.schema = None

    def load_schema(self, path: Path = None):
        self.schema = SchemaLoader(path or (self.path / 'schema'))

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

        if not isinstance(value, list):
            value = [value]

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

    def load_yaml_files(self):
        for name in ['vocabulary', 'providers', 'datasets', 'projects']:
            for path in self.path.glob('%s/**/*' % name):
                if not path.is_file():
                    continue
                if path.suffix != '.yml':
                    self.error("Only .yml files are supported, found unsupported %s file.", path)
                    continue
                with self.push(str(path.relative_to(self.path))):
                    data = yaml.load(path.read_text())
                    self.load(data, path)

        self.validate_vocabulary_refs()

    def load(self, data: dict, path: Path):
        try:
            self.validate(data)
        except (ValidationError, RefResolutionError) as e:
            self.error("Error while reading %s: %s" % (path.relative_to(self.path), e))
        else:
            self.objects[data['type']][data['id']] = self.loaders[data['type']](data)
            self.objects[data['type']][data['id']]['path'] = path

    def load_dataset(self, data):
        dataset = {
            'id': data['id'],
            'title': data['title'],
            'description': data.get('description', ''),
            'type': data['type'],
            'provider': data['provider'],
            'version': data.get('version', 1),
            'date': self.call('date', self._parse_date, data['date']),
            'stars': data.get('stars'),
            'source': self.call('source', self._parse_source, data.get('source')),
        }
        dataset['objects'] = self.call('objects', self._load_objects, data.get('objects') or {}, dataset)
        self._validate_dataset_post_load(dataset)
        return dataset

    def _load_objects(self, objects, dataset):
        result = {}

        for name, data in objects.items():
            if ':' in name:
                name, tag = name.split(':', 1)
            else:
                tag = ''

            if name not in result:
                result[name] = {}

            result[name][tag] = self.call(name, self._load_object, data, dataset)

        return result

    def _load_object(self, data, dataset):
        obj = {
            'stars': data.get('stars', dataset['stars']),
            'source': self.call('source', self._parse_source, data.get('source')),
            'version': data.get('version', dataset['version']),
        }
        obj['properties'] = self.call('properties', self._load_properties, data.get('properties') or {}, obj)
        return obj

    def _load_properties(self, props, obj):
        result = {}

        # Load all properties and collect virtual properties to be loaded later.
        vprops = {}
        for name, data in props.items():
            if ':' in name:
                vprops[name] = data
                continue
            result[name] = self.call(name, self._load_property, data or {}, obj)
            result[name]['vprops'] = {}

        # Load virtual properties.
        for name, data in vprops.items():
            name, tag = name.split(':', 1)

            # If virtual property is defined, but the main property is not, then define the main property using
            # defaults.
            if name not in result:
                result[name] = self.call(name, self._load_property, {}, obj)
                result[name]['vprops'] = {}

            if name in result:
                result[name]['vprops'][tag] = self.call(name, self._load_property, data or {}, obj)
            else:
                result[name] = {
                    'vprops': {
                        tag: self.call(name, self._load_property, data or {}, obj),
                    },
                }

        # Calculate missing main property values from its virtual properties.
        for name, prop in result.items():
            if prop['version'] is None:
                prop['version'] = max((x['version'] for x in prop['vprops'].values() if x and x['version']), default=obj['version'])
            if prop['stars'] is None:
                prop['stars'] = min((x['stars'] for x in prop['vprops'].values() if x and x['stars']), default=obj['stars'])

        return result

    def _load_property(self, data, obj):
        return {
            'type': data.get('type'),
            'stars': data.get('stars', None),
            'source': self.call('source', self._parse_source, data.get('source')),
            'version': data.get('version', obj['version']),
        }

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
            return

        if data['type'] not in self.objects:
            raise ValidationError("Type %s is not one of: %s." % (data['type'], ', '.join(sorted(self.objects.keys()))))

        if data['type'] not in self.schema.schemas:
            self.error("Unknown object type %r." % data['type'])
            return

        schema = self.schema.schemas[data['type']]
        validate(data, schema)

        if data['type'] in ('project', 'dataset'):
            self.validate_vocabulary(data)

        if data['type'] == 'project':
            self.validate_project_refs(data)

        if data['type'] == 'provider':
            self.validate_media_path('providers', data['id'], data.get('logo'))

    def validate_vocabulary_ref(self, oname, prop_name, ref_by, ref_in=None):
        ref_in = ref_in or {}

        if oname is None:
            return

        if oname not in self.objects['vocabulary']:
            self.error("Unknown object %r, referenced by vocabulary property %r, via %r option.",
                       oname, '/'.join(ref_by), ref_in.get('object', 'object'))
            return

        if prop_name is None:
            return

        if prop_name not in self.objects['vocabulary'][oname].get('properties', {}):
            self.error("Unknown object %r property %r, referenced by vocabulary property %r, via %r option.",
                       oname, prop_name, '/'.join(ref_by), ref_in.get('property', 'property'))
            return

    def validate_vocabulary_refs(self):
        for oname, obj in self.objects['vocabulary'].items():
            with self.push(str(obj['path'].relative_to(self.path))):
                for pname, prop in obj.get('properties', {}).items():
                    ref_by = (oname, pname)
                    if prop['type'] == 'ref':
                        self.validate_vocabulary_ref(prop.get('object'), None, ref_by)
                    if prop['type'] == 'backref':
                        secondary = prop.get('secondary')
                        if secondary and isinstance(secondary, str):
                            self.validate_vocabulary_ref(secondary, prop.get('property'), ref_by, {
                                'object': 'secondary',
                            })
                        elif secondary:
                            self.validate_vocabulary_ref(prop.get('object'), None, ref_by)
                        else:
                            self.validate_vocabulary_ref(prop.get('object'), prop.get('property'), ref_by)
                    if prop['type'] == 'generic':
                        for i, ref_obj_name in enumerate(prop.get('enum', [])):
                            self.validate_vocabulary_ref(ref_obj_name, None, ref_by, {
                                'object': 'enum[%d]' % i,
                            })

    def validate_vocabulary(self, data):
        for oname, obj in data.get('objects', {}).items():
            if obj and obj.get('local') is True:
                continue
            if ':' in oname:
                oname, _ = oname.split(':', 1)
            if oname not in self.objects['vocabulary']:
                with self.push('objects'):
                    self.error("Unknown object name %r. You can only use names defined in vocabulary.", oname)
                continue
            for pname, prop in obj.get('properties', {}).items():
                if prop and prop.get('local') is True:
                    continue
                if ':' in pname:
                    pname, _ = pname.split(':', 1)
                if pname not in self.objects['vocabulary'][oname]['properties']:
                    with self.push('objects', oname, 'properties'):
                        self.error("Unknown property name %r in %r object. You can only use names defined in vocabulary.",
                                   pname, oname)

    def validate_project_refs(self, data):
        for oname, obj in data.get('objects', {}).items():
            for pname, prop in obj.get('properties', {}).items():
                with self.push('objects', oname, 'properties', pname, 'source'):
                    self.validate_dataset_ref(oname, pname, (prop or {}).get('source'))

    def validate_source_refs(self, data):
        with self.push('provider'):
            self.validate_provider_ref(data.get('provider'))
        with self.push('source'):
            self.validate_source_uri(data.get('source'))
        for oname, obj in data.get('objects', {}).items():
            with self.push('objects', oname, 'source'):
                self.validate_source_uri(obj.get('source'))
            for pname, prop in obj.get('properties', {}).items():
                with self.push('objects', oname, 'properties', pname, 'source'):
                    self.validate_source_uri(prop.get('source'))

    def validate_source_uri(self, oname, pname, source):
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
            funcs = ('xml', 'xpath', 'css', 'prop')
            if func not in funcs:
                self.error("Unknown source function %s. Known functions are %s.", func, ', '.join(funcs))
            return

        self.validate_dataset_ref(oname, pname, source)

    def validate_dataset_ref(self, oname, pname, dataset):
        if dataset is None:
            return

        if dataset not in self.objects['dataset']:
            self.error("Unknown dataset %s id, referenced in %s.%s.", dataset, oname, pname)
            return

        if oname not in self.objects['dataset'][dataset].get('objects', {}):
            self.error("Unknown dataset %s object name, referenced in %s.%s.", dataset, oname, pname)
            return

        if pname not in self.objects['dataset'][dataset]['objects'][oname].get('properties', {}):
            self.error("Unknown dataset %s property name, referenced in %s.%s.", dataset, oname, pname)
            return

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

    def _validate_dataset_post_load(self, dataset):
        for oname, objects in dataset.get('objects', {}).items():
            for tag, obj in objects.items():
                for pname, prop in obj.get('properties', {}).items():
                    if prop['stars'] is None:
                        with self.push('objects', (oname + ':' + tag) if tag else oname, 'properties', pname):
                            self.error("'stars' parameter is required, you can specify it on dataset, object, "
                                       "property or virtual property.")


def load_manifest_data(base_path: Path = None, schema_path: Path = None, loader: Loader = None):
    loader = loader or Loader(base_path)
    loader.load_schema(schema_path)
    loader.load_yaml_files()
    return loader

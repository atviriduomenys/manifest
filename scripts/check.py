#!/usr/bin/env python

import sys
from pathlib import Path
from urllib.parse import urlparse

from jsonschema import Draft4Validator, SchemaError, ValidationError, RefResolutionError, validate
from ruamel.yaml import YAML

yaml = YAML(typ='safe')


class Validator:

    def __init__(self, here: Path):
        self.here = here
        self.schemas = {}
        self.objects = {
            'vocabulary': {},
            'provider': {},
            'source': {},
            'project': {},
        }

    def _load_schema_refs(self, value, definitions):
        if isinstance(value, dict):
            if '$ref' in value and value['$ref'].endswith('.yml'):
                return self.load_schema(self.here / 'schema' / value['$ref'], definitions)
            else:
                return {
                    k: self._load_schema_refs(v, definitions)
                    for k, v in value.items()
                }
        if isinstance(value, list):
            return [self._load_schema_refs(v, definitions) for v in value]

        return value

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
            raise ValidationError("Error while reading %s: %s" % (path.relative_to(self.here), e))
        if main:
            self.schemas[path.stem] = data
        return data

    def load(self, path: Path):
        data = yaml.load(path.read_text())
        try:
            self.validate(data)
        except (ValidationError, RefResolutionError) as e:
            raise ValidationError("Error while reading %s: %s" % (path.relative_to(self.here), e))

        self.objects[data['type']][data['id']] = data

    def validate(self, data: dict):
        if not isinstance(data, dict):
            raise ValidationError("Incorrect type, expected dict got %s." % type(data))

        if 'type' not in data:
            raise ValidationError("Type is not given.")

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
                raise ValidationError("Unknown object name %s. You can only use names defined in vocabulary." % obj_name)
            for field_name, field in obj.get('properties', {}).items():
                if field_name not in self.objects['vocabulary'][obj_name]['properties']:
                    raise ValidationError("Unknown field name %s in %s object. You can only use names defined in vocabulary." % (field_name, obj_name))

    def validate_project_refs(self, data):
        for obj_name, obj in data.get('objects', {}).items():
            for field_name, field in obj.get('properties', {}).items():
                self.validate_source_ref(obj_name, field_name, field.get('source'))

    def validate_source_refs(self, data):
        self.validate_provider_ref(data.get('provider'))
        self.validate_source_uri(data.get('source'))
        for obj_name, obj in data.get('objects', {}).items():
            self.validate_source_uri(obj.get('source'))
            for field_name, field in obj.get('properties', {}).items():
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
                raise ValidationError("Unknown source uri scheme %s. Known schemes are %s." % (uri.scheme, ', '.join(schemes)))
            return

        if ':' in source:
            func, source = source.split(':', 1)
            funcs = ('xml', 'xpath', 'css', 'field')
            if func not in funcs:
                raise ValidationError("Unknown source function %s. Known functions are %s." % (func, ', '.join(funcs)))
            return

        self.validate_source_ref(obj_name, field_name, source)

    def validate_source_ref(self, obj_name, field_name, source):
        if source is None:
            return

        if source not in self.objects['source']:
            raise ValidationError("Unknown source %s id, referenced in %s.%s." % (source, obj_name, field_name))

        if obj_name not in self.objects['source'][source].get('objects', {}):
            raise ValidationError("Unknown source %s object name, referenced in %s.%s." % (source, obj_name, field_name))

        if field_name not in self.objects['source'][source]['objects'][obj_name].get('properties', {}):
            raise ValidationError("Unknown source %s field name, referenced in %s.%s." % (source, obj_name, field_name))

    def validate_provider_ref(self, provider):
        if provider is None:
            return

        if provider not in self.objects['provider']:
            raise ValidationError("Unknown provider %s id." % provider)

    def validate_media_path(self, type, id, name):
        if name is None:
            return

        path = self.here / 'media' / type / id / name
        if not path.exists():
            raise ValidationError("Can't find media file %s." % path)


def main():
    ok = True
    here = Path()
    validator = Validator(here)

    for name in ['schema', 'vocabulary', 'providers', 'sources', 'projects']:
        for path in here.glob('%s/**/*.yml' % name):
            try:
                if name == 'schema':
                    validator.load_schema(path)
                else:
                    validator.load(path)
            except ValidationError as e:
                ok = False
                print(e)

    if ok:
        print("All seems to be OK.")
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())

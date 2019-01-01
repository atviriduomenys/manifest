from pathlib import Path

from jsonschema import Draft4Validator
from ruamel.yaml import YAML


yaml = YAML(typ='safe')


class SchemaLoader:

    def __init__(self, path: Path):
        self.path = path
        self.definitions = {}
        self.schemas = {}
        self._load_definitions()
        self._load_schemas()

    def _read_yaml_file(self, path: Path):
        try:
            content = path.read_text() % {
                'object_name_pattern': r'^[a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ/_]+$',
                'property_name_pattern': r'^[a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ/_:]+$',
            }
            return yaml.load(content)
        except:  # noqa
            print('Error while loading %s.' % path)
            raise

    def _find_references(self, value):
        if isinstance(value, dict):
            if '$ref' in value:
                yield value['$ref']
            else:
                for k, v in value.items():
                    yield from self._find_references(v)
        elif isinstance(value, list):
            for v in value:
                yield from self._find_references(v)

    def _load_definitions(self):
        base = self.path / 'definitions'
        for path in base.glob('**/*.yml'):
            name = str(path.relative_to(base).with_suffix(''))
            schema = self._read_yaml_file(path)
            references = list(self._find_references(schema))
            definitions = schema.pop('definitions', {})
            self.definitions[name] = {
                'path': path,
                'schema': schema,
                'definitions': definitions,
                'references': references,
            }

    def _collect_definitions(self, definitions, schema):
        for ref in schema['references']:
            if not ref.startswith('#/definitions/'):
                continue
            name = ref[len('#/definitions/'):]
            if name in definitions:
                continue
            if name in schema['definitions']:
                definitions[name] = schema['definitions']
                continue
            if name in self.definitions:
                self._collect_definitions(definitions, self.definitions[name])
                definitions[name] = self.definitions[name]
            else:
                raise Exception("Unknown $ref %r in %s." % (ref, schema['path']))

    def _load_schemas(self):
        for path in self.path.glob('*.yml'):
            name = str(path.relative_to(self.path).with_suffix(''))
            schema = self._read_yaml_file(path)
            references = list(self._find_references(schema))
            definitions = schema.pop('definitions', {})
            schema['definitions'] = {}
            self._collect_definitions(schema['definitions'], {
                'path': path,
                'schema': schema,
                'definitions': definitions,
                'references': references,
            })
            Draft4Validator.check_schema(schema)
            self.schemas[name] = schema

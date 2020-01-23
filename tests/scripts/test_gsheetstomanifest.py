import datetime
import pathlib
import textwrap
import re

from ruamel.yaml import YAML

from spinta.testing.context import create_test_context

from lodam.services.gsheets import update_manifest_files
from lodam.services.gsheets import get_csv_rows

yaml = YAML(typ='safe')


def _read_rows(rows):
    for line in rows.splitlines():
        if line.strip():
            yield [x.strip() for x in line.split('|')]


def test_create_new_file(postgresql, config, tmpdir):
    tmpdir = pathlib.Path(tmpdir)

    context = create_test_context(config)
    context.load({
        'manifests': {
            'default': {
                'backend': 'default',
                'path': str(tmpdir),
            },
        },
    })

    rows = _read_rows('''
    dataset                     | resource | origin | model                       | property | type   | ref | const | title  | description | table     | column   | comment
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | etapas   | string |     | award | Etapas | Aprašymas   |           |          |
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | org      | ref    | org |       |        |             | ATN1      | ORG      |
    ''')

    update_manifest_files(context, rows)

    assert sorted([str(p.relative_to(tmpdir)) for p in tmpdir.glob('**/*.yml')]) == [
        'datasets/gov/vpt/new/ataskaitos/atn1.yml',
    ]
    assert yaml.load((tmpdir / 'datasets/gov/vpt/new/ataskaitos/atn1.yml').read_text()) == {
        'type': 'dataset',
        'name': 'gov/vpt/new/ataskaitos/atn1',
        'resources': {
            '': {  # resource
                'objects': {
                    'ATN1': {  # origin
                        'valstybe/pirkimas/ataskaita': {  # model
                            'source': 'ATN1',
                            'properties': {
                                'etapas': {  # property
                                    'type': 'string',
                                    'title': 'Etapas',
                                    'description': 'Aprašymas',
                                    'const': 'award',
                                },
                                'org': {  # property
                                    'type': 'ref',
                                    'object': 'org',
                                    'source': 'ORG'
                                },
                            },
                        },
                    },
                },
            },
        },
    }


def test_update_existing_file(postgresql, config, tmpdir):
    tmpdir = pathlib.Path(tmpdir)

    (tmpdir / 'datasets/gov/vpt').mkdir(mode=0o755, parents=True)
    (tmpdir / 'datasets/gov/vpt/ataskaitos.yml').write_text('\n'.join([
        '# Some comment',
        'type: dataset',
        'name: gov/vpt/ataskaitos',
        'version:',
        '  number: 1',
        '  date: 2019-08-27',
        'resources:',
        '  "":',
        '    type: sql',
        '    objects:',
        '      ATN1:',
        '        valstybe/pirkimas:',
        '          source: ATN1',
        '          properties:',
        '            etapas:',
        '              type: string',
        '              const: awadr',
        '            org:',
        '              type: ref',
        '              object: ogr',
        '              # More comments',
        '              source: OGR  # at the end of line',
        '            legacy:',
        '              type: string',
    ]))

    context = create_test_context(config)
    context.load({
        'manifests': {
            'default': {
                'backend': 'default',
                'path': str(tmpdir),
            },
        },
    })

    rows = _read_rows('''
    dataset            | resource | origin | model             | property | type   | ref | const | title       | description | table  | column   | comment
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | etapas   | string |     | award | Etapas      | Aprašymas   |        |          |
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | org      | ref    | org |       |             |             | ATN1   | ORG      |
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | title    | string |     |       | Pavadinimas |             | ATN1   | TITLE    |
    ''')

    update_manifest_files(context, rows)

    assert sorted([str(p.relative_to(tmpdir)) for p in tmpdir.glob('**/*.yml')]) == [
        'datasets/gov/vpt/ataskaitos.yml',
    ]
    content = (tmpdir / 'datasets/gov/vpt/ataskaitos.yml').read_text()
    assert '# Some comment' in content
    assert '# at the end of line' in content
    assert yaml.load(content) == {
        'type': 'dataset',
        'name': 'gov/vpt/ataskaitos',
        'version': {
            'number': 1,
            'date': datetime.date(2019, 8, 27),
        },
        'resources': {
            '': {
                'type': 'sql',
                'objects': {
                    'ATN1': {
                        'valstybe/pirkimas': {
                            'source': 'ATN1',
                            'properties': {
                                'etapas': {
                                    'type': 'string',
                                    'title': 'Etapas',
                                    'description': 'Aprašymas',
                                    'const': 'award',
                                },
                                'org': {
                                    'type': 'ref',
                                    'object': 'org',
                                    'source': 'ORG',
                                },
                                'title': {
                                    'type': 'string',
                                    'title': 'Pavadinimas',
                                    'source': 'TITLE',
                                },
                            },
                        },
                    },
                },
            },
        },
    }


def test_csv_file(postgresql, config, tmpdir):
    tmpdir = pathlib.Path(tmpdir)

    context = create_test_context(config)
    context.load({
        'manifests': {
            'default': {
                'backend': 'default',
                'path': str(tmpdir),
            },
        },
    })

    (tmpdir / 'schema.csv').write_text(re.sub(r' *\| *', ',', textwrap.dedent('''\
    dataset                     | resource | origin | model                       | property | type   | ref | const | title  | description | table     | column   | comment
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | etapas   | string |     | award | Etapas | Aprašymas   |           |          |
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | org      | ref    | org |       |        |             | ATN1      | ORG      |
    ''')))
    rows = get_csv_rows(tmpdir / 'schema.csv')

    update_manifest_files(context, rows)

    assert sorted([str(p.relative_to(tmpdir)) for p in tmpdir.glob('**/*.yml')]) == [
        'datasets/gov/vpt/new/ataskaitos/atn1.yml',
    ]
    assert yaml.load((tmpdir / 'datasets/gov/vpt/new/ataskaitos/atn1.yml').read_text()) == {
        'type': 'dataset',
        'name': 'gov/vpt/new/ataskaitos/atn1',
        'resources': {
            '': {  # resource
                'objects': {
                    'ATN1': {  # origin
                        'valstybe/pirkimas/ataskaita': {  # model
                            'source': 'ATN1',
                            'properties': {
                                'etapas': {  # property
                                    'type': 'string',
                                    'title': 'Etapas',
                                    'description': 'Aprašymas',
                                    'const': 'award',
                                },
                                'org': {  # property
                                    'type': 'ref',
                                    'object': 'org',
                                    'source': 'ORG'
                                },
                            },
                        },
                    },
                },
            },
        },
    }

import datetime
import pathlib

from ruamel.yaml import YAML

from spinta.testing.context import create_test_context

from lodam.services.gsheets import update_manifest_files

yaml = YAML(typ='safe')


def _read_rows(rows):
    for line in rows.splitlines():
        if line.strip():
            yield [x.strip() for x in line.split('|')]


def test_create_new_file(config, tmpdir):
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
    Open Data Manifest          |          |        |                             |          |        |     |       | VPT (new) |          |
    dataset                     | resource | origin | model                       | property | type   | ref | const | object    | property | comment
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | etapas   | string |     | award |           |          |
    gov/vpt/new/ataskaitos/atn1 |          | ATN1   | valstybe/pirkimas/ataskaita | org      | ref    | org |       | ATN1      | ORG      |
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


def test_update_existing_file(config, tmpdir):
    tmpdir = pathlib.Path(tmpdir)

    (tmpdir / 'datasets/gov/vpt').mkdir(mode=0o755, parents=True)
    (tmpdir / 'datasets/gov/vpt/ataskaitos.yml').write_text('\n'.join([
        '# Some comment',
        'type: dataset',
        'name: gov/vpt/ataskaitos',
        'date: 1',
        'version: 2019-08-27',
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
        '              const: award',
        '            org:',
        '              type: ref',
        '              object: org',
        '              # More comments',
        '              source: ORG  # at the end of line',
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
    Open Data Manifest |          |        |                   |          |        |     |       | VPT    |          |
    dataset            | resource | origin | model             | property | type   | ref | const | object | property | comment
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | etapas   | string |     | award |        |          |
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | org      | ref    | org |       | ATN1   | ORG      |
    gov/vpt/ataskaitos |          | ATN1   | valstybe/pirkimas | title    | string |     |       | ATN1   | TITLE    |
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
        'date': 1,
        'version': datetime.date(2019, 8, 27),
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
                                    'const': 'award',
                                },
                                'org': {
                                    'type': 'ref',
                                    'object': 'org',
                                    'source': 'ORG',
                                },
                                'title': {
                                    'type': 'string',
                                    'source': 'TITLE',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

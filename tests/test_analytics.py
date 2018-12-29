from pathlib import Path
from statistics import mean

import pytest

from admanifest.manifest import load_manifest_data
from admanifest.analytics import get_timeline_by_stars


def test_progress(manifest):
    manifest.add('field', stars=3)
    result = manifest()
    assert result.errors == []
    assert get_timeline_by_stars(result) == []


def find_sources(manifest, obj_name, prop_name):
    for source in manifest.objects['source'].values():
        if obj_name in source['objects'] and prop_name in source['objects'][obj_name]['properties']:
            yield source, source['objects'][obj_name]['properties'][prop_name]


def test_flat_tables():
    here = Path().resolve()
    manifest = load_manifest_data(here)

    if manifest.errors:
        for error in manifest.errors:
            pytest.fail(error)

    table = []
    for project in manifest.objects['project'].values():
        users = [x['users'] for x in project.get('impact', [])]
        users = mean(users) if users else None
        for obj_name, obj in project['objects'].items():
            for prop_name, prop in obj['properties'].items():
                sources = list(find_sources(manifest, obj_name, prop_name))
                sources = sorted(sources, key=lambda x: x[1]['stars'])
                if sources:
                    source, source_prop = sources[-1]
                    source = {
                        'id': source['id'],
                        'stars': source_prop['stars'],
                        'provider': source['provider'],
                    }
                else:
                    source = {'id': None, 'stars': 0, 'provider': None}

                table.append({
                    'project': project['id'],
                    'object': obj_name,
                    'property': prop_name,
                    'source': source['id'],
                    'provider': source['provider'],
                    'stars': source['stars'],
                    'users': users,
                })

    assert len(table) > 0

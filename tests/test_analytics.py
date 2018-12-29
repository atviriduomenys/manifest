from pathlib import Path
from statistics import mean

import pytest
import pandas as pd

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

    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 1000)

    frame = pd.DataFrame(table)

    print()
    print(' Duomenių rinkinių sąrašas pagal prioritetą '.center(80, '-'))
    print(
        frame.dropna(subset=['source']).groupby(['source', 'project']).agg({
            'stars': 'mean',
            'users': 'first',
        }).groupby(level=0).agg({
            'stars': 'mean',
            'users': 'sum',
        }).sort_values(['stars', 'users'], ascending=[True, False])
    )

    print(' Projektai pagal brandos lygį '.center(80, '-'))
    print(frame.groupby('project').stars.mean().sort_index())

    print(' Visi duomenys '.center(80, '-'))
    print(frame[['project', 'object', 'property', 'provider', 'source', 'stars', 'users']])

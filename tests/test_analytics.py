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


def find_datasets(manifest, oname, pname):
    for dataset in manifest.objects['dataset'].values():
        if oname in dataset['objects']:
            for obj in dataset['objects'][oname].values():
                if pname in obj['properties']:
                    yield dataset, obj['properties'][pname]


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
                datasets = list(find_datasets(manifest, obj_name, prop_name))
                datasets = sorted(datasets, key=lambda x: x[1]['stars'])
                if datasets:
                    dataset, dataset_prop = datasets[-1]
                    dataset = {
                        'id': dataset['id'],
                        'stars': dataset_prop['stars'],
                        'provider': dataset['provider'],
                    }
                else:
                    dataset = {'id': None, 'stars': 0, 'provider': None}

                table.append({
                    'project': project['id'],
                    'object': obj_name,
                    'property': prop_name,
                    'dataset': dataset['id'],
                    'provider': dataset['provider'],
                    'stars': dataset['stars'],
                    'users': users,
                })

    assert len(table) > 0

    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 1000)

    frame = pd.DataFrame(table)

    print()
    print(' Duomenių rinkinių sąrašas pagal prioritetą '.center(80, '-'))
    _frame = frame.dropna(subset=['dataset']).groupby(['dataset', 'project']).agg({
        'stars': ['sum', 'count'],
        'users': 'first',
    }).groupby(level=0).agg({
        ('stars', 'sum'): 'sum',
        ('stars', 'count'): 'sum',
        ('users', 'first'): 'sum',
    })
    print(
        pd.DataFrame({
            'stars': _frame[('stars', 'sum')] / _frame[('stars', 'count')],
            'users': _frame[('users', 'first')],
        }).sort_values(['stars', 'users'], ascending=[True, False])
    )

    print(' Duomenų laukai be šaltinio '.center(80, '-'))
    print(
        frame[frame.provider.isnull()].groupby(['object', 'property', 'project']).agg({
            'users': 'first',
        }).sort_values('users', ascending=False)
    )

    print(' Projektai pagal brandos lygį '.center(80, '-'))
    print(frame.groupby('project').stars.mean().sort_index())

    print(' Visi duomenys '.center(80, '-'))
    print(frame[['project', 'object', 'property', 'provider', 'dataset', 'stars', 'users']])

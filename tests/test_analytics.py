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
    datasets_used_in_projects = set()
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
                    datasets_used_in_projects.add(dataset['id'])
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

    # Add datasets not used in any project.
    for dataset in manifest.objects['dataset'].values():
        if dataset['id'] in datasets_used_in_projects:
            continue
        for oname, tags in dataset.get('objects', {}).items():
            props = {}
            for tag, obj in tags.items():
                for pname, prop in obj.get('properties', {}).items():
                    if pname not in props:
                        props[pname] = {
                            'stars': []
                        }
                    props[pname]['stars'].append(prop['stars'])
            for pname, prop in props.items():
                table.append({
                    'project': None,
                    'object': oname,
                    'property': pname,
                    'dataset': dataset['id'],
                    'provider': dataset['provider'],
                    'stars': sum(prop['stars']) / len(prop['stars']),
                    'users': None,
                })

    assert len(table) > 0

    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 1000)

    datasets = pd.DataFrame(table)

    print()
    print(' Duomenių rinkinių sąrašas pagal prioritetą '.center(80, '-'))
    ds = datasets.copy()
    ds['project'] = ds['project'].fillna('')
    ds['users'] = ds['users'].fillna(0)
    ds = ds.dropna(subset=['dataset']).groupby(['dataset', 'project']).agg({
        'stars': ['sum', 'count'],
        'users': 'first',
        'project': 'first',
    }).groupby(level=0).agg({
        ('stars', 'sum'): 'sum',
        ('stars', 'count'): 'sum',
        ('users', 'first'): 'sum',
        ('project', 'first'): 'count',
    })
    ds = pd.DataFrame({
        'stars': ds[('stars', 'sum')] / ds[('stars', 'count')],
        'users': ds[('users', 'first')],
        'projects': ds[('project', 'first')],
    })
    ds['score'] = (
        (ds['stars'] / 5) * -1 + 1 +
        (ds['users'] / ds['users'].max())
    ) / .02
    print(ds.sort_values('score', ascending=False))

    print(' Duomenų laukai be šaltinio '.center(80, '-'))
    ds = (
        datasets[datasets.provider.isnull()].groupby(['object', 'property', 'project']).agg({
            'users': 'first',
        }).sort_values('users', ascending=False)
    )
    print('Visi projekto duomenų laukai turi šaltinį!' if ds.empty else ds)

    print(' Projektai pagal brandos lygį '.center(80, '-'))
    print(datasets.groupby('project').stars.mean().sort_index())

    print('-' * 80)

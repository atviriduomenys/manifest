from pathlib import Path

import pytest
import pandas as pd

from admanifest.manifest import load_manifest_data
from admanifest.analytics import get_timeline_by_stars
from admanifest.analytics import get_flat_projects_and_datasets


def test_progress(manifest):
    manifest.add('field', stars=3)
    result = manifest()
    assert result.errors == []
    assert get_timeline_by_stars(result) == []


def test_flat_tables():
    here = Path().resolve()
    manifest = load_manifest_data(here)

    for error in manifest.errors:
        pytest.fail(error)

    table = list(get_flat_projects_and_datasets(manifest))

    assert len(table) > 0

    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_colwidth', 100)

    df = pd.DataFrame(table)

    print()
    print(' Duomenų rinkinių sąrašas pagal prioritetą '.center(80, '-'))
    tdf = df.copy()
    tdf['project'] = tdf['project'].fillna('')
    tdf['users'] = tdf['users'].fillna(0)
    tdf = tdf.dropna(subset=['dataset']).groupby(['dataset', 'project']).agg({
        'stars': ['sum', 'count'],
        'users': 'first',
        'project': 'first',
    }).groupby(level=0).agg({
        ('stars', 'sum'): 'sum',
        ('stars', 'count'): 'sum',
        ('users', 'first'): 'sum',
        ('project', 'first'): 'count',
    })
    tdf = pd.DataFrame({
        'stars': tdf[('stars', 'sum')] / tdf[('stars', 'count')],
        'users': tdf[('users', 'first')],
        'projects': tdf[('project', 'first')],
    })
    tdf['score'] = (
        (tdf['stars'] / 5) * -1 + 1 +
        (tdf['users'] / tdf['users'].max())
    ) / .02
    print(tdf.sort_values('score', ascending=False))

    print(' Duomenų laukai be šaltinio '.center(80, '-'))
    tdf = (
        df[df.owner.isnull()].groupby(['object', 'property', 'project']).agg({
            'users': 'first',
        }).sort_values('users', ascending=False)
    )
    print('Visi projekto duomenų laukai turi šaltinį!' if tdf.empty else tdf)

    print(' Projektai pagal brandos lygį '.center(80, '-'))
    print(df.groupby('project').stars.mean().sort_values(ascending=False))

    print(' Duomenų rinkiniai pagal brandos lygį '.center(80, '-'))
    print(df.groupby('dataset').stars.mean().sort_values(ascending=False))

    print(' Duomenų tiekėjai pagal brandos lygį '.center(80, '-'))
    print(df.groupby('owner').stars.mean().sort_values(ascending=False))

    print('-' * 80)

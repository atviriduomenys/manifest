from pathlib import Path

import pytest

from admanifest.manifest import Manifest
from admanifest.analytics import get_timeline_by_stars


def test_progress(manifest):
    manifest.add('field', stars=3)
    result = manifest()
    assert result.errors == []
    assert get_timeline_by_stars(result) == []


def test_flat_tables():
    here = Path().resolve()
    manifest = Manifest(here)

    result = manifest.select('source', [
        'title',
        'objects.title',
        'objects.properties.title',
    ])

    for items in result:
        print(*items)

    assert False

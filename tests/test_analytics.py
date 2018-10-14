from admanifest.analytics import get_timeline_by_stars


def test_progress(manifest):
    manifest.add('field', stars=3)
    result = manifest()
    assert result.errors == []
    assert list(get_timeline_by_stars(result)) == [
        ('s1', 'o1', 3),
    ]

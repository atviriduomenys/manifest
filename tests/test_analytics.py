import datetime

from admanifest.analytics import get_timeline_by_stars


def test_progress(manifest):
    manifest.add('source', source='s1', since='2018-01-01', stars=1)
    manifest.add('field', source='s1', stars=3)
    manifest.add('source', source='s2', since='2018-01-02', stars=3)
    result = manifest()
    assert result.errors == []
    assert list(get_timeline_by_stars(result)) == [
        ('s1', 'o1', 'f1', datetime.date(2018, 1, 1), 3),
        ('s2', None, None, datetime.date(2018, 1, 2), 3),
    ]

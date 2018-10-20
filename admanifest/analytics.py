from operator import itemgetter


def _get_timeline_by_starts(manifest):
    for source in manifest.objects['source'].values():
        if len(source['objects']) == 0:
            yield source['id'], None, None, source['since'], source['stars']
        for object in source['objects'].values():
            for field in object['properties'].values():
                yield source['id'], object['id'], field['id'], field['since'], field['stars']


def get_timeline_by_stars(manifest):
    return sorted(_get_timeline_by_starts(manifest), key=itemgetter(3))

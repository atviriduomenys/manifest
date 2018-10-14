def get_timeline_by_stars(manifest):
    for source in manifest.objects['source'].values():
        for object in source.get('objects', {}).values():
            for field in object.get('properties', {}).values():
                yield source['id'], object['id'], field['stars']

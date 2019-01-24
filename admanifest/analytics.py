from statistics import mean


def get_timeline_by_stars(manifest):
    return []


def find_datasets(manifest, oname, pname, owner):
    for dataset in manifest.objects['dataset'].values():
        if dataset['owner'] == owner:
            # Skip dataset if owner for dataset and project is the same.
            continue
        if oname in dataset['objects']:
            for obj in dataset['objects'][oname].values():
                if pname in obj['properties']:
                    yield dataset, obj['properties'][pname]


def get_flat_projects_and_datasets(manifest):
    table = []

    # Load all projects and datasets used by projects.
    datasets_used_in_projects = set()
    for project in manifest.objects['project'].values():
        users = [x['users'] for x in project.get('impact', [])]
        users = mean(users) if users else None
        for obj_name, obj in project['objects'].items():
            for prop_name, prop in obj['properties'].items():
                datasets = list(find_datasets(manifest, obj_name, prop_name, project['owner']))
                datasets = sorted(datasets, key=lambda x: x[1]['stars'])
                if datasets:
                    dataset, dataset_prop = datasets[-1]
                    dataset = {
                        'id': dataset['id'],
                        'stars': dataset_prop['stars'],
                        'owner': dataset['owner'],
                    }
                    datasets_used_in_projects.add((dataset['id'], obj_name, prop_name))
                else:
                    dataset = {'id': None, 'stars': 0, 'owner': None}

                yield {
                    'project': project['id'],
                    'object': obj_name,
                    'property': prop_name,
                    'dataset': dataset['id'],
                    'owner': dataset['owner'],
                    'stars': dataset['stars'],
                    'users': users,
                }

    # Add dataset properties not used in any project.
    for dataset in manifest.objects['dataset'].values():
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
                if (dataset['id'], oname, pname) not in datasets_used_in_projects:
                    yield {
                        'project': None,
                        'object': oname,
                        'property': pname,
                        'dataset': dataset['id'],
                        'owner': dataset['owner'],
                        'stars': sum(prop['stars']) / len(prop['stars']),
                        'users': None,
                    }

    return table

import datetime


def test_yml_files(manifest):
    result = manifest({
        'sources/gov/lrs.yaml': '''\
            type: source
        '''
    })
    assert result.errors == [
        "Only .yml files are supported, found unsupported sources/gov/lrs.yaml file.",
    ]


def test_id_is_required(manifest):
    result = manifest({
        'sources/gov/lrs.yml': '''\
            type: source
        '''
    })
    assert result.errors == [
        "sources/gov/lrs.yml: Error while reading sources/gov/lrs.yml: 'id' is a required property",
    ]


def test_since_date_validation(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'sources/gov/lrs.yml': '''\
            id: gov/lrs
            type: source
            title: LRS
            since: "01.01"
            stars: 3
            provider: gov/lrs
            objects:
                object:
                    since: "01.02"
                    properties:
                        prop:
                            type: string
                            since: "01.03"
        '''
    })
    assert result.errors == [
        "sources/gov/lrs.yml: since: time data '01.01' does not match format '%Y-%m-%d'",
        "sources/gov/lrs.yml: objects: object: since: time data '01.02' does not match format '%Y-%m-%d'",
        "sources/gov/lrs.yml: objects: object: properties: prop: since: time data '01.03' does not match format '%Y-%m-%d'",
    ]


def test_since_date_inheritance(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'sources/gov/lrs.yml': '''\
            id: gov/lrs
            type: source
            title: LRS
            since: "2018-01-01"
            stars: 3
            provider: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == []
    assert result.objects['source']['gov/lrs']['since'] == datetime.date(2018, 1, 1)
    assert result.objects['source']['gov/lrs']['objects']['object']['since'] == datetime.date(2018, 1, 1)
    assert result.objects['source']['gov/lrs']['objects']['object']['properties']['prop']['since'] == datetime.date(2018, 1, 1)


def test_stars_validation_error(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'sources/gov/lrs.yml': '''\
            id: gov/lrs
            type: source
            title: LRS
            since: "2018-01-01"
            provider: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == [
        "sources/gov/lrs.yml: objects: object: properties: prop: stars: stars parameter is required, you can specify it on dataset, object or field scope.",
    ]


def test_stars_inheritance(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'sources/gov/lrs.yml': '''\
            id: gov/lrs
            type: source
            title: LRS
            since: "2018-01-01"
            stars: 3
            provider: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == []
    assert result.objects['source']['gov/lrs']['stars'] == 3
    assert result.objects['source']['gov/lrs']['objects']['object']['stars'] == 3
    assert result.objects['source']['gov/lrs']['objects']['object']['properties']['prop']['stars'] == 3


def test_stars_inheritance_2(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'sources/gov/lrs.yml': '''\
            id: gov/lrs
            type: source
            title: LRS
            since: "2018-01-01"
            provider: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
                            stars: 3
        '''
    })
    assert result.errors == []
    assert result.objects['source']['gov/lrs']['stars'] is None
    assert result.objects['source']['gov/lrs']['objects']['object']['stars'] is None
    assert result.objects['source']['gov/lrs']['objects']['object']['properties']['prop']['stars'] == 3

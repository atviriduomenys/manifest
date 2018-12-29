import datetime
from pathlib import Path

from admanifest.manifest import load_manifest_data


def test_check_all_files():
    result = load_manifest_data(Path())
    assert result.errors == [], result.errors


def test_yml_files(manifest):
    result = manifest({
        'datasets/gov/lrs.yaml': '''\
            type: dataset
        '''
    })
    assert result.errors == [
        "Only .yml files are supported, found unsupported datasets/gov/lrs.yaml file.",
    ]


def test_id_is_required(manifest):
    result = manifest({
        'datasets/gov/lrs.yml': '''\
            type: dataset
        '''
    })
    assert result.errors == [
        "datasets/gov/lrs.yml: Error while reading datasets/gov/lrs.yml: 'id' is a required property",
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
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
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
        "datasets/gov/lrs.yml: since: time data '01.01' does not match format '%Y-%m-%d'",
        "datasets/gov/lrs.yml: objects: object: since: time data '01.02' does not match format '%Y-%m-%d'",
        "datasets/gov/lrs.yml: objects: object: properties: prop: since: time data '01.03' does not match format '%Y-%m-%d'",
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
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
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
    assert result.objects['dataset']['gov/lrs']['since'] == datetime.date(2018, 1, 1)
    assert result.objects['dataset']['gov/lrs']['objects']['object']['since'] == datetime.date(2018, 1, 1)
    assert result.objects['dataset']['gov/lrs']['objects']['object']['properties']['prop']['since'] == datetime.date(2018, 1, 1)


def test_stars_validation_error(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
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
        "datasets/gov/lrs.yml: objects: object: properties: prop: stars: stars parameter is required, you can specify it on dataset, object or field scope.",
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
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
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
    assert result.objects['dataset']['gov/lrs']['stars'] == 3
    assert result.objects['dataset']['gov/lrs']['objects']['object']['stars'] == 3
    assert result.objects['dataset']['gov/lrs']['objects']['object']['properties']['prop']['stars'] == 3


def test_stars_inheritance_2(manifest):
    result = manifest({
        'vocabulary/object.yml': '''\
            id: "object"
            type: "vocabulary"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
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
    assert result.objects['dataset']['gov/lrs']['stars'] is None
    assert result.objects['dataset']['gov/lrs']['objects']['object']['stars'] is None
    assert result.objects['dataset']['gov/lrs']['objects']['object']['properties']['prop']['stars'] == 3

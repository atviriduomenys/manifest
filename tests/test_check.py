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


def test_date_validation(manifest):
    result = manifest({
        'models/object.yml': '''\
            id: "object"
            type: "model"
            version: 1
            date: "2019-01-06"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
            version: 1
            date: "01.01"
            stars: 3
            title: LRS
            owner: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == [
        "datasets/gov/lrs.yml: date: time data '01.01' does not match format '%Y-%m-%d'",
    ]


def test_stars_validation_error(manifest):
    result = manifest({
        'models/object.yml': '''\
            id: "object"
            type: "model"
            version: 1
            date: "2019-01-06"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
            version: 1
            date: "2018-01-01"
            title: LRS
            owner: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == [
        "datasets/gov/lrs.yml: objects: object: properties: prop: 'stars' parameter is required, you can specify it "
        "on dataset, object, property or virtual property.",
    ]


def test_stars_inheritance(manifest):
    result = manifest({
        'models/object.yml': '''\
            id: "object"
            type: "model"
            version: 1
            date: "2019-01-06"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
            title: LRS
            version: 1
            date: "2018-01-01"
            stars: 3
            owner: gov/lrs
            objects:
                object:
                    properties:
                        prop:
                            type: string
        '''
    })
    assert result.errors == []
    assert result.objects['dataset']['gov/lrs']['stars'] == 3
    assert result.objects['dataset']['gov/lrs']['objects']['object']['']['stars'] == 3
    assert result.objects['dataset']['gov/lrs']['objects']['object']['']['properties']['prop']['stars'] == 3


def test_stars_inheritance_2(manifest):
    result = manifest({
        'models/object.yml': '''\
            id: "object"
            type: "model"
            version: 1
            date: "2018-01-01"
            properties:
                prop:
                    type: "string"
        ''',
        'datasets/gov/lrs.yml': '''\
            id: gov/lrs
            type: dataset
            version: 1
            date: "2018-01-01"
            title: LRS
            owner: gov/lrs
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
    assert result.objects['dataset']['gov/lrs']['objects']['object']['']['stars'] is None
    assert result.objects['dataset']['gov/lrs']['objects']['object']['']['properties']['prop']['stars'] == 3

import io
import csv

import sqlalchemy as sa

from lodam.services.sqlschema import inspect, writecsv


def test_inspect():
    engine = sa.create_engine('sqlite://')
    engine.execute('CREATE TABLE t(foo INTEGER NOT NULL, bar INTEGER NOT NULL, PRIMARY KEY(foo, bar));')
    cols = inspect(engine)
    f = io.StringIO()
    writecsv(f, cols)
    f.seek(0)
    assert list(csv.DictReader(f)) == [
        {
            'dataset': '',
            'resource': '',
            'origin': '',
            'model': 't',
            'property': '_id',
            'type': 'pk',
            'ref': '',
            'const': '',
            'title': '',
            'description': '',
            'table': 't',
            'column': 'foo,bar',
            'ref.table': '',
            'ref.column': '',
        },
        {
            'dataset': '',
            'resource': '',
            'origin': '',
            'model': 't',
            'property': 'foo',
            'type': 'integer',
            'ref': '',
            'const': '',
            'title': '',
            'description': '',
            'table': 't',
            'column': 'foo',
            'ref.table': '',
            'ref.column': '',
        },
        {
            'dataset': '',
            'resource': '',
            'origin': '',
            'model': 't',
            'property': 'bar',
            'type': 'integer',
            'ref': '',
            'const': '',
            'title': '',
            'description': '',
            'table': 't',
            'column': 'bar',
            'ref.table': '',
            'ref.column': '',
        },
    ]

import io
import csv

import sqlalchemy as sa

from lodam.services.sqlschema import inspect, writecsv


def test_inspect():
    engine = sa.create_engine('sqlite://')
    engine.execute('CREATE TABLE t(id INTEGER PRIMARY KEY);')
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
            'property': 'id',
            'type': 'pk',
            'ref': '',
            'const': '',
            'title': '',
            'description': '',
            'table': 't',
            'column': 'id',
            'ref.table': '',
            'ref.column': '',
        },
    ]

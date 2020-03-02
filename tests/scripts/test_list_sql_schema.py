from typing import Iterable, Dict

import io
import csv

import sqlalchemy as sa

from lodam.services import sqlschema


def pretty(rows: Iterable[Dict]):
    cols = [
        'dataset',
        'resource',
        'base',
        'model',
        'property',
        'source',
        'type',
        'ref',
        'level',
        'access',
        'title',
        'description',
    ]

    hpos = cols.index('property')
    hsize = 1  # hierachical column size
    bsize = 3  # border size
    sizes = dict(
        [(c, 1) for c in cols[:hpos]] +
        [(c, len(c)) for c in cols[hpos:]]
    )
    rows = list(rows)
    for row in rows:
        for i, col in enumerate(cols):
            val = str(row[col])
            if i < hpos:
                size = (hsize + bsize) * (hpos - i) + sizes['property']
                if size < len(val):
                    sizes['property'] += len(val) - size
            elif sizes[col] < len(val):
                sizes[col] = len(val)

    line = []
    for col in cols:
        size = sizes[col]
        line.append(col[:size].ljust(size))

    depth = 0
    lines = [line]
    for row in rows:
        line = []

        for i, col in enumerate(cols[:hpos + 1]):
            val = row[col]
            if val:
                depth = i
                break
        else:
            val = ''
            if depth < hpos:
                depth += 1
            else:
                depth = 2

        line += [' ' * hsize] * depth
        size = (hsize + bsize) * (hpos - depth) + sizes['property']
        line += [val.ljust(size)]

        for col in cols[hpos + 1:]:
            val = str(row[col])
            size = sizes[col]
            line.append(val.ljust(size))

        lines.append(line)

    lines = [' | '.join(line) for line in lines]
    indent = '    '
    return '\n'.join([indent + l.rstrip() for l in lines]) + '\n' + indent


def inspect(sql, dataset='datasets/test/data', resource='sqlite'):
    engine = sa.create_engine('sqlite://')
    engine.connect().connection.cursor().executescript(sql)
    models = sqlschema.inspect(engine)
    f = io.StringIO()
    sqlschema.writecsv(f, models, dataset=dataset, resource=resource)
    f.seek(0)
    return list(csv.DictReader(f))


def test_no_pk():
    table = inspect('''\
    CREATE TABLE BAZ(
        foo INTEGER NOT NULL,
        bar TEXT NOT NULL
    );
    ''')
    assert pretty(table) == '''\
    d | r | b | m | property | source | type    | ref | level | access | title | description
    datasets/test/data       |        |         |     |       |        |       |
      | sqlite               |        |         |     |       |        |       |
      |   |                  |        |         |     |       |        |       |
      |   |   | baz          | BAZ    |         |     |       |        |       |
      |   |   |   | foo      | foo    | integer |     | 3     |        |       |
      |   |   |   | bar      | bar    | string  |     | 3     |        |       |
    '''


def test_pk():
    table = inspect('''\
    CREATE TABLE BAZ(
        ID INTEGER NOT NULL,
        PRIMARY KEY(ID)
    );
    ''')
    assert pretty(table) == '''\
    d | r | b | m | property | source | type    | ref | level | access | title | description
    datasets/test/data       |        |         |     |       |        |       |
      | sqlite               |        |         |     |       |        |       |
      |   |                  |        |         |     |       |        |       |
      |   |   | baz          | BAZ    |         | id  |       |        |       |
      |   |   |   | id       | ID     | integer |     | 4     |        |       |
    '''


def test_two_pkeys():
    table = inspect('''\
    CREATE TABLE BAZ(
        foo INTEGER NOT NULL,
        bar INTEGER NOT NULL,
        PRIMARY KEY(foo, bar)
    );
    ''')
    assert pretty(table) == '''\
    d | r | b | m | property | source | type    | ref      | level | access | title | description
    datasets/test/data       |        |         |          |       |        |       |
      | sqlite               |        |         |          |       |        |       |
      |   |                  |        |         |          |       |        |       |
      |   |   | baz          | BAZ    |         | foo, bar |       |        |       |
      |   |   |   | foo      | foo    | integer |          | 4     |        |       |
      |   |   |   | bar      | bar    | integer |          | 4     |        |       |
    '''


def test_fkeys():
    table = inspect('''\
    CREATE TABLE COUNTRY(
        ID INTEGER NOT NULL PRIMARY KEY,
        AREA INTEGER NULL,
        NAME TEXT NOT NULL
    );
    CREATE TABLE CITY(
        ID INTEGER NOT NULL PRIMARY KEY,
        COUNTRY_ID INTEGER,
        NAME TEXT NOT NULL,
        FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRY (ID)
    );
    ''')
    assert pretty(table) == '''\
    d | r | b | m | property   | source     | type    | ref         | level | access | title | description
    datasets/test/data         |            |         |             |       |        |       |
      | sqlite                 |            |         |             |       |        |       |
      |   |                    |            |         |             |       |        |       |
      |   |   | city           | CITY       |         | id          |       |        |       |
      |   |   |   | id         | ID         | integer |             | 4     |        |       |
      |   |   |   | country_id | COUNTRY_ID | ref     | country[id] | 4     |        |       |
      |   |   |   | name       | NAME       | string  |             | 3     |        |       |
      |   |                    |            |         |             |       |        |       |
      |   |   | country        | COUNTRY    |         | id          |       |        |       |
      |   |   |   | id         | ID         | integer |             | 4     |        |       |
      |   |   |   | area       | AREA       | integer |             | 3     |        |       |
      |   |   |   | name       | NAME       | string  |             | 3     |        |       |
    '''

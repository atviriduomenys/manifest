import io
import csv

import sqlalchemy as sa

from lodam.services import sqlschema
from lodam.testing import inventory


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
    assert inventory(table) == '''\
    d | r | b | m | property | source | prepare | type    | ref | level | access | title | description
    datasets/test/data       |        |         |         |     |       |        |       |
      | sqlite               |        |         |         |     |       |        |       |
      |   |                  |        |         |         |     |       |        |       |
      |   |   | baz          | BAZ    |         |         |     |       |        |       |
      |   |   |   | foo      | foo    |         | integer |     | 3     |        |       |
      |   |   |   | bar      | bar    |         | string  |     | 3     |        |       |
    '''


def test_pk():
    table = inspect('''\
    CREATE TABLE BAZ(
        ID INTEGER NOT NULL,
        PRIMARY KEY(ID)
    );
    ''')
    assert inventory(table) == '''\
    d | r | b | m | property | source | prepare | type    | ref | level | access | title | description
    datasets/test/data       |        |         |         |     |       |        |       |
      | sqlite               |        |         |         |     |       |        |       |
      |   |                  |        |         |         |     |       |        |       |
      |   |   | baz          | BAZ    |         |         | id  |       |        |       |
      |   |   |   | id       | ID     |         | integer |     | 4     |        |       |
    '''


def test_two_pkeys():
    table = inspect('''\
    CREATE TABLE BAZ(
        foo INTEGER NOT NULL,
        bar INTEGER NOT NULL,
        PRIMARY KEY(foo, bar)
    );
    ''')
    assert inventory(table) == '''\
    d | r | b | m | property | source | prepare | type    | ref      | level | access | title | description
    datasets/test/data       |        |         |         |          |       |        |       |
      | sqlite               |        |         |         |          |       |        |       |
      |   |                  |        |         |         |          |       |        |       |
      |   |   | baz          | BAZ    |         |         | foo, bar |       |        |       |
      |   |   |   | foo      | foo    |         | integer |          | 4     |        |       |
      |   |   |   | bar      | bar    |         | integer |          | 4     |        |       |
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
    assert inventory(table) == '''\
    d | r | b | m | property   | source     | prepare | type    | ref         | level | access | title | description
    datasets/test/data         |            |         |         |             |       |        |       |
      | sqlite                 |            |         |         |             |       |        |       |
      |   |                    |            |         |         |             |       |        |       |
      |   |   | city           | CITY       |         |         | id          |       |        |       |
      |   |   |   | id         | ID         |         | integer |             | 4     |        |       |
      |   |   |   | country_id | COUNTRY_ID |         | ref     | country[id] | 4     |        |       |
      |   |   |   | name       | NAME       |         | string  |             | 3     |        |       |
      |   |                    |            |         |         |             |       |        |       |
      |   |   | country        | COUNTRY    |         |         | id          |       |        |       |
      |   |   |   | id         | ID         |         | integer |             | 4     |        |       |
      |   |   |   | area       | AREA       |         | integer |             | 3     |        |       |
      |   |   |   | name       | NAME       |         | string  |             | 3     |        |       |
    '''

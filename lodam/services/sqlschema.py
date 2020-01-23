import csv

import sqlalchemy as sa

from sqlalchemy.engine import reflection
from sqlalchemy.dialects import mssql


TYPES = {
    sa.Integer: 'integer',
    sa.String: 'string',
    sa.Date: 'date',
    sa.DateTime: 'datetime',
    sa.Numeric: 'number',
    sa.LargeBinary: 'binary',

    # MSSQL types
    mssql.IMAGE: 'image',
    mssql.TIMESTAMP: 'datetime',
    mssql.BIT: 'boolean',
    mssql.MONEY: 'number',
    mssql.UNIQUEIDENTIFIER: 'string',  # 16-byte GUID
}


def inspect(engine, schema=None):
    insp = reflection.Inspector.from_engine(engine)
    for table in insp.get_table_names(schema):
        pkey = insp.get_pk_constraint(table, schema)
        if pkey:
            yield (
                table,
                pkey['constrained_columns'],
                'pk',
                '',
            )

        fkeys = insp.get_foreign_keys(table, schema)
        refs = {}
        for fkey in fkeys:
            for col, ref in zip(fkey['constrained_columns'], fkey['referred_columns']):
                assert col not in refs, (table, col, refs)
                refs[col] = {
                    'schema': fkey['referred_schema'],
                    'table': fkey['referred_table'],
                    'column': ref,
                }

        for column in insp.get_columns(table, schema):
            yield (
                table,
                column['name'],
                detect_type(column['type']),
                refs.get(column['name'], ''),
            )


def detect_type(ctype):
    for ct in ctype.__class__.__mro__:
        if ct in TYPES:
            return TYPES[ct]
    raise Exception("Can't detect column {column.name} type. Type MRO:\n - " + '\n - '.join(
        ct.__name__
        for ct in ctype.__class__.__mro__
    ))


def writecsv(f, cols, params=None):
    params = {
        'dataset': '',
        'resource': '',
        'origin': '',
        'model': '{table}',
        **(params or {}),
    }
    writer = csv.writer(f)
    writer.writerow([
        'dataset',
        'resource',
        'origin',
        'model',
        'property',
        'type',
        'ref',
        'const',
        'title',
        'description',
        'table',
        'column',
        'ref.table',
        'ref.column',
    ])
    for table, column, ctype, ref in cols:
        kwargs = {
            'table': table.lower(),
        }

        if ctype == 'pk':
            dtype = 'pk'
            prop = '_id'
            column = ','.join(column)
        else:
            prop = column.lower()

        if ref:
            dtype = 'ref'
        else:
            dtype = ctype

        writer.writerow([
            params['dataset'].format(**kwargs),
            params['resource'].format(**kwargs),
            params['origin'].format(**kwargs),
            params['model'].format(**kwargs),
            prop,
            dtype,
            params['model'].format(**{**kwargs, 'table': ref['table'].lower()}) if ref else '',
            '',  # const
            '',  # title
            '',  # description
            table,
            column,
            ref['table'] if ref else '',
            ref['column'] if ref else '',
        ])

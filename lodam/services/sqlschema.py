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
            pkeys = pkey['constrained_columns']
        else:
            pkeys = []
        model = {
            'model': table.lower(),
            'source': table,
            'ref': ', '.join([pk.lower() for pk in pkeys]),
        }
        props = inspect_table(insp, table, schema, pkeys)
        yield model, props


def inspect_table(insp, table, schema, pkeys):
    refs = {}
    fkeys = insp.get_foreign_keys(table, schema)
    for fkey in fkeys:
        for col, ref in zip(fkey['constrained_columns'], fkey['referred_columns']):
            assert col not in refs, (table, col, refs)
            refschema = fkey['referred_schema']
            reftable = fkey['referred_table'].lower()
            ref = ref.lower()
            if schema and refschema and refschema != schema:
                refs[col] = f'{refschema}.{reftable}[{ref}]'
            else:
                refs[col] = f'{reftable}[{ref}]'

    for column in insp.get_columns(table, schema):
        name = column['name']
        if name in refs:
            dtype = 'ref'
        else:
            dtype = detect_type(column['type'])
        if name in pkeys or name in refs:
            level = 4
        else:
            level = 3
        yield {
            'property': name.lower(),
            'source': name,
            'type': dtype,
            'ref': refs.get(name, ''),
            'level': level,
        }


def detect_type(ctype):
    for ct in ctype.__class__.__mro__:
        if ct in TYPES:
            return TYPES[ct]
    raise Exception("Can't detect column {column.name} type. Type MRO:\n - " + '\n - '.join(
        ct.__name__
        for ct in ctype.__class__.__mro__
    ))


def writecsv(f, models, dataset='', resource=''):
    writer = csv.DictWriter(f, [
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
    ])
    writer.writeheader()
    writer.writerow({'dataset': dataset})
    writer.writerow({'resource': resource})
    for model, props in models:
        writer.writerow({'base': ''})
        writer.writerow(model)
        for prop in props:
            writer.writerow(prop)

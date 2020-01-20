#!/usr/bin/env python

import csv
import sys

import click
import sqlalchemy as sa
from sqlalchemy.engine import reflection
from sqlalchemy.dialects import mssql


@click.command()
@click.argument('dsn')
@click.option('--schema', help="database schema name")
@click.option('-o', '--output', help="output file")
@click.option('--dataset', default='sql', help="dataset name tamplate")
@click.option('--resource', default='sql', help="resource name template")
@click.option('--origin', default='sql', help="origin name template")
@click.option('--model', default='{table}', help="model name template")
def main(dsn, schema, output, dataset, resource, origin, model):
    engine = sa.create_engine(dsn)
    cols = inspect(engine, schema)
    params = {
        'dataset': dataset,
        'resource': resource,
        'origin': origin,
        'model': model,
    }
    if output:
        with open(output, 'w') as f:
            write(f, cols, params)
    else:
        write(sys.stdout, cols, params)


def write(f, cols, params):
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
    for table, column, ctype, pkey, ref in cols:
        kwargs = {
            'table': table.lower(),
            'column': column.lower(),
            'type': ctype,
        }
        if pkey:
            mtype = 'pk'
        elif ref:
            mtype = 'ref'
        else:
            mtype = ctype
        writer.writerow([
            params['dataset'].format(**kwargs),
            params['resource'].format(**kwargs),
            params['origin'].format(**kwargs),
            params['model'].format(**kwargs),
            column.lower(),
            mtype,
            params['model'].format(**{**kwargs, 'table': ref['table'].lower()}) if ref else '',
            '',  # const
            '',  # title
            '',  # description
            table,
            column,
            ref['table'] if ref else '',
            ref['column'] if ref else '',
        ])


def inspect(engine, schema=None):
    insp = reflection.Inspector.from_engine(engine)
    for table in insp.get_table_names(schema):
        pkey = insp.get_pk_constraint(table, schema)
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
                column['name'] in pkey['constrained_columns'],
                refs.get(column['name'], ''),
            )


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


def detect_type(ctype):
    for ct in ctype.__class__.__mro__:
        if ct in TYPES:
            return TYPES[ct]
    raise Exception("Can't detect column {column.name} type. Type MRO:\n - " + '\n - '.join(
        ct.__name__
        for ct in ctype.__class__.__mro__
    ))


if __name__ == "__main__":
    main()

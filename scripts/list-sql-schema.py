#!/usr/bin/env python

import sys

import click
import sqlalchemy as sa

from lodam.services.sqlschema import inspect, writecsv


@click.command()
@click.argument('dsn')
@click.option('--schema', help="database schema name")
@click.option('-o', '--output', help="output file")
@click.option('--dataset', default='datasets/example/data', help="dataset name")
@click.option('--resource', default='sql', help="resource name")
def main(dsn, schema, output, dataset, resource):
    engine = sa.create_engine(dsn)
    models = inspect(engine, schema)
    if output:
        with open(output, 'w') as f:
            writecsv(f, models, dataset=dataset, resource=resource)
    else:
        writecsv(sys.stdout, models, dataset=dataset, resource=resource)


if __name__ == "__main__":
    main()

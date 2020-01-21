#!/usr/bin/env python

import sys

import click
import sqlalchemy as sa

from lodam.services.sqlschema import inspect, writecsv


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
            writecsv(f, cols, params)
    else:
        writecsv(sys.stdout, cols, params)


if __name__ == "__main__":
    main()

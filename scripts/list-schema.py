#!/usr/bin/env python

import click

from spinta import commands
from spinta import components
from spinta.config import create_context


@click.command()
@click.option('--option', '-o', multiple=True, help='Set configuration option, example: `-o option.name=value`.')
def main(option):
    context = create_context(cli_args=option)

    _load_manifest(context)

    store = context.get('store')
    manifest = store.manifests['default']
    _traverse_namespaces(manifest.objects['ns'][''])


def _traverse_namespaces(ns: components.Namespace, level: int = 0):
    if level > 0:
        _list_properties(ns, level)
    for name in ns.names.values():
        print('  ' * level, name.title + '/')
        _traverse_namespaces(name, level + 1)


def _list_properties(ns: components.Namespace, level: int):
    props = {}
    for model in (ns.models or {}).values():
        for prop in (model.properties or {}).values():
            if prop.name.startswith('_'):
                continue
            if prop.name not in props:
                props[prop.name] = {}
            specifier = model.model_specifier()
            if specifier not in props[prop.name]:
                props[prop.name][specifier] = []
            props[prop.name][specifier].append(prop)

    for prop, models in props.items():
        types = ' | '.join(set(p.dtype.name for model in models.values() for p in model))
        model = 'yes' if '' in models else 'no'
        datasets = sum(1 for x in models if x)
        prop = '  ' * level + '  - ' + prop
        ref = _get_ref_object(models)
        print(f'{prop:42}  model={model:<3}  datasets={datasets:<2}  type={types}{ref}')


def _get_ref_object(models):
    for model in models.values():
        for p in model:
            if p.dtype.name in ('ref', 'backref') and p.dtype.model:
                return f'  ref={p.dtype.model.name}'
    return ''


def _load_manifest(context: components.Context) -> None:
    rc = context.get('config.raw')
    config = context.set('config', components.Config())
    store = context.set('store', components.Store())
    commands.load(context, config, rc)
    commands.check(context, config)
    commands.load(context, store, rc)
    commands.check(context, store)


if __name__ == "__main__":
    main()

import functools
import inspect
import re

from admanifest.manifest import Manifest, Schema, Value, Path


def schema_function(*args, **kwargs):
    injections = {
        'manifest': Manifest,
        'schema': Schema,
        'value': Value,
        'path': Path,
    }

    def decorator(func):
        inject = {}

        sig = inspect.signature(func)
        for name, param in sig.parameters.items():
            for varname, Class in injections.items():
                if param.annonation is Class:
                    inject[name] = varname
                    break

        @functools.wraps(func)
        def wrapper(**context):
            kw = dict(kwargs)
            for arg, name in inject.items():
                kw[arg] = context[name]
            return func(*args, **kw)

        return wrapper

    return decorator


@schema_function()
def get_data_source_schema():
    return {}


@schema_function()
def read_yml_files(base: str, manifest: Manifest):
    for path in (manifest.path / base).glob('**/*.yml'):
        print(path)


_NAME_PATTERN = re.compile(r'^[a-zA-Z_]+$')


_SOURCE_SCHEMA = {
    'csv': {
        'description': """
            See: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
        """,
        'properties': {
            'dsn': {'type': 'string'},
            'compression': {'enum': ['gzip', 'bz2', 'zip', 'xz']},
            'encoding': {'type': 'string'},
            'error_bad_lines': {'type': 'boolean'},
            'header': {
                'description': """
                    Row number(s) to use as the column names, and the start of the data. Default behavior is to
                    infer the column names: if no names are passed the behavior is identical to header=0 and
                    column names are inferred from the first line of the file, if column names are passed
                    explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be
                    able to replace existing names. The header can be a list of integers that specify row
                    locations for a multi-index on the columns e.g. [0,1,3]. Intervening rows that are not
                    specified will be skipped (e.g. 2 in this example is skipped). Note that this parameter
                    ignores commented lines and empty lines if skip_blank_lines=True, so header=0 denotes the
                    first line of data rather than the first line of the file.
                """,
                'oneof': [
                    {'type': 'integer'},
                    {'items': {'type': 'integer'}, 'type': 'array'},
                ],
            },
            'quotechar': {'type': 'string'},
            'quoting': {'enum': ['minimal', 'all', 'nonnumeric', 'none']},
            'sep': {
                'description': """
                    Delimiter to use. If sep is None, separator will be automatically detected using Python’s
                    builtin sniffer tool, csv.Sniffer. In addition, separators longer than 1 character and
                    different from '\\s+' will be interpreted as regular expressions.

                    Note that regex delimiters are prone to ignoring quoted data.
                """,
                'title': 'Separator',
                'type': 'string',
            },
            'skipfooter': {'type': 'integer'},
            'skiprows': {'type': 'integer'},
            'type': {'enum': ['csv']},
            'warn_bad_lines': {'type': 'boolean'},
        },
    },
    'excel': {
        'properties': {
            'dsn': {'type': 'string'},
            'header': {
                'oneof': [
                    {'type': 'integer'},
                    {'items': {'type': 'integer'}, 'type': 'array'},
                ],
            },
            'sheet': {'oneof': [{'type': 'string'}, {'type': 'integer'}]},
            'skipfooter': {'type': 'integer'},
            'skiprows': {'type': 'integer'},
            'type': {'enum': ['excel']},
        },
    },
    'htmltable': {
        'properties': {
            'attrs': {
                'type': 'object',
                'properties': {
                    re.compile(r'[a-z0-9_-]+'): {
                        'type': 'string',
                    },
                },
            },
            'dsn': {'type': 'string'},
            'match': {'type': 'string'},
            'skiprows': {'type': 'integer'},
            'type': {'enum': ['htmltable']},
        },
    },
    'json': {
        'properties': {
            'dsn': {'type': 'string'},
            'encoding': {'type': 'string'},
            'lines': {
                'description': 'Read file as one json object per line.\n',
                'type': 'boolean',
            },
            'type': {'enum': ['json']},
        },
    },
    'sql': {
        'properties': {
            'dsn': {
                'description': 'See: https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls',
                'type': 'string',
            },
            'encoding': {'type': 'string'},
            'type': {'enum': ['sql']},
        },
    },
    'xml': {
        'properties': {
            'dsn': {'type': 'string'},
            'encoding': {'type': 'string'},
            'type': {'enum': ['xml']},
        },
    },
}

_STARS = {
    'enum': [
        0,
        1,
        2,
        3,
        4,
        5,
    ]
}

MANIFEST = {
    'vocabulary': {
        'title': 'Data object',
        'description': 'Defines vocabulary for a single data object.',
        'type': 'object',
        'properties': {
            'id': {
                'type': 'string',
                'title': 'Data vocabulary ID',
                'required': True,
            },
            'type': {
                'enum': [
                    'vocabulary',
                ],
                'required': True,
            },
            'title': {
                'type': 'string',
                'title': 'Data vocabulary name',
            },
            'description': {
                'type': 'string',
                'title': 'Description of this data object',
            },
            'properties': {
                'type': 'object',
                'properties': {
                    _NAME_PATTERN: {
                        'type': 'object',
                        'title': 'Data field',
                        'properties': {
                            'type': {
                                'enum': [
                                    'string',
                                    'integer',
                                    'number',
                                ],
                                'required': True,
                            },
                            'title': {
                                'type': 'string',
                                'title': 'Data field name',
                            }
                        }
                    }
                }
            }
        }
    },

    'provider': {
        'type': 'object',
        'title': 'Data provider',
        'description': 'Information about data provider.',
        'properties': {
            'id': {
                'type': 'string',
                'title': 'Provider ID',
                'description': 'Unique idetifier for a provider withing this repository.',
                'required': True,
            },
            'type': {
                'enum': ['provider'],
                'required': True,
            },
            'title': {
                'title': 'Provider name',
                'type': 'string',
                'required': True,
            },
            'sector': {
                'enum': ['public', 'private'],
                'title': 'Provider organisation sector',
                'required': True,
            },
            'logo': {
                'type': 'string',
                'title': 'Provider logo',
                'description': """
                    Path to the provider logo. Path will be dynamically constructed, from media/, provider ID and logo
                    file name specified by this property.
                """,
            },
        },
    },

    'source': {
        'type': 'object',
        'title': 'Data source',
        'description': 'Information about data source and data provider by this source.\n',
        'services': {
            'select': read_yml_files('source'),
        },
        'properties': {
            'id': {
                'type': 'string',
                'title': 'Data source ID',
                'required': True,
            },
            'type': {
                'enum': ['source'],
                'required': True,
            },
            'title': {
                'type': 'string',
                'title': 'Data source name',
                'required': True,
            },
            'description': {
                'type': 'string',
                'title': 'Data source description',
            },
            'since': {'format': 'date', 'type': 'string', 'required': True},
            'until': {'format': 'date', 'type': 'string'},
            'stars': _STARS,
            'provider': {
                'type': 'string',
                'title': 'Data provider ID',
                'description': 'Reference to data provider.',
                'required': True,
            },
            'opengovdata': {
                'type': 'array',
                'title': 'Open government data principles',
                'items': {
                    'enum': [
                        'complete',
                        'primary',
                        'timely',
                        'accessible',
                        'machine_processable',
                        'non-discriminatory',
                        'non-proprietary',
                        'license-free',
                        'online_and_free',
                        'permanent',
                        'trusted',
                        'presumption_of_openness',
                        'documented',
                        'safe_to_open',
                    ],
                },
            },
            'source': {
                'schema': get_data_source_schema(),
                'title': 'Data source',
                'description': """
                    URI to the data source, you can use different schemes, like http, xml, html, csv and etc. to specify
                    how source data should be loaded.
                """,
            },
            'objects': {
                'type': 'object',
                'title': 'Data description',
                'properties': {
                    _NAME_PATTERN: {
                        'type': 'object',
                        'title': 'Data object',
                        'properties': {
                            'since': {'format': 'date', 'type': 'string'},
                            'until': {'format': 'date', 'type': 'string'},
                            'source': {
                                'type': 'string',
                                'title': 'Data source',
                                'description': 'ID of data source.',
                            },
                            'stars': _STARS,
                            'properties': {
                                'type': 'object',
                                'properties': {
                                    _NAME_PATTERN: {
                                        'type': 'object',
                                        'title': 'Data field',
                                        'properties': {
                                            'type': {
                                                'enum': [
                                                    'string',
                                                    'integer',
                                                    'numeric',
                                                ],
                                                'required': True,
                                            },
                                            'since': {'format': 'date', 'type': 'string'},
                                            'until': {'format': 'date', 'type': 'string'},
                                            'stars': _STARS,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },

    'project': {
        'type': 'object',
        'required': ['id', 'type', 'title', 'since'],
        'title': 'Data needed for a project',
        'description': 'Data description containing information about data needed for a project.\n',
        'properties': {
            'id': {
                'type': 'string',
                'title': 'Project ID',
                'description': 'Unique idetifier for a project withing a repository where all data descriptions are stored..\n',
                'required': True,
            },
            'type': {'enum': ['project']},
            'title': {'title': 'Project name', 'type': 'string'},
            'since': {'format': 'date', 'type': 'string'},
            'until': {'format': 'date', 'type': 'string'},
            'impact': {
                'type': 'array',
                'title': 'List of impact indicators by year',
                'items': {
                    'type': 'object',
                    'properties': {
                        'employees': {
                            'description': 'Number of emplyees, employed for specified year who worked on this project.',
                            'title': 'Number of emplyees',
                            'type': 'integer',
                        },
                        'revenue': {
                            'description': 'Revenue in Eruos generated for a specified year.',
                            'title': 'Revenue in Euros',
                            'type': 'number',
                        },
                        'users': {
                            'description': 'Number of unique project users for a specified year.\n',
                            'title': 'Number of users',
                            'type': 'integer',
                        },
                        'year': {'title': 'Year', 'type': 'integer'},
                    },
                },
            },
            'objects': {
                'type': 'object',
                'title': 'Data description',
                'properties': {
                    _NAME_PATTERN: {
                        'type': 'object',
                        'title': 'Data object',
                        'properties': {
                            'since': {'format': 'date', 'type': 'string'},
                            'until': {'format': 'date', 'type': 'string'},
                            'properties': {
                                'type': 'object',
                                'properties': {
                                    _NAME_PATTERN: {
                                        'properties': {
                                            'since': {
                                                'format': 'date',
                                                'type': 'string',
                                            },
                                            'type': {
                                                'enum': [
                                                    'string',
                                                    'integer',
                                                    'numeric',
                                                ],
                                            },
                                            'until': {
                                                'format': 'date',
                                                'type': 'string',
                                            },
                                        },
                                        'required': ['type'],
                                        'title': 'Data field',
                                        'type': 'object',
                                    },
                                },
                            },
                            'source': {
                                'description': 'ID of data source.',
                                'title': 'Data source',
                                'type': 'string',
                            },
                        },
                    },
                },
            },
        },
    },
}

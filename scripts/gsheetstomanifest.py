import collections
import json
import os
import pickle
import re

import click

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from spinta.config import create_context
from spinta import components
from spinta import commands


@click.command()
@click.option('-c', '--credentials', 'creds_file', help="Google Sheets API credentials (json file)")
@click.option('--cache/--no-cache', default=False, help="Cache results in a file")
@click.option('--dry-run', is_flag=True, default=False, help="Just show what will be done, but do not apply any changes")
@click.argument('sheet_url')
def main(creds_file, cache, dry_run, sheet_url):
    spreadsheet_id, sheet_id = parse_sheet_url(sheet_url)
    cache_file = f'gsheet-{spreadsheet_id}-{sheet_id}.json'

    data = None
    data_from_cache = False
    if cache and os.path.exists(cache_file):
        data_from_cache = True
        with open(cache_file) as f:
            data = json.load(f)

    if data is None:
        service = get_google_service(creds_file)
        data = get_sheet_data(service, spreadsheet_id, sheet_id)

    if cache and data_from_cache is False:
        with open(cache_file, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    rows = iter(data.get('values', []))

    # Skip first header row, because column names are on the second row.
    next(rows, None)

    columns = next(rows, None)
    columns = columns or [None]

    if columns[0] == 'dataset':
        schema = [
            'dataset',
            'resource',
            'model',
            'property',
            'type',
            'ref',
            'const',
            'source.object',
            'source.property',
        ]
    else:
        raise click.ClickException(f"Unknown first column {columns[0]!r}.")

    context = create_context()
    rc = context.get('config.raw')
    config = context.set('config', components.Config())
    store = context.set('store', components.Store())
    commands.load(context, config, rc)
    commands.check(context, config)
    commands.load(context, store, rc)
    commands.check(context, store)

    manifest_path = store.manifests['default'].path

    for i, row in enumerate(rows, 3):
        row = Row(schema, row)
        if row.dataset:
            path = manifest_path / ('datasets/' + row.dataset + '.yml')
            if path.exists():
                print(row.dataset, 'exists')
            else:
                print(row.dataset)
            # print(row.source.object)
            # print(row.source.property)


class Row:

    def __init__(self, schema, data):
        nested_schema = collections.defaultdict(list)
        nested_data = collections.defaultdict(list)
        for i, name in enumerate(schema):
            if len(data) > i:
                value = data[i]
            else:
                value = None

            if '.' in name:
                parent, name = name.split('.', 1)
                nested_schema[parent].append(name)
                nested_data[parent].append(value)
            else:
                setattr(self, name, value)

        for parent in nested_schema.keys():
            setattr(self, parent, Row(nested_schema[parent], nested_data[parent]))


def check_schema(schema, columns):
    errors = []
    for i, name in enumerate(schema):
        pos = i + 1
        if '.' in name:
            name = name.rsplit('.', 1)[1]
        if len(columns) <= i:
            errors.append(f"Missing column {name!r} at position {pos}.")
            continue
        if name != columns[i]:
            errors.append(f"Unknonw column {columns[i]!r} at position {pos}, expected {name!r} column.")
    if errors:
        raise click.ClickException('\n - ' + '\n - '.join(errors) + '\n')


def get_google_service(creds_file):
    creds = authenticate(creds_file)
    service = build('sheets', 'v4', credentials=creds)
    return service


def authenticate(creds_file, token_file='gsheetstoken.pickle'):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets.readonly',
    ]

    creds = None

    # Read token from cache.
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, scopes)
            creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(token_file, 'wb') as token:
        pickle.dump(creds, token)

    return creds


def get_sheet_data(service, spreadsheet_id, sheet_id):
    sheet = service.spreadsheets()
    name = get_sheet_name_by_id(service, spreadsheet_id, sheet_id)
    return sheet.values().get(spreadsheetId=spreadsheet_id, range=name).execute()


def get_sheet_name_by_id(service, spreadsheet_id, sheet_id):
    sheet = service.spreadsheets()
    result = sheet.get(spreadsheetId=spreadsheet_id).execute()
    sheets_by_id = {
        x['properties']['sheetId']: x['properties']['title']
        for x in result['sheets']
    }
    return sheets_by_id[sheet_id]


def parse_sheet_url(sheet_url):
    spreadsheet_id_match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url)
    if spreadsheet_id_match:
        spreadsheet_id = spreadsheet_id_match.group(1)
    else:
        raise click.ClickException(f"Can't find spreadsheet id from given URL '{sheet_url}'.")

    sheet_id_match = re.search(r'[#&]gid=([0-9]+)', sheet_url)
    if sheet_id_match:
        sheet_id = int(sheet_id_match.group(1))
    else:
        raise click.ClickException(f"Can't find sheet id from given URL '{sheet_url}'.")

    return spreadsheet_id, sheet_id


if __name__ == "__main__":
    main()

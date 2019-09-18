"""
Example:

    $ env/bin/python scripts/gsheetstomanifest.py \
        --cache \
        -c ~/Atsiuntimai/credentials.json \
        'https://docs.google.com/spreadsheets/d/4IbBbyphR8oU2cuNRBlZrByWJ2wZH0C7pRkul6YVypPC/edit#gid=6183807853'

If you wan't to refresh cache, just remove gsheet-*-*.json file:

    $ rm gsheet-4IbBbyphR8oU2cuNRBlZrByWJ2wZH0C7pRkul6YVypPC-6183807853.json

Here `4IbBbyphR8oU2cuNRBlZrByWJ2wZH0C7pRkul6YVypPC` is document id, and `6183807853` is sheet id.

"""

import click

from lodam.services.gsheets import get_gsheet_rows
from lodam.services.gsheets import load_spinta_context
from lodam.services.gsheets import update_manifest_files


@click.command()
@click.option('-c', '--credentials', 'creds_file', help="Google Sheets API credentials (json file)")
@click.option('--cache/--no-cache', default=False, help="Cache results in a file, defaults to no-cache")
@click.option('--dry-run', is_flag=True, default=False, help="Just show what will be done, but do not apply any changes")
@click.argument('sheet_url')
def main(creds_file, cache, dry_run, sheet_url):
    rows = get_gsheet_rows(sheet_url, cache, creds_file)
    context = load_spinta_context()
    update_manifest_files(context, rows)


if __name__ == "__main__":
    main()

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

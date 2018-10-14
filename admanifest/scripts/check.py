#!/usr/bin/env python

import sys
from pathlib import Path
from ruamel.yaml import YAML

from admanifest.manifest import load_manifest_data

yaml = YAML(typ='safe')


def main():
    here = Path()
    result = load_manifest_data(here)
    if result.errors:
        for error in result.errors:
            print(error)
        return 1
    else:
        print("All seems to be OK.")


if __name__ == "__main__":
    sys.exit(main())

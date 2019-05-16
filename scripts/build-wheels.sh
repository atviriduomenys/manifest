#!/bin/sh

set -e -x

if [ -d var/wheels ] ; then
    rm -r var/wheels
fi

mkdir -p var/wheels

mkdir -p ci

python -m venv ci/env
ci/env/bin/pip install wheel
ci/env/bin/pip wheel --find-links=/opt/wheels --wheel-dir=var/wheels -r requirements.txt -e .

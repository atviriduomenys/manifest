FROM python:3.7-alpine

RUN apk update \
 && apk add --no-cache \
        python-dev build-base git postgresql-dev libxslt-dev libxml2-dev \
        libpq libxml2 libxslt libffi-dev gfortran py-numpy-dev freetype-dev \
        libpng-dev linux-headers py-setuptools


COPY requirements-dev.txt /tmp/requirements-dev.txt

RUN python -m venv /opt/venv \
 && /opt/venv/bin/pip install wheel numpy \
 && /opt/venv/bin/pip wheel -w /opt/wheels -r /tmp/requirements-dev.txt

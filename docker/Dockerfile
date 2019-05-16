FROM python:3.7-alpine

ENV SPINTA_ENV=prod
ENV SPINTA_CONFIG=lodam.config:CONFIG
ENV SPINTA_CONFIG_PATH=/opt/lodam/config
ENV SPINTA_MANIFESTS_DEFAULT_PATH=/opt/lodam/manifest
ENV PATH=/opt/lodam/env/bin:$PATH

COPY var/wheels/*.whl /tmp/wheels/
COPY manifest/ /opt/lodam/manifest/
COPY tests/config/ /opt/lodam/config/

RUN apk add --no-cache libpq libxml2 libxslt

RUN python -m venv /opt/lodam/env \
 && /opt/lodam/env/bin/pip install --no-index -f /tmp/wheels lodam

EXPOSE 9000

WORKDIR /opt/lodam

CMD ["uvicorn", "spinta.asgi:app", "--host", "0.0.0.0", "--port", "9000"]

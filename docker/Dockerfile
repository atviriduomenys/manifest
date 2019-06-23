FROM python:3.7-slim
RUN mkdir /opt/atviriduomenys
WORKDIR /opt/atviriduomenys
RUN apt-get update \
 && apt-get install -y --no-install-recommends git build-essential python-dev
COPY . manifest
RUN set -xe \
 && python --version \
 && python -m venv env \
 && env/bin/pip install --upgrade wheel pip \
 && env/bin/pip wheel -w wheels -r manifest/requirements.txt -e manifest


FROM python:3.7-slim
RUN mkdir /opt/atviriduomenys
WORKDIR /opt/atviriduomenys
ENV SPINTA_ENV=production
ENV SPINTA_CONFIG=lodam.config:CONFIG
ENV SPINTA_CONFIG_PATH=/opt/atviriduomenys/config
ENV SPINTA_MANIFESTS_DEFAULT_PATH=/opt/atviriduomenys/manifest
ENV PATH=/opt/atviriduomenys/env/bin:$PATH
COPY --from=0 /opt/atviriduomenys/wheels/*.whl wheels/
RUN set -xe \
 && python --version \
 && python -m venv env \
 && env/bin/pip install --no-index -f wheels lithuanian-open-data-manifest
EXPOSE 9000
CMD ["uvicorn", "spinta.asgi:app", "--host", "0.0.0.0", "--port", "9000"]

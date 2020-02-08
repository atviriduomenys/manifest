.PHONY: env
env: .env env/.done requirements.txt requirements-dev.txt docs/requirements.txt

env/bin/pip:
	python3.8 -m venv env
	env/bin/pip install --upgrade pip wheel setuptools

env/.done: env/bin/pip setup.py requirements-dev.txt
	env/bin/pip install -r requirements-dev.txt -e .
	touch env/.done

env/bin/pip-compile: env/bin/pip
	env/bin/pip install pip-tools

requirements-dev.txt: env/bin/pip-compile requirements.in requirements-dev.in
	env/bin/pip-compile --no-index requirements.in requirements-dev.in -o requirements-dev.txt

requirements.txt: env/bin/pip-compile requirements.in
	env/bin/pip-compile --no-index requirements.in -o requirements.txt

docs/requirements.txt: env/bin/pip-compile docs/requirements.in
	env/bin/pip-compile --no-index docs/requirements.in -o docs/requirements.txt

.env: .env.example
	cp -n .env.example .env | true
	touch .env

.PHONY: upgrade
upgrade: env/bin/pip-compile
	env/bin/pip-compile --upgrade --no-index requirements.in -o requirements.txt
	env/bin/pip-compile --upgrade --no-index requirements.in requirements-dev.in -o requirements-dev.txt
	env/bin/pip-compile --upgrade --no-index docs/requirements.in docs/requirements.txt

.PHONY: test
test: env
	env/bin/py.test -vvxra --cov=lodam --cov-report=term-missing tests

.PHONY: dist
dist: env/bin/pip
	env/bin/python setup.py sdist bdist_wheel

.PHONY: run
run: env
	AUTHLIB_INSECURE_TRANSPORT=1 env/bin/uvicorn spinta.asgi:app --debug

.PHONY: build-image
build-image:
	docker build -t registry.gitlab.com/atviriduomenys/manifest:latest -f docker/Dockerfile .

.PHONY: push-image
push-image:
	docker push registry.gitlab.com/atviriduomenys/manifest

.PHONY: docs-auto
docs-auto:
	$(MAKE) -C docs auto

.PHONY: docs-open
docs-open:
	$(MAKE) -C docs open

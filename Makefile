.PHONY: env
env: .env env/.done requirements.txt

env/bin/pip:
	python3.7 -m venv env
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

.env: .env.example
	cp -n .env.example .env | true
	touch .env

.PHONY: upgrade
upgrade: env/bin/pip-compile
	env/bin/pip-compile --upgrade --no-index requirements.in -o requirements.txt
	env/bin/pip-compile --upgrade --no-index requirements.in requirements-dev.in -o requirements-dev.txt

.PHONY: test
test: env
	env/bin/py.test -vvxra --tb=native --cov=lodam --cov-report=term-missing tests

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
	docker push registry.gitlab.com/atviriduomenys/manifest:latest

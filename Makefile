env/done: env/bin/pip requirements.txt requirements-dev.txt
	env/bin/pip install -r requirements-dev.txt -e .
	touch env/done

env/bin/pip:
	python3.5 -m venv env

requirements.txt: env/bin/pip-compile requirements.in
	env/bin/pip-compile --no-index requirements.in -o requirements.txt

requirements-dev.txt: env/bin/pip-compile requirements.in requirements-dev.in
	env/bin/pip-compile --no-index requirements.in requirements-dev.in -o requirements-dev.txt

env/bin/pip-compile: env/bin/pip
	env/bin/pip install pip-tools

.PHONY: check
check: env/done
	env/bin/admanifest-check

.PHONY: test
test: env/done
	env/bin/py.test -vvxra --tb=native tests

.PHONY: upgrade
upgrade: env/bin/pip-compile
	env/bin/pip-compile --upgrade --no-index requirements.in requirements-dev.in -o requirements-dev.txt

.PHONY: clean
clean:
	rm -r env
	find -iname '*.pyc' -delete

env/done: env/bin/pip scripts/requirements.txt
	env/bin/pip install -r scripts/requirements.txt
	touch env/done

env/bin/pip:
	python3 -m venv env

scripts/requirements.txt: env/bin/pip-compile scripts/requirements.in
	env/bin/pip-compile --no-index scripts/requirements.in -o scripts/requirements.txt

env/bin/pip-compile: env/bin/pip
	env/bin/pip install pip-tools

.PHONY: check
check: env/done
	env/bin/python scripts/check.py

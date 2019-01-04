PYVER = $(shell poetry run python -c "import sys; print(*sys.version_info[:2], sep='.')")
VENVS = $(shell poetry config settings.virtualenvs.path | tr -d '"')
VENV = $(VENVS)/open-data-manifest-py$(PYVER)

.PHONY: env
env: $(VENV)/done

.PHONY: check
check: env
	poetry run admanifest-check

.PHONY: test
test: env
	poetry run py.test -vvxra --tb=native tests

$(VENV)/done: pyproject.toml
	poetry install
	touch $(VENV)/done

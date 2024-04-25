.PHONY: clean clean_tox envs help piptools requirements secrets selfcheck upgrade

.DEFAULT_GOAL := help

# --------------------------------------------------------------------------------------
# Base
# --------------------------------------------------------------------------------------

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## remove generated byte code, coverage reports, and build artifacts
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	coverage erase
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean_tox: ## clear tox requirements cache
	rm -fr .tox

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

# --------------------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------------------

piptools: ## install pinned version of pip-compile and pip-sync
	pip install -qr requirements/pip.txt
	pip install -qr requirements/pip-tools.txt

PIP_COMPILE_OPTS = --strip-extras
PIP_COMPILE = pip-compile --upgrade $(PIP_COMPILE_OPTS)
PIP_COMPILE_UNSAFE = $(PIP_COMPILE) --allow-unsafe

# Make sure to order requirements based on their include layer hierarchy!
REQUIREMENTS_GROUPS := pip pip-tools base ci test-ci test quality dev

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: piptools ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	@for group in $(REQUIREMENTS_GROUPS); do \
		CMD=$$( [ $$group = "pip" ] && echo "$(PIP_COMPILE_UNSAFE)" || echo "$(PIP_COMPILE)" ); \
		$$CMD -o requirements/$$group.txt requirements/$$group.in; \
	done

requirements: clean_tox piptools ## install development environment requirements
	pip-sync -q requirements/dev.txt

# --------------------------------------------------------------------------------------
# Setup
# --------------------------------------------------------------------------------------

# Find all example env files in the project
EXAMPLE_ENV_FILES := $(shell find . -type f -name "*.env.example")

envs: # generate env files required to configure application environment
	@echo "Generating env files from the following example files:"
	@echo "$(EXAMPLE_ENV_FILES)"
	@for file in $(EXAMPLE_ENV_FILES); do \
		env_name=$$(basename "$$file" | sed -e 's/\.env\.example$$//'); \
		cp "$$file" "$$(dirname "$$file")/$$env_name.env"; \
	done

# Find all placeholder secret files in the project
PLACEHOLDER_FILES := $(shell find . -type f -name "_*.txt")

secrets: # generate secrets required by Compose application model
	@echo "Generating secrets from the following files:"
	@echo "$(PLACEHOLDER_FILES)"
	@for file in $(PLACEHOLDER_FILES); do \
		secret_name=$$(basename "$$file" | sed -e 's/^_//' -e 's/\.txt$$//'); \
		openssl rand -base64 24 | tr -d '\n' > "$$(dirname "$$file")/$$secret_name.txt"; \
	done

.PHONY: build build.all build.dev build.test dev dev.admin healthy help \
	selfcheck sync test test.admin watch.dev watch.test

.DEFAULT_GOAL := help

# ------------------------------------------------------------------------------
# Base
# ------------------------------------------------------------------------------

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

# TODO(apexDev37)
healthy: ## checks the compose app model is valid
	@echo "The compose application model is valid"

# TODO(apexDev37)
sync: ## checks local and in-container interpreter/package manager are synced

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

# ------------------------------------------------------------------------------
# Build
# ------------------------------------------------------------------------------

build: ## build the base, `web` service image with default env: `production`
	 @docker build . \
	 	--file src/Dockerfile \
		--target final-stage \
		--tag djangops:base

build.all: ## build all `web` service images for all supported target envs
build.all: build build.test build.dev

build.dev: ## build the dev, `web` service image with target env: `develop`
	 @docker build . \
	 	--file src/Dockerfile \
		--target env-develop \
		--tag djangops:dev

build.test: ## build the test, `web` service image with target env: `testing`
	 @docker build . \
	 	--file src/Dockerfile \
		--target env-testing \
		--tag djangops:test

# ------------------------------------------------------------------------------
# Up
# ------------------------------------------------------------------------------

dev: ## run core compose services with the develop environment target
	@echo "Starting core services in [develop] mode."
	@docker compose \
		-f compose.yaml \
		-f compose.develop.yaml \
		up -d

dev.admin: ## run adminer profile service with the develop environment target
	@echo "Starting core services and adminer profile in [develop] mode."
	@docker compose \
		-f compose.yaml --profile admin \
		-f compose.develop.yaml \
		up -d

test: ## run core compose services with the testing environment target
	@echo "Starting core services in [testing] mode."
	@docker compose \
		-f compose.yaml \
		-f compose.testing.yaml \
		up -d

test.admin: ## run adminer profile service with the testing environment target
	@echo "Starting core services and adminer profile in [testing] mode."
	@docker compose \
		-f compose.yaml --profile admin \
		-f compose.testing.yaml \
		up -d

# ------------------------------------------------------------------------------
# Watch: Targets to run compose services in watch mode.
# ------------------------------------------------------------------------------

watch.dev: ## watch `service:web` and start core services with develop target
	@echo "Starting core services and watching 'web' service in [develop] mode."
	@docker compose \
		-f compose.yaml -f compose.develop.yaml \
		watch --no-up

watch.test: ## watch `service:web` and start core services with testing target
	@echo "Starting core services and watching 'web' service in [testing] mode."
	@docker compose \
		-f compose.yaml -f compose.testing.yaml \
		watch --no-up

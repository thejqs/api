list:
	@echo "Available commands:"
	@echo "+++++++++++++++++++"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | \
		awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | \
		sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

help: list

local-build:
	DOCKER_BUILDKIT=0 docker-compose \
		-f "docker-compose.yml" \
		build

local-load-data:
	docker-compose -f "docker-compose.yml" run --rm web python manage.py load_data

local-makemigrations:
	docker-compose -f "docker-compose.yml" run --rm web python manage.py makemigrations

local-migrate:
	docker-compose -f "docker-compose.yml" run --rm web python manage.py migrate

local-pg-cli:
	docker exec -it api-db-1 bash

local-run:
	docker-compose -f "docker-compose.yml" up

local-shell:
	docker-compose -f "docker-compose.yml" run --rm web python manage.py shell

local-shell-plus:
	docker-compose -f "docker-compose.yml" run --rm web python ./manage.py shell_plus

local-shell-plus-sql:
	docker-compose -f "docker-compose.yml" run --rm web python manage.py shell_plus \
		--print-sql

local-teardown-all-containers:
	docker system prune -a

.PHONY: \
	list \
	help \
	local-build \
	local-load-data \
	local-makemigrations \
	local-migrate \
	local-pg-cli \
	local-run \
	local-shell \
	local-shell-plus \
	local-shell-plus-sql \
	local-teardown-all-containers \

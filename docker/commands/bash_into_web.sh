#!/bin/bash
#
# Bash interactively into the `web` svc (service container).
#
# Note:
# The ad-hoc behavior of `docker compose run` creates new instances on each run,
# which need to be removed manually. Therefore, we use `docker compose exec`
# which is ideal for this context to connect to a running service container.
# Hence, prefer the latter.
#
# Instructions:
# ➜ chmod +x ./docker/commands/bash_into_web.sh
# ➜ ./docker/commands/bash_into_web.sh

# define the directory of the script being executed dynamically.
SCRIPT_DIR=$(realpath "$0")
PROJECT_ROOT_DIR=$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")

# define path to local compose file relative to `this` script.
COMPOSE_FILE_PATH="$PROJECT_ROOT_DIR/compose.yaml"

# define the default shell command.
DEFAULT_SHELL="/bin/sh"

# Get the ID of the running web container.
web_svc_id=$(docker compose -f "$COMPOSE_FILE_PATH" ps -q web)

if [[ -z "$web_svc_id" ]]; then
  echo "Starting web service..."
  docker compose up --no-deps -d web
fi

# Bash into running `web` svc.
docker compose exec -it web $DEFAULT_SHELL

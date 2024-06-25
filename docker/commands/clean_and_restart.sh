#!/bin/bash
#
# Clean all traces of the compose model, rebuild, and restart services.
# This is ideal for users who want to start from scratch.
#
# Warning:
# This operation will:
#   1. stop all running services
#   2. delete all service containers, networks, and volumes
#   3. rebuild the entire compose application model from scratch
#
# Instructions:
# ➜ chmod +x ./docker/commands/clean_and_restart.sh
# ➜ ./docker/commands/clean_and_restart.sh

# Function to recursively search for `compose.yaml` in parent dirs.
find_compose_file()
{
  local current_dir
  current_dir=$(pwd)
  while [[ "$current_dir" != "/" ]]; do
    if [[ -f "$current_dir/compose.yaml" ]]; then
      echo "$current_dir/compose.yaml"
      return 0
    fi
    current_dir=$(dirname "$current_dir")
  done
  echo "compose.yaml file not found."
  exit 1
}

# Function to warn user and prompt for confirmation.
prompt_user_confirm()
{
  echo "Warning: This will result in data loss for any persisted storage."
  read -p "Are you sure you want to proceed? (y/N): " -r
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operation aborted."
    exit 1
  fi
}

# Function to encapsulate docker execution tasks.
docker_exec_operation()
{
  # Stop all services
  docker compose -f "$COMPOSE_FILE_PATH" stop
  # Remove all containers, networks, and volumes
  docker compose -f "$COMPOSE_FILE_PATH" down --volumes
  # Rebuild and restart all services
  docker compose -f "$COMPOSE_FILE_PATH" up \
    --build --force-recreate --remove-orphans
}

# Main function entry-point to execute the script.
main()
{
  COMPOSE_FILE_PATH=$(find_compose_file)
  prompt_user_confirm
  docker_exec_operation
  echo "Operation completed successfully."
  exit 0
}

# Execute the main function.
main

#!/bin/bash
#
# Removes system-wide untagged dangling images from Docker rebuilds.

err()
{
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*" >&2
}

remove_dangling_images()
{
  local image_ids
  image_ids=$(docker images --filter "dangling=true" -q)

  if [[ -n "$image_ids" ]]; then
    echo "Listing dangling images:"
    docker images --filter "dangling=true"

    read -p "Dangling images listed above. Remove them? (y/N) " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
      docker rmi -f "$image_ids" || err "Failed to remove some images."
    else
      echo "Aborted!"
    fi
  else
    echo "No dangling images found."
  fi
}

remove_dangling_images

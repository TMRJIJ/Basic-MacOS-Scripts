#!/bin/bash

# Set the directory you want to work in
TARGET_DIR=""

# Make sure we're working within the correct directory
if [ ! -d "$TARGET_DIR" ]; then
  echo "The specified directory does not exist: $TARGET_DIR"
  exit 1
fi

# Change to the specified directory
cd "$TARGET_DIR" || exit

# Loop through all directories in the target directory
for dir in "$TARGET_DIR"/*/; do
  # Check if the directory contains exactly one subdirectory
  subdir=$(find "$dir" -mindepth 1 -maxdepth 1 -type d)
  if [ "$(echo "$subdir" | wc -l)" -eq 1 ]; then
    # Move all files from the subdirectory to the parent directory
    mv "$subdir"/* "$dir"
    # Remove the now-empty subdirectory
    rmdir "$subdir"
  fi
done

echo "Images moved and empty folders removed."

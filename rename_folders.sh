#!/bin/bash


# Loop through each folder
for dir in */; do
    # Remove the trailing slash from the directory name
    dir_name="${dir%/}"

    # Get the first image file in the directory (assuming all files in the directory belong to the same set)
    first_image=$(ls "$dir" | head -n 1)

    # Extract the set name from the image file (assuming format "photoevent-set-1-img-1.jpg")
    if [[ $first_image =~ ^(.+)-[0-9]+\.jpg$ ]]; then
        set_name="${BASH_REMATCH[1]}"

        # Rename the directory if the set name is different from the current directory name
        if [[ "$dir_name" != "$set_name" ]]; then
            mv "$dir" "$set_name"
            echo "Renamed $dir_name to $set_name"
        fi
    fi
done

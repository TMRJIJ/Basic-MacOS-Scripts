import os
import re

def get_resolution(filename):
    match = re.match(r'(\d+)x(\d+)_', filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

def delete_lower_res_images(directory):
    images = {}

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Add other image formats if needed
            resolution = get_resolution(filename)
            if resolution:
                base_filename = filename.split('_', 1)[1]  # Extract unique identifier after the resolution
                # Check if this file is the highest resolution version
                if base_filename not in images or resolution > images[base_filename][0]:
                    # If a lower resolution version exists, mark it for deletion
                    if base_filename in images:
                        os.remove(os.path.join(directory, images[base_filename][1]))
                    images[base_filename] = (resolution, filename)

if __name__ == "__main__":
    # Ask user to input the folder path
    directory = input("Please enter the path to the folder containing the images: ")

    # Check if the provided path is valid
    if os.path.isdir(directory):
        delete_lower_res_images(directory)
        print(f"Lower resolution images have been deleted from {directory}.")
    else:
        print("The provided directory does not exist. Please check the path and try again.")

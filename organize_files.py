import os
import shutil

# Base directory where your files are located
base_directory = ''

# Get a list of all files in the directory
files = os.listdir(base_directory)

# Iterate through each file in the directory
for file in files:
    # Skip hidden files like .DS_Store
    if file.startswith('.'):
        continue

    # Get the set name from the file name (e.g., 'albumname-pic-1')
    set_name = file.rsplit('-', 1)[0]

    # Create a directory for the set if it doesn't already exist
    set_folder = os.path.join(base_directory, set_name)
    if not os.path.exists(set_folder):
        os.makedirs(set_folder)

    # Move the file into the corresponding set directory
    shutil.move(os.path.join(base_directory, file), os.path.join(set_folder, file))

print("Files organized successfully.")

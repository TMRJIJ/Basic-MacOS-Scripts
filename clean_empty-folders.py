import os

def remove_empty_folders(directory):
    # Iterate over all the directories and subdirectories
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            # Check if the directory is empty
            if not os.listdir(folder_path):
                print(f"Removing empty folder: {folder_path}")
                os.rmdir(folder_path)

# Specify the directory where you want to remove empty folders
base_directory = ''

# Call the function to remove empty folders
remove_empty_folders(base_directory)

print("Empty folders removed successfully.")

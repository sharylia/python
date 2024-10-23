import os

def list_files_in_directory(directory_path):
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
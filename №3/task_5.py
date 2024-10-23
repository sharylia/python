import os
import time

def file_stats(filepath):
    if not os.path.isfile(filepath):
        return None

    size = os.path.getsize(filepath)
    last_modified = time.ctime(os.path.getmtime(filepath))
    name, extension = os.path.splitext(os.path.basename(filepath))
    
    return {
        'size': size,
        'last_modified': last_modified,
        'name': name,
        'extension': extension
    }
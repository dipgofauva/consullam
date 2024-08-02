import os

def get_latest_modified_date(directory):
    latest_modified_date = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_date = os.path.getmtime(file_path)
            if file_modified_date > latest_modified_date:
                latest_modified_date = file_modified_date
    return latest_modified_date

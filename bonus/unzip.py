import zipfile

def unarchive(filepath, dest_directory):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(dest_directory)

if __name__ == "__main__":
    unarchive(filepath="compressed_files/compressed.zip", dest_directory="unarchive")
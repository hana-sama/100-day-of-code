import zipfile
import pathlib

def make_archive(filepaths, dest_directory):
    dest_path = pathlib.Path(dest_directory, "compressed_3.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py", "bonus2.py"], dest_directory="compressed_files")
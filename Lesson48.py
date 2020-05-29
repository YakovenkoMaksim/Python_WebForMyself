import zipfile
import os

folder_path = '/Users/yakovenko/Documents/GitHub/Python_WebForMyself/test'
zip_path = '/Users/yakovenko/Documents/GitHub/Python_WebForMyself/test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

for folder, subfolders, files in os.walk(folder_path):
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), folder_path),
                     compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()

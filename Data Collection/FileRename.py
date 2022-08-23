import glob

from tqdm import tqdm
from zipfile import ZipFile

# Zip file list
file_list = glob.glob("../Image/농산물 품질(QC) 이미지/Validation/*.zip")
json_zip_list, image_zip_list = list(), list()
for file_dir in file_list:
    if file_dir.split("\\")[-1][0] == "[":
        json_zip_list.append(file_dir)
    else:
        image_zip_list.append(file_dir)

# Unzip
for json_zip in tqdm(json_zip_list):
    with ZipFile(json_zip, "r") as zip:
        zip.extractall("temp_val/json")
print("JSON File is unzipped in temp folder")

for image_zip in tqdm(image_zip_list):
    with ZipFile(image_zip, "r") as zip:
        zip.extractall("temp_val/image")
print("Image File is unzipped in temp folder")

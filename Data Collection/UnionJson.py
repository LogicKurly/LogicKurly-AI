import glob
import json

from tqdm import tqdm

# Union
QC_json = ".\\data.json"
Crawling_json = ".\\CrawlingData.json"

json_file_list = [QC_json, Crawling_json]

json_dict = dict()
images, categories, annotations = list(), list(), list()
for json_file in json_file_list:
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        images.append(json_data["images"])
        annotations.append(json_data["annotations"])
categories.append(json_data["categories"])

json_dict["images"] = images
json_dict["categories"] = categories
json_dict["annotations"] = annotations

# Write json file
with open("./union.json", "w", encoding="utf-8") as make_file:
    json.dump(json_dict, make_file, indent="\t")

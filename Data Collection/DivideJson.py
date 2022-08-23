import glob
import json

from tqdm import tqdm

# Category
keyword_list = [
    "onion",  # 양파 : 0
    "garlic",  # 마늘 : 1
    "carrot",  # 당근 : 2
    "paprika",  # 파프리카 : 3
    "chili",  # 고추 : 4
    "egg",  # 달걀 : 5
    "tofu",  # 두부 : 6
    "mushroom",  # 버섯 : 7
    "potato",  # 감자 : 8
    "daikon",  # 무 : 9
    "sweet pumpkin",  # 단호박 : 10
    "green onion",  # 대파 : 11
    "milk",  # 우유 : 12
    "tomato",  # 토마토 : 13
    "young squash",  # 애호박 : 14
    "chives",  # 부추 : 15
    "cucumber",  # 오이 : 16
    "ginger",  # 생강 : 17
    "sweet potato",  # 고구마 : 18
    "eggplant",  # 가지 : 19
    "basil",  # 바질 : 20
    "spinach",  # 시금치 : 21
    "lettuce",  # 양상추 : 22
    "napa cabbage",  # 배추 : 23
    "cabbage",  # 양배추 : 24
]

# Union
id_list = glob.glob("./Crawling/image/*.jpg")
index = 0  # len(id_list)
img_index, obj_index = index, index


json_file = ".\\식재료-10.json"

with open(json_file, "r", encoding="utf-8") as f:
    json_data = json.load(f)

categories = list()
for category in json_data["categories"]:
    category_dict = dict()
    category_dict["id"] = category["id"] - 30
    category_dict["name"] = category["name"]
    categories.append(category_dict)

for idx, image in tqdm(enumerate(json_data["images"])):
    json_dict, image_dict = dict(), dict()
    images, annotations = list(), list()
    
    image_dict["id"] = image["id"] - 9789 + img_index
    image_dict["file_name"] = image["file_name"]
    image_dict["width"] = image["width"]
    image_dict["height"] = image["height"]
    images.append(image_dict)

    for annotation in json_data["annotations"]:
        annotation_dict = dict()
        if annotation["image_id"] == image["id"]:
            annotation_dict["image_id"] = image_dict["id"]
        else:
            continue 
        
        annotation_dict["id"] = obj_index  # 이미지 하나당 객체 하나라서 가능
        annotation_dict["bbox"] = annotation["bbox"]
        annotation_dict["category_id"] = annotation["category_id"] - 30
        annotations.append(annotation_dict)
        obj_index += 1

    json_dict["images"] = images
    json_dict["categories"] = categories
    json_dict["annotations"] = annotations

    # Write json file
    with open(f"./CrawlingJson/CrawlingData_{idx+img_index}.json", "w", encoding="utf-8") as make_file:
        json.dump(json_dict, make_file, indent="\t")

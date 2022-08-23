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

categories = list()

for index, keyword in enumerate(keyword_list):
    category_dict = dict()
    category_dict["id"] = index
    category_dict["name"] = keyword

    categories.append(category_dict)

# Union
id_list = glob.glob("./val/image/*.png")
index = len(id_list)

json_dict = dict()
images, annotations = list(), list()
json_file_list = glob.glob("./temp_val/json/*.json")

target_keyword = [
    ["onion", 0],
    ["garlic", 1],
    ["potato", 8],
    ["radish", 9],
    ["chinese-cabbage", 23],
    ["cabbage", 24],
]
for json_file in tqdm(json_file_list):
    for keyword, category_id in target_keyword:
        if keyword in json_file.split("\\")[-1].split(".")[0]:
            break
    else:
        continue

    image_dict = dict()
    annotation_dict = dict()
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        image_dict["id"] = index
        image_dict["file_name"] = json_file.split("\\")[-1].split(".")[0] + ".png"
        image_dict["width"] = json_data["img_width"]
        image_dict["height"] = json_data["img_height"]

        annotation_dict["image_id"] = index
        annotation_dict["id"] = index  # 이미지 하나당 객체 하나라서 가능
        annotation_dict["bbox"] = [
            json_data["bndbox"]["xmin"],
            json_data["bndbox"]["ymin"],
            json_data["img_width"],
            json_data["img_height"],
        ]

        annotation_dict["category_id"] = category_id
        images.append(image_dict)
        annotations.append(annotation_dict)
        index += 1

json_dict["images"] = images
json_dict["categories"] = categories
json_dict["annotations"] = annotations

# Write json file
with open("./val/val.json", "w", encoding="utf-8") as make_file:
    json.dump(json_dict, make_file, indent="\t")

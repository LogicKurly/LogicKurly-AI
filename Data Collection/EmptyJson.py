import os
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


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

# Union
json_dict = dict()
images, annotations = list(), list()

json_dict["images"] = images
json_dict["categories"] = categories
json_dict["annotations"] = annotations

# Write json file
createDirectory("./sample/")
with open("./sample/sample.json", "w", encoding="utf-8") as make_file:
    json.dump(json_dict, make_file, indent="\t")

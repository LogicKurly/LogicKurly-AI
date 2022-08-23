import io
from pickletools import read_uint1
from torchvision import models
import json
from flask import Flask, jsonify, request
from flask import make_response
import torchvision.transforms as transforms
import torch
from PIL import Image
import os

app = Flask(__name__)

# yolo model 불러오기
model = torch.hub.load(
    "/home/ec2-user/yolov5/",
    "custom",
    path="/home/ec2-user/yolov5/kurly_NY/20220823-KNY-Yolov5-n3/weights/best.pt",
    source="local",
)

# POST 통신으로 들어오는 이미지를 저장하고 모델로 추론하는 과정
def save_image(file):
    file.save("/home/ec2-user/temp/" + file.filename)


@app.route("/")
def web():
    return "Ingredient API"


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]
        save_image(file)  # 들어오는 이미지 저장
        train_img = "/home/ec2-user/temp/" + file.filename
        temp = model(train_img)
        result = temp.pandas().xyxy[0]["name"]

        # category
        # categories = dict()
        # categories['onion'] = 0
        # categories['garlic'] = 1
        # categories['carrot'] = 2
        # categories['paprika'] = 3
        # categories['chili'] = 4
        # categories['egg'] = 5
        # categories['tofu'] = 6
        # categories['mushroom'] = 7
        # categories['potato'] = 8
        # categories['daikon'] = 9
        # categories['sweet pumpkin'] = 10
        # categories['green onion'] = 11
        # categories['milk'] = 12
        # categories['tomato'] = 13
        # categories['young squash'] = 14
        # categories['chives'] = 15
        # categories['cucumber'] = 16
        # categories['ginger'] = 17
        # categories['sweet potato'] = 18
        # categories['eggplant'] = 19
        # categories['basil'] = 20
        # categories['spinach'] = 21
        # categories['lettuce'] = 22
        # categories['napa cabbage'] = 23
        # categories['cabbage'] = 24

        answer = set()
        for i in range(len(result)):
            answer.add(result[i])

        name = file.filename

        res = {"answer": list(answer), "name": name}
        print(res)
        return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

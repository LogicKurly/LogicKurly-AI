## 정적 크롤링

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from tqdm import tqdm

import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


baseUrl = "https://www.foodiesfeed.com/?s="
pixabayUrl = "https://pixabay.com/ko/images/search/"

keyword_list = [
    "onion",  # 양파
    "garlic",  # 마늘
    "carrot",  # 당근
    "paprika",  # 파프리카
    "chili",  # 고추
    "egg",  # 달걀
    "tofu",  # 두부
    "mushroom",  # 버섯
    "potato",  # 감자
    # 'daikon', # 무 (데이터 없음)
    "sweet pumpkin",  # 단호박
    "green onion",  # 대파
    "milk",  # 우유
    "tomato",  # 토마토
    "young squash",  # 애호박
    "chives",  # 부추
    "cucumber",  # 오이
    "ginger",  # 생강
    "sweet potato",  # 고구마
    "eggplant",  # 가지
    "basil",  # 바질
    "spinach",  # 시금치
    "lettuce",  # 양상추
    "napa cabbage",  # 배추
]

print(f"키워드는 총 {len(keyword_list)} 개")

keyword_list = ['sweet potato']
for idx, keyword in enumerate(keyword_list):
    print(f"{idx}. {keyword}")

    createDirectory(f"./images/{keyword}/")

    url1 = baseUrl + quote_plus(keyword)  # 한글 검색 자동 변환
    url2 = pixabayUrl + quote_plus(keyword) + "/"

    url_list = [url1]  # url2]

    for url in url_list:
        html = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
            },
        )
        html = urlopen(html)
        soup = bs(html, "html.parser")

        if url == url1:
            img = soup.find_all(class_="cover-img wp-post-image")
        else:
            img = soup.find_all(class_="photo-result-image")

        image_num = len(img)

        n = 1
        for i in tqdm(img):
            imgUrl = i["src"]
            imgUrl = Request(
                imgUrl,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
                },
            )
            with urlopen(imgUrl) as f:
                with open(
                    f"./images/{keyword}/img_{n}.jpg", "wb"
                ) as h:  # w - write b - binary
                    img = f.read()
                    h.write(img)
            n += 1
        print(f"{idx}. {keyword} - Total Image Num : {n-1}")

print(f"Image Crawling is done.")

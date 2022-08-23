import glob
import json

# image_file_list = glob.glob('./Crawling/image/*.jpg')
json_file_dir = glob.glob('./Crawling/json/*.json')

for json_file in json_file_dir:
    with open(json_file, 'r') as f:
        json_data = json.load(f)

        images = json_data['images']
        annotations = json_data['annotations']

        for image in images:
            image_id = image['id']
            image_name = image['file_name'].replace(".jpg", "")
            image_width = image['width']
            image_height = image['height']

            file = open("./labels/"+image_name + ".txt", "w")
            for annot in annotations:
                x1, y1, x2, y2 = annot['bbox'] # 객체 1개의 bbox 위치 좌표
                x1 = x1/image_width
                y1 = y1/image_height
                x2 = (x2-x1)/image_width
                y2 = (y2-y1)/image_height

                label = annot['category_id']
                file.write(f"{label} {x1:f} {y1:f} {x2:f} {y2:f}\n")
            file.close()
            
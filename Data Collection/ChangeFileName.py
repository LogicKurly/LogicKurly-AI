import os
import glob
import shutil

from tqdm import tqdm


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

folder_list = glob.glob("../Crawling/images/*")

i = 0
for folder_dir in folder_list:
    file_list = glob.glob(folder_dir + "/*.jpg")

    for file_dir in tqdm(file_list):
        createDirectory('./CrawlingData/')
        shutil.move(file_dir, f"./CrawlingData/crawling_img_{i}.jpg")
        i += 1

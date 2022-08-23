import requests
import os
import json


def send_data(url):
    path_dir = "/home/ec2-user/temp/image"
    file_list = os.listdir(path_dir)

    result = dict()
    for index, name in enumerate(file_list):
        files = {"file": open("/home/ec2-user/temp/image/" + name, "rb")}
        res = requests.post(url, files=files)
        # name = res['name']
        res_json = res.json()
        if res_json["answer"]:
            os.system(
                "mv /home/ec2-user/temp/image/" + name + " /home/ec2-user/temp/result/"
            )
        else:
            os.system("rm -f /home/ec2-user/temp/image" + name)

        result[index] = res_json["answer"]

    result = json.dumps(result)
    print("Done")
    return result


url = "http://localhost:5000/predict"

result_json = send_data(url)

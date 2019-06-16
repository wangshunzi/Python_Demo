import requests

url = "https://pic.qiushibaike.com/system/pictures/12192/121923784/medium/UH29U8HAWB1NVD8T.jpg"
resp = requests.get(url)
image_name = url.split("/")[-1]
with open("images/{}".format(image_name), "wb") as f:
    f.write(resp.content)

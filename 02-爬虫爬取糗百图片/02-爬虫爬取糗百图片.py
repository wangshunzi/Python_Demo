import requests
from lxml import html

url = "https://www.qiushibaike.com/imgrank/"
resp = requests.get(url)
# print(resp.text)

html_content = html.fromstring(resp.text)

image_urls = ["https:" + url for url in html_content.xpath("//div[contains(@class, article)]//div[@class='thumb']/a/img/@src")]
print(image_urls)

#
for url in image_urls:
    resp = requests.get(url)
    image_name = url.split("/")[-1]
    with open("images/{}".format(image_name), "wb") as f:
        f.write(resp.content)


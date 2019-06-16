import requests
from lxml import html

def down_load_image(start_url, page=1):
    if page == 0:
        return
    resp = requests.get(start_url)
    # print(resp.text)

    html_content = html.fromstring(resp.text)

    image_urls = ["https:" + url for url in html_content.xpath("//div[contains(@class, article)]//div[@class='thumb']/a/img/@src")]
    # print(image_urls)

    #
    for url in image_urls:
        resp = requests.get(url)
        image_name = url.split("/")[-1]
        with open("images/{}".format(image_name), "wb") as f:
            f.write(resp.content)

    # 下一页url
    next_url_result = html_content.xpath("//span[@class='next']/parent::a/@href")
    if next_url_result:
        next_url = "https://www.qiushibaike.com" + next_url_result[0]
        page = page - 1
        down_load_image(next_url, page)

down_load_image("https://www.qiushibaike.com/pic/", page=2)
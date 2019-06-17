import requests
from lxml import html
from PIL import Image, ImageDraw, ImageFont


# 处理文本，限宽
def parse_text(text, font_size, limit_width):
    content = list(text)
    step = limit_width // font_size
    current_lenght = step
    while current_lenght < len(content):
        content.insert(current_lenght - 1, "\n")
        current_lenght += step
    return "".join(content)



def compose_image_content(back_image, image, content, save_path):
    # 创建一个背景图片
    back_image = Image.open(back_image)
    back_image = back_image.resize((800, 1200))

    # 创建段子的图片
    new_image = Image.open(image)
    new_image = new_image.resize((600, 800))

    # 绘制
    back_image.paste(new_image, (100, 100))

    # 绘制文字
    draw_image = ImageDraw.Draw(back_image)
    draw_image.multiline_text((100, 920), parse_text(content, 20, 600), fill=128, font=ImageFont.truetype("title_font.ttf", 20), align="left")

    back_image.save(save_path)

    return save_path





def download_joke(start_url, page=1, image_result=[]):
    if page == 0:
        return
    resp = requests.get(start_url)
    html_content = html.fromstring(resp.text)

    divs = html_content.xpath("//div[@id='content-left']/div[contains(@class, article)]")
    for div in divs:
        image_url = "https:" + div.xpath(".//div[@class='thumb']/a/img/@src")[0]
        text_content = div.xpath(".//div[@class='content']//span/text()")[0]
        # print(image_url, text_content)
        # continue
        resp = requests.get(image_url)
        image_name = "images/{}".format(image_url.split("/")[-1])
        with open(image_name, "wb") as f:
            f.write(resp.content)
        # print("正在合成图片...")
        image_result.append(compose_image_content("qiubai_back.jpg",image_name, text_content,image_name))


    # 下一页url
    next_url_result = html_content.xpath("//span[@class='next']/parent::a/@href")
    if next_url_result:
        next_url = "https://www.qiushibaike.com" + next_url_result[0]
        page = page - 1
        download_joke(next_url, page, image_result)



if __name__ == '__main__':
    import itchat

    @itchat.msg_register(itchat.content.TEXT)
    def recieve_msg(msg):
        to_user = msg["ToUserName"]
        if to_user != "filehelper":
            return None

        if msg["Text"].lower() == "joke":
            images = []
            download_joke("https://www.qiushibaike.com/pic/", page=1, image_result=images)
            # print(images)
            for image in images:
                itchat.send_image(image, toUserName="filehelper")
                # itchat.send_msg("xx", toUserName="filehelper")

    itchat.auto_login(hotReload=True)
    itchat.run()

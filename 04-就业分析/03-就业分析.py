import requests

# 经过这么几个步骤，可以保证拿到后续请求的必备cookie
# cookie被保存在了session
session_url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
}
session = requests.Session()
session.get(session_url, headers=headers)


def get_save_jobs(page_num, kd, city="上海"):

    # job_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    job_url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false".format(city)
    data = {
        "first": "true",
        "pn": page_num,
        "kd": kd
    }
    resp = session.post(job_url, data=data, headers=headers)
    # resp.encoding = "utf-8"
    # print(resp.text)

    titles = ["公司名称", "职位名称", "工作年限", "教育程度", "城市", "薪资", "福利", "经度", "纬度", "公司规模", "融资", "地铁线"]
    items = []
    for dic in resp.json()["content"]["positionResult"]["result"]:
        com_name = dic["companyFullName"]
        pos_name = dic["positionName"]
        work_year = dic["workYear"]
        edu = dic["education"]
        city = dic["city"]
        salary = dic["salary"]
        ad = dic["positionAdvantage"]
        lng = dic["longitude"]
        lat = dic["latitude"]
        com_size = dic["companySize"]
        finance_stage = dic["financeStage"]
        line_staion = dic["linestaion"]
        items.append([com_name, pos_name, work_year, edu, city, salary, ad, lng, lat, com_size, finance_stage, line_staion])

    import csv
    import os
    csv_file_path = "jobs.csv"

    # 1. 判断文件是否存在
    # 不存在则创建一个新的文件，并把表头信息填充
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, "w", encoding="gbk", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(titles)

    # 2. 追加新的行内容
    with open(csv_file_path, "a+", encoding="gbk", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(items)

import time
if __name__ == '__main__':
    for i in range(1, 5):
        get_save_jobs(i, "python", "深圳")
        time.sleep(2)

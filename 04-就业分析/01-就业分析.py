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

job_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}

resp = session.post(job_url, data=data, headers=headers)
print(resp.json())
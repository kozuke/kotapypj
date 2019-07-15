import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.yahoo.co.jp/")
url = []

soup = BeautifulSoup(r.content, "html.parser")
css = soup.select("#contentsWrap > section.topics > div > div > div > ul > li")
print(css)

for val in css:
    print(val.text)

yaho = soup.find_all("a")
# aタグの部分の内容を確認
print(yaho)

for script in yaho:
    # "主要"ニュースのタイトルを取ってくるにはどうしたらよい？
    x = script.text
    url.append(x)

line_notify_token = '自分のID'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = url

payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)

import requests
from bs4 import BeautifulSoup

url = "https://www.todayhumor.co.kr/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 전체 목록 가져오기
items = soup.find_all("td", attrs={"class":"subject"})
for item in items:
    print("title:", item.a.get_text())
    print("link:", item.a["href"])
    print("============================")

import re
import requests
from bs4 import BeautifulSoup

url = "https://www.todayhumor.co.kr/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("tr", attrs={"class":re.compile("^view")})
for item in items:
    title = item.find("td", attrs={"class":"subject"}).get_text()
    print(title)

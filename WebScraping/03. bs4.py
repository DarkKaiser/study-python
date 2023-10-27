import requests
from bs4 import BeautifulSoup

url = "https://www.todayhumor.co.kr/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print("Title:", soup.title)
print("Title Text:", soup.title.get_text())
print(soup.a["href"])

print(soup.find("a", attrs={"class":"topmenu_button"}))
print(soup.find(attrs={"class":"topmenu_button"}))

atag = soup.find(attrs={"class":"topmenu_button"})
print(atag.attrs)

lst1 = soup.find("div", attrs={"class":"list list_tr_sisa cf"})
lst2 = lst1.next_sibling.next_sibling
print(lst2.a.get_text())
lst3 = lst2.next_sibling.next_sibling
print(lst3.a.get_text())

print(lst1.parent())

lst2 = lst1.find_next_sibling("div")
print(lst2.a.get_text())

print(lst1.find_next_siblings("div"))

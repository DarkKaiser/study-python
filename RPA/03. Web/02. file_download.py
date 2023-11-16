import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# 크롬에서 다운로드 받는 파일의 경로를 지정
chrome_options.add_experimental_option('prefs', {'download.default_directory':'c:\\temp\\'})

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame("iframeResult")

# download 링크 클릭
elem = browser.find_element(By.XPATH, "/html/body/p[2]/a")
elem.click()

time.sleep(5)
browser.quit()

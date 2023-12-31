import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

###################################################################
# Headless 크롬 띄우기
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")   # 설정된 크기에 맞춰서 내부적으로 브라우저를 띄워서 동작
###################################################################

browser = webdriver.Chrome(options=options)
browser.get("http://www.naver.com")
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW") # 로그인 버튼
elem.click()

browser.back()
# browser.forward()
# browser.refresh()

# 검색 텍스트 입력박스 찾기
# elem = browser.find_element(By.ID, "query")   # 바로 찾기
# ID가 'query'인 엘리멘트가 위치할 때(나타날 때)까지 최대 10초동안 대기하면서 찾는다.
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "query")))

# elem.clear()  # 검색 텍스트 입력박스 내용 삭제
elem.send_keys("파이썬")
elem.send_keys(Keys.ENTER)

elems = browser.find_elements(By.TAG_NAME, "a")
for e in elems:
    print(e.get_attribute("href"))

# HTML 출력
print(browser.page_source)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(5)

# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우져 종료

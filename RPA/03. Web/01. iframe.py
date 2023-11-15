import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# HTML 문서 내부에 있는 IFrame으로 전환
browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

# IFrame에서 다시 상위로 빠져 나옴
browser.switch_to.default_content()

time.sleep(50)

browser.quit()

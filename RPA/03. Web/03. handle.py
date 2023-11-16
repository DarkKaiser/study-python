from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

# Browser 윈도우(탭) 핸들값
curr_handle = browser.current_window_handle
print(curr_handle)

# Browser의 모든 윈도우(탭) 핸들값
handles = browser.window_handles
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # 해당 핸들의 윈도우(탭)를 가리키도록 변경

# 해당 핸들의 윈도우(탭)이 닫힌다.
# 탭이 하나였을 경우에는 Browser 자체가 종료된다.
browser.quit()

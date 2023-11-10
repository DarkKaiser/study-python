import sys
import time
import pyautogui

# 화면상에서 '파일' 메뉴의 위치를 찾아서 클릭한다.
# file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png")
# if file_menu == None:
#     print("찾지를 못하였습니다.")
# else:
#     print(file_menu)
#     pyautogui.click(file_menu)

# 화면상에 존재하는 모든 '파일' 메뉴의 위치를 찾아서 클릭한다.
# for i in pyautogui.locateAllOnScreen("RPA/02. Desktop/file_menu.png"):
#     pyautogui.click(i)

###########################
# 인식 속도개선
###########################
# 1. GrayScale
# file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png", grayscale=True)
# print(file_menu)
# pyautogui.click(file_menu)

# 2. 범위지정
# file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png", region=(0, 0, 200, 100))
# print(file_menu)
# pyautogui.click(file_menu)

# 3. 정확도 조정
# file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png", confidence=0.7) # 70%
# print(file_menu)
# pyautogui.click(file_menu)

###########################
# 자동화 대상이 바로 보여지지 않는 경우
###########################
# 1. 계속 기다리기
# file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png")
# while file_menu is None:
#     file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# 2. 일정 시간동안 기다리기(Timeout)
timeout = 10 # 10초 대기
start = time.time() # 시작시간 설정
file_menu = None
while file_menu is None:
    file_menu = pyautogui.locateOnScreen("RPA/02. Desktop/file_menu.png")
    end = time.time() # 종료시간 설정
    if end - start > timeout:
        print("시간 종료")
        sys.exit()

print(file_menu)
pyautogui.click(file_menu)

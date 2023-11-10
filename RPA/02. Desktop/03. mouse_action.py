import pyautogui

#################
# 클릭
#################
pyautogui.click(100, 100, duration=1) # 1초동안 (100, 100) 좌표로 이동후에 마우스 클릭

# 좌표 정보를 넣지 않으면 현재 마우스가 위치한 곳에서 마우스 클릭
pyautogui.click() # pyautogui.mouseDown() + pyautogui.mouseUp()

pyautogui.doubleClick() # = pyautogui.click(clicks=2)

# pyautogui.rightClick() 마우스 우측버튼 클릭
# pyautogui.middleClick() 마우스 휠 클릭

#################
# 드래그
#################
pyautogui.moveTo(500, 500)
pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100만큼, y 0만큼 드래그

#################
# 스크롤
#################
pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤

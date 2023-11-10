import pyautogui

# 절대 좌표로 마우스 이동
pyautogui.moveTo(100, 100) # 지정한 위치로 마우스 이동
pyautogui.moveTo(100, 200, duration=0.25) # 0.25초 동안 100, 200 위치로 마우스 이동

# 상대 좌료로 마우스 이동
pyautogui.move(100, 100)
print(pyautogui.position()) # 현재 마우스 좌표 출력

p = pyautogui.position()
print("x:", p[0], "y:", p[1])
print("x:", p.x, "y:", p.y)

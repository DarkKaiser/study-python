import pyautogui

# 스크린샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png")

# 지정된 좌표의 픽셀 정보 얻기
pixel = pyautogui.pixel(28, 18)
print(pixel)

# 지정된 좌표의 픽셀 정보가 주어진 픽셀과 일치하는지 확인
print(pyautogui.pixelMatchesColor(28, 18, pixel))

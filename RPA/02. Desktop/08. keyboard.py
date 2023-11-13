import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive == False:
    w.activate()

pyautogui.write("12345")
pyautogui.write("abcdefg", interval=0.25)
pyautogui.write("한글") # 한글은 입력되지 않음, pyperclip을 이용해서 클립보드로 복사하는 방식으로 사용 가능

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"])

# 특수문자
pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# 조합키(Hot Key)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")

# 간편한 조합키
pyautogui.hotkey("ctrl", "a")

# pyperclip을 이용한 한글입력
pyperclip.copy("한글")
pyautogui.hotkey("ctrl", "v")

import pyautogui

fw = pyautogui.getActiveWindow()
print(fw.title)
print(fw.size)
print(fw.left, fw.top, fw.right, fw.bottom)

# 모든 윈도우 가져오기
for w in pyautogui.getAllWindows():
    print(w)

# 특정 제목을 가진 모든 윈도우 가져오기
for w in pyautogui.getWindowsWithTitle("제목 없음"):
    print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive == False:
    w.activate()

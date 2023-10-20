from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")  # 너비 x 높이 + x좌표 + y좌표

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)

root.mainloop()

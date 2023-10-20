from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

chkvar = IntVar()   # chkvar에 int 형으로 값을 저장한다.
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# checkbox.select()   # 자동선택처리
# checkbox.deselect() # 선택해제처리
checkbox.pack()

def btnCmd():
    print(chkvar.get()) # 0 : 체크해제, 1 : 체크

btn = Button(root, text="클릭", command=btnCmd)
btn.pack()

root.mainloop()

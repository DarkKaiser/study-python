import time
from tkinter import *
import tkinter.ttk as ttk

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

progressbar1 = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar1.start(10)   # 10ms마다 움직임
progressbar1.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(10)   # 10ms마다 움직임
progressbar2.pack()

def btnCmd():
    progressbar1.stop()
    progressbar2.stop()

btn = Button(root, text="중지", command=btnCmd)
btn.pack()

#############################

p_var = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar3.pack()

def btnCmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기
        
        p_var.set(i)
        progressbar3.update()

btn2 = Button(root, text="시작", command=btnCmd2)
btn2.pack()

root.mainloop()

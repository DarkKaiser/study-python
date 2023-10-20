from tkinter import *

def btnCmd():
    print("버튼이 클릭되었습니다.")

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

btn1 = Button(root, text="버튼1", padx=10, pady=20)
btn1.pack()

btn2 = Button(root, text="버튼2", width=10, height=3)
btn2.pack()

btn3 = Button(root, text="버튼3", fg="red", bg="yellow")
btn3.pack()

photo = PhotoImage(file="Basic_GUI/img.png")
btn4 = Button(root, image=photo)
btn4.pack()

btn5 = Button(root, text="동작하는 버튼", command=btnCmd)
btn5.pack()

root.mainloop()

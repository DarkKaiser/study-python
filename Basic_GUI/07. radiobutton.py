from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.select()

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

def btnCmd():
    print(burger_var.get())

btn = Button(root, text="주문", command=btnCmd)
btn.pack()

root.mainloop()

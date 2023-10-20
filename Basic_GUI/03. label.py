from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="Basic_GUI/img.png")
label2 = Label(root, image=photo)
label2.pack()

def onChange():
    label1.config(text="또 만나요")
    
    global photo2
    photo2 = PhotoImage(file="Basic_GUI/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=onChange)
btn.pack()

root.mainloop()

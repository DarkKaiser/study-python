from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

listbox = Listbox(root, selectmode="extended", height=3)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btnCmd():
    # 삭제
    listbox.delete(0)   # 맨 앞에 항목 삭제
    listbox.delete(END) # 맨 뒤에 항목 삭제
    
    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요")
    
    # 항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
    
    # 선택된 항목 확인(위치로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btnCmd)
btn.pack()

root.mainloop()

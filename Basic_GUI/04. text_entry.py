from tkinter import *

root = Tk()

root.title("제목")
root.geometry("640x480+10+10")

# 여러줄
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 한 줄 텍스트
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btnCmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1.0 : 1번째 라인의 컬럼 0번째에서부터 가져와라는 의미
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btnCmd)
btn.pack()

root.mainloop()

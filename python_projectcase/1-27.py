from tkinter import *


# 定义的函数监听事件
def printkey(event):
    print("你按下了：" + event.char)


root = Tk()
# 实例化单行输入框
entry = Entry(root)
# 给输入框绑定按键监听事件<KeyPress>为监听任何按键
entry.bind("<KeyPress>", printkey)
entry.pack()
root.mainloop()

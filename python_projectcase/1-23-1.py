from tkinter import *

colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
root = Tk()
f = Frame(root, height=200, width=200)
f.color = 0
# 设置框架背景色
f['bg'] = colors[f.color]
lab1 = Label(f, text="0")
lab1.pack()


def foo():
    f.color = (f.color + 1) % len(colors)
    lab1['bg'] = colors[f.color]
    lab1['text'] = str(int(lab1['text']) + 1)
    # 隔500ms执行foo()函数刷新屏幕
    f.after(500, foo)


f.pack()
f.after(500, foo)
root.mainloop()

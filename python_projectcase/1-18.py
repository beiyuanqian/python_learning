from tkinter import *

win = Tk()
win.title("我的窗口")
lab1 = Label(win, text='你好', anchor="nw")
# 显示label组件
lab1.pack()
# 显示内置的位图，创建显示疑问图标Label组件
lab2 = Label(win, bitmap="question")
lab2.pack()
# 显示自选的图片
bm = PhotoImage(file=r"E:\GTSCbug列表\微信图片_20210916200213.png")
lab3 = Label(win, image=bm)
lab3.bm = bm
lab3.pack()

win.mainloop()

from tkinter import *

root = Tk()


def printRect(event):
    print("rectangle左键事件")


def printRect2(event):
    print("rectangle右键事件")


def printLine(event):
    print("Line事件")


# 创建一个Canvas,设置其背景色为白色
cv = Canvas(root, bg='white')
rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags="r1")
# 绑定item与鼠标左键事件
cv.tag_bind("r1", "<Button-1>", printRect)
# 绑定item与鼠标右键事件
cv.tag_bind("r1", "<Button-3>", printRect2)
# 创建一个line,并将其tags设置为r2
cv.create_line(180, 70, 280, 70, width=10, tags="r2")
# 绑定item与鼠标左键事件
cv.tag_bind("r2", '<Button-1>', printLine)
cv.pack()
root.mainloop()

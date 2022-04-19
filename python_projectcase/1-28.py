from tkinter import *


# 定义的函数监听事件
def leftClick(event):
    print("x轴坐标：", event.x)
    print("y轴坐标：", event.y)
    print("相当于屏幕左上角x轴坐标：", event.x_root)
    print("相当于屏幕左上角y轴坐标：", event.y_root)


root = Tk()
lab = Label(root, text="hello")
lab.pack()
# 给label绑定鼠标监听事件
lab.bind("<Button-1>", leftClick)
root.mainloop()

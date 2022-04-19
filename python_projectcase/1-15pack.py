import tkinter

# 创建Windows窗口对象
root = tkinter.Tk()
# 设置Windows窗口大小
root.geometry("400x300")

label = tkinter.Label(root, text="Hello,python")
# 将Label组件添加到窗口中显示
label.pack()
# 创建文字是“BUTTON1”的Button组件
button1 = tkinter.Button(root, text="BUTTON1")
# 将button1组件添加到窗口中显示，左停靠
button1.pack(side=tkinter.LEFT)
# 创建文字是“BUTTON2”的Button组件
button2 = tkinter.Button(root, text="BUTTON2")
# 将button2组件添加到窗口中显示，左停靠
button2.pack(side=tkinter.RIGHT)

root.mainloop()

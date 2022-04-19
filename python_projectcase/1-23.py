from tkinter import *

root = Tk()
root.title("使用Frame组件的例子")
# 创建第一个frame组件
f1 = Frame(root)
f1.pack()
# 创建第二个frame组件
f2 = Frame(root)
f2.pack()
# 创建第三个frame组件，放置在窗口底部
f3 = LabelFrame(root, text="第3个Frame")
f3.pack(side=BOTTOM)

redbutton = Button(f1, text="Red", fg="red")
redbutton.pack(side=LEFT)
brownbutton = Button(f1, text="Brown", fg="brown")
brownbutton.pack(side=LEFT)
bluebutton = Button(f1, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)
blackbutton = Button(f2, text="Black", fg="black")
blackbutton.pack()
greenbutton = Button(f3, text="Green", fg="green")
greenbutton.pack()
root.mainloop()

import tkinter

root = tkinter.Tk()
# 创建StringVar对象
r = tkinter.StringVar()
# 设置初始值为1，初始选中中国
r.set("1")
radio = tkinter.Radiobutton(root, variable=r, value="1", text="中国")
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value="2", text="美国")
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value="3", text="日本")
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value="4", text="加拿大")
radio.pack()
radio = tkinter.Radiobutton(root, variable=r, value="5", text="韩国")
radio.pack()
root.mainloop()
print(r.get())


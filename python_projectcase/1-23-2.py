from tkinter import *

root = Tk()
f = Frame(root, height=200, width=200)
lab1 = Label(f, text="欢迎参观")
x = 0


def foo():
    global x
    x = x + 10
    if x > 200:
        x = 0
    lab1.place(x=x, y=0)
    f.after(500, foo)


f.pack()
foo()
# f.after(500, foo)
root.mainloop()

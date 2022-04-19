import sqlite3

conn = sqlite3.connect("test2.db")
cursor = conn.cursor()
# 执行查询语句
cursor.execute("select * from exam")
# 获取查询结果集
values = cursor.fetchall()
cursor.close()
conn.close()

import tkinter
from tkinter import *
from tkinter.messagebox import *


def callNext():
    global k
    global score
    k = k + 1
    # 判断用户是否做完
    if k >= len(values):
        showinfo("提示", "题目做完了")
        return
    # 获取用户的选择
    useranswer = r.get()
    # 获取被选中单选按钮变量值
    print(r.get())
    if useranswer == values[k][5]:
        showinfo("恭喜", "恭喜你答对了！")
        score += 10
    else:
        showinfo("遗憾", "遗憾你答错了！")
    # 显示下一题
    # 题目信息
    timu['text'] = values[k][0]
    # A选项
    radio1['text'] = values[k][1]
    # B选项
    radio2['text'] = values[k][2]
    # C选项
    radio3['text'] = values[k][3]
    # D选项
    radio4['text'] = values[k][4]
    r.set("E")


def callResult():
    showinfo("你的得分", str(score))


root = tkinter.Tk()
root.title("Python智力问答游戏")
root.geometry("500x200")
# 创建StringVar对象
r = tkinter.StringVar()
# 设置初始值为”E"，初始没选中
r.set("E")
k = 0
score = 0
# 题目
timu = tkinter.Label(root, text=values[k][0])
timu.pack()
# 创建第一个Frame组件
f1 = Frame(root)
f1.pack()
radio1 = tkinter.Radiobutton(f1, variable=r, value="A", text=values[k][1])
radio1.pack()
radio2 = tkinter.Radiobutton(f1, variable=r, value="B", text=values[k][2])
radio2.pack()
radio3 = tkinter.Radiobutton(f1, variable=r, value="C", text=values[k][3])
radio3.pack()
radio4 = tkinter.Radiobutton(f1, variable=r, value="D", text=values[k][4])
radio4.pack()
# 创建第二个Frame组件
f2 = Frame(root)
f2.pack()
Button(f2, text="下一题", command=callNext).pack(side=LEFT)
Button(f2, text="结果", command=callResult).pack(side=LEFT)
root.mainloop()

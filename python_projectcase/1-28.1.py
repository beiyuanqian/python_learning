import tkinter as tk
import random

# 玩家要猜的数字
number = random.randint(0, 1024)
running = True
# 猜的次数
num = 0
# 提示猜测范围的最大数
nmaxn = 1024
# 提示猜测范围的最小数
nminn = 0


# "关闭"按钮事件函数
def eBtnClose(event):
    root.destroy()


# "猜"按钮事件函数
def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        # 获取猜的数字并转化为数字
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval("恭喜答对了！")
            num += 1
            running = False
            numGuess()
        elif val_a < number:
            # 猜小了
            if val_a > nminn:
                # 修改提示猜测范围的最小数
                nminn = val_a
                num += 1
                labelqval("小了哦，请输入" + str(nminn) + "到" + str(nmaxn) + "之间任意整数：")
        else:
            if val_a < nmaxn:
                # 修改提示猜测范围的最大数
                nmaxn = val_a
                num += 1
                labelqval("大了哦，请输入" + str(nminn) + "到" + str(nmaxn) + "之间任意整数：")
    else:
        labelqval("你已经答对啦。。。")


def numGuess():
    if num == 1:
        labelqval("一次答对！")
    elif num < 10:
        labelqval("==十次以内就答对了牛。。。  尝试次数：" + str(num))
    else:
        labelqval("好吧，您都试了超过10v次了。。。  尝试次数：" + str(num))


def labelqval(vText):
    # 修改提示标签文字
    label_val_q.config(label_val_q, text=vText)


root = tk.Tk()
root.geometry("400x90+200+200")
label_val_q = tk.Label(root, width="80")
label_val_q.pack(side="top")

# 单行输入文本框
entry_a = tk.Entry(root, width="40")
# "猜"按钮
btnGuess = tk.Button(root, text="猜")
entry_a.pack(side="left")
# 绑定事件
entry_a.bind("<Return>", eBtnGuess)
btnGuess.bind("<Button-1>", eBtnGuess)
btnGuess.pack(side="left")
# ”关闭按钮“
btnClose = tk.Button(root, text="关闭")
btnClose.bind("<Button->", eBtnClose)
btnClose.pack(side="left")
labelqval("请输入0到1024之间的任意整数：")
entry_a.focus_set()
print(number)
root.mainloop()

from tkinter import *

root = Tk()


def hello():
    print("你单击主菜单")


m = Menu(root)
for item in ['文件', '编辑', '视图']:
    # 添加菜单项
    m.add_command(label=item, command=hello)
# 附加主菜单到窗口
root['menu'] = m
root.mainloop()

# 导入Tkinter模块
import tkinter

# 创建Windows窗口对象
win = tkinter.Tk()
# 设置Windows窗口大小
win.geometry("800x600")
# # 窗口大小不可变
# win.resizable(False, False)
# 设置窗口的最小尺寸
win.minsize(400, 600)
# 设置窗口的最大尺寸
win.maxsize(1440, 800)
# 设置窗口标题
win.title("我的第一个GUI程序")
# 进入消息循环，也就是显示窗口
win.mainloop()

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/12}

"""
import os

# 相当于打开操作系统的shell，敲入一串命令
# 阻塞式调用：调用的外部程序没有退出时，python程序会一直停留在这里，直到调用的外部程序退出，代码才接着往下运行
# os.system("dir")
# os.system("ipconfig")
# os.system("mspaint")
# print("after")
ret = os.system("for %i in (1,2,10) do @echo %i")
print("ret = ", ret)
"""

"""
import subprocess

# 执行一个指定的命令，并将结果以字节字符串的形式返回
# out = subprocess.check_output("ipconfig")
# print(out.decode("gbk"))
# 阻塞式调用
# out = subprocess.check_output("mspaint")
# print("执行结果", out.decode("gbk"))
child = subprocess.Popen("ipconfig")
child = subprocess.Popen(
    "ipconfig",
    stdout=subprocess.PIPE,
)
output, err = child.communicate()
print(output)
"""

"""
from subprocess import Popen, PIPE

# 输出重定向
child = Popen("ipconfig")
child = Popen(
    "ipconfig",
    stdout=PIPE,
)
output, err = child.communicate()
print(output)
"""

from subprocess import Popen, PIPE
# 输入重定向
child = Popen(
    "python 2.py",
    stdin=PIPE,
    encoding="gbk"  # 不加会报错
)

output, err = child.communicate("1\n2\n")
print(output)

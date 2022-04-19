# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/30}

import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()
# 连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 远程主机ip地址、端口号，再远程主机已经存在的用户名和密码
ssh.connect("192.168.2.149", 22, "songqin", "songqin")
# 执行命令，并获取命令执行结果
# stdin, stdout, stderr = ssh.exec_command("cd Desktop;ls")
# print(stdout.read().decode("utf8"))
# stdin, stdout, stderr = ssh.exec_command("pwd")
# print(stdout.read().decode("utf8"))

sftp = ssh.open_sftp()
# 将本地文件传送到远程机器,第一个参数为本地文件路径，第二个参数为远程文件路径
sftp.put(r"D:\PYproject\test\pythonAdvanced\day1\1.png", "/home/songqin/Desktop/1.png")
# 将远程机器文件下载到本地，第一个参数是远程文件路径，第二个参数是本地路径
sftp.get("/home/songqin/Desktop/2.png", r"D:\PYproject\test\pythonAdvanced\day5\2.png")

ssh .close()

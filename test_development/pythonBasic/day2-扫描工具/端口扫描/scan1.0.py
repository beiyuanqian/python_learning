# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/15}

# ——————————1.0版本扫描单个端口——————————————
import socket


def scan_tool(ip, port):
    # 建立TCP连接
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置超时时间
    TCP_sock.settimeout(1)
    # 查看连接返回,如果为0即返回成功
    try:
        conn = TCP_sock.connect_ex((ip, port))  # 会有返回值(ip,port),port是一个int
        if conn == 0:
            print(f'服务器：{ip},端口:{port}---开放成功')
        else:
            print(f'服务器：{ip},端口:{port}---未开放')
    except:
        print('扫描异常')


if __name__ == '__main__':
    ip = input('请输入需要扫描的服务器ip>>>')
    port = int(input('请输入需要扫描的端口>>>').strip())
    scan_tool(ip, port)

"""
用户反馈：
1、1.0版本不能实现扫描多个端口
2、1.0版本不能实现有些服务不是ip形式，是域名的形式
"""

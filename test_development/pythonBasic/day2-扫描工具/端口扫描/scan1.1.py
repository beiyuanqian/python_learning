# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/15}

# ——————————1.1版本扫描单个端口——————————————
"""
1、解决1.0版本不能实现扫描多个端口
2、解决1.0版本有些服务不是ip形式，是域名的形式
"""

import socket
import re
import time


# 1-校验ip,正则网站http://c.runoob.com/front-end/854
def check_ip(ip):
    # 正则判断IP是否正确
    ip_address = re.compile("((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}")
    if ip_address.match(ip) and len(ip) >= 0:
        return True
    else:
        return False


# 2-校验域名
def check_domainName(domain):
    # 正则判断域名是否正确
    dm = re.compile("[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?")
    if dm.match(domain):
        return True
    else:
        return False


# 3-端口扫描
def scan_tool(ip, port):
    startPort, endPort = port.split(',')
    # 开始计时
    start_time = time.time()
    for one in range(int(startPort), int(endPort) + 1):
        # 建立TCP连接
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间
        TCP_sock.settimeout(1)
        # 查看连接返回,如果为0即返回成功
        try:
            conn = TCP_sock.connect_ex((ip, one))  # 会有返回值(ip,port),port是一个int
            if conn == 0:
                print(f'服务器：{ip},端口:{one}---开放成功')
            else:
                pass
                # print(f'服务器：{ip},端口:{one}---未开放')
        except:
            print('扫描异常！')
        # 关闭连接
        TCP_sock.close()
        # 结束计时
    end_time = time.time()
    print('扫描过程耗时：', end_time - start_time)


# 4、域名扫描
def domain_scan(domain):
    # 获取域名的ip
    server_ip = socket.gethostbyname(domain)
    print(f'该域名：{domain}，对应的ip：{server_ip}')
    return server_ip


if __name__ == '__main__':
    info = input('请输入需要扫描的服务器ip或者域名>>>')
    port = input('请输入需要扫描的端口是xxx,xxxx格式>>>').strip()
    if check_ip(info):
        scan_tool(info, port)
    elif check_domainName(info):
        scan_tool(domain_scan(info), port)
    else:
        print('输入有误')

"""
用户反馈：
1、扫描功能实现，但是扫描较慢
"""

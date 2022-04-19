# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/17}

"""
需求：
1、把端口输出并统计开放端口个数
"""

import socket
import re
import time
import threading


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


# 3-端口扫描--线程扫描函数
def scan_tool(ip, port, portlist=[]):
    # 建立TCP连接
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置超时时间
    TCP_sock.settimeout(1)
    # 查看连接返回,如果为0即返回成功
    try:
        conn = TCP_sock.connect_ex((ip, port))  # 会有返回值(ip,port),port是一个int
        if conn == 0:
            print(f'服务器：{ip},端口:{port}---开放成功')
            # 增加开放端口到列表
            portlist.append(port)
        else:
            pass
            # print(f'服务器：{ip},端口:{one}---未开放')
    except:
        print('扫描异常！')
    # 关闭连接
    TCP_sock.close()


# 多线程函数封装
def threads_scan(ip, ports='0,65535', portlist=[]):
    # 存放线程对象
    threadList = []

    # 开始计时
    start_time = time.time()
    startPort, endPort = ports.split(',')
    # 创建线程
    for one in range(int(startPort), int(endPort) + 1):
        t = threading.Thread(target=scan_tool, args=(ip, one, portlist))
        threadList.append(t)
    # 启动线程
    for one in threadList:
        one.start()
    # 阻塞
    for one in threadList:
        one.join()
    # 结束计时
    end_time = time.time()
    print('扫描过程耗时：', end_time - start_time)
    print('开放端口是>>>', portlist)
    print('开放端口数是>>>', len(portlist))
    # fo = export_data()
    for one in portlist:
        info = f'服务器的ip:{ip},端口{one}已开放！'
        export_data(info)
    #     fo.write(info+'\n')
    # fo.write(f'扫描过程耗时：{end_time - start_time}s')
    # fo.close()


# 4、域名扫描
def domain_scan(domain):
    # 获取域名的ip
    server_ip = socket.gethostbyname(domain)
    print(f'该域名：{domain}，对应的ip：{server_ip}')
    return server_ip


# 输出文件
def export_data(info):
    with open(r'/模块一：python基础/day3-优化\端口扫描\port.txt', 'a') as fo:
        fo.write(info + '\n')
    # 此方法不传info参数
    # fo = open(r'D:\PYproject\测试开发\模块一：python基础\day3-优化\端口扫描\port.txt', 'a')
    # return fo


if __name__ == '__main__':
    info = input('请输入需要扫描的服务器ip或者域名>>>')
    port = input('请输入需要扫描的端口是xxx,xxxx格式>>>').strip()

    if check_ip(info):
        threads_scan(info, port)
    elif check_domainName(info):
        threads_scan(domain_scan(info), port)
    else:
        print('输入有误')

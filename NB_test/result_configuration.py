# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

# 提取设备信息，统计设备个数，此方法适用于提供的txt文件只包含imei码
equipment = []
file1 = r'F:\测试项目\门锁\NB并发测试IMEI_7.14.txt'
with open(file1) as file1:
    lines = file1.readlines()
    for line in lines:
        a = line.replace('\n', '')
        equipment.append(a)
    print('设备信息', equipment)
    print('设备总个数：', len(equipment))

# 选取时间段
StartDatatime = '2021-07-14 00:00:00.000'
EndDatatime = '2021-07-15 00:00:00.000'

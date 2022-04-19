# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
# path = r'F:\刘小涵\测试项目\门锁\7-14数据\7-14日志\\'
# log.catalogue(path)
a = ['07-14.0', '07-14.1', '07-14.2', '07-14.3', '07-14.4', '07-14.5', '07-14.6', '07-14.7', '07-14.8', '07-14.9',
     '07-14.10', '07-14.11', '07-14.12', '07-14.13', '07-14.14', '07-14.15', '07-14.16', '07-14.17', '07-14.18',
     '07-14.19', '07-14.20', '07-14.21', '07-14.22', '07-14.23', '07-14.24', '07-14.25', '07-14.26', '07-14.27',
     '07-14.28', '07-14.29', '07-14.30', '07-14.31', '07-14.32', '07-14.33', '07-14.34', '07-14.35', ]

for i in range(0, len(a)):
    for line in open(r'F:\测试项目\门锁\7-14数据\7-14日志\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel(r"F:/测试项目/门锁/7-14数据/7-14日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\测试项目\门锁\7-14数据\7-14日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/测试项目/门锁/7-14数据/7-14日志上报数据.xlsx", index=False)

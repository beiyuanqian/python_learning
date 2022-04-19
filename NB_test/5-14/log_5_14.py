# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-14数据\5-14日志\\'
log.catalogue(path)
a = ['05-14.0', '05-14.1', '05-14.2', '05-14.3', '05-14.4', '05-14.5', '05-14.6', '05-14.7', '05-14.8', '05-14.9',
     '05-14.10', '05-14.11', '05-14.12', '05-14.13', '05-14.14', '05-14.15', '05-14.16', '05-14.17', '05-14.18',
     '05-14.19', '05-14.20', '05-14.21', '05-14.22', '05-14.23', '05-14.24', '05-14.25', '05-14.26', '05-14.27',
     '05-14.28', '05-14.29', '05-14.30', '05-14.31', '05-14.32', '05-14.33', '05-14.34', '05-14.35', '05-14.36',
     '05-14.37', '05-14.38', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-14数据\5-14日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-14数据/5-14日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-14数据\5-14日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)

# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)

df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-14数据/5-14日志上报数据.xlsx", index=False)

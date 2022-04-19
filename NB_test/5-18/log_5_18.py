# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-18数据\5-18日志\\'
log.catalogue(path)
a = ['05-18.0', '05-18.1', '05-18.2', '05-18.3', '05-18.4', '05-18.5', '05-18.6', '05-18.7', '05-18.8', '05-18.9',
     '05-18.10', '05-18.11', '05-18.12', '05-18.13', '05-18.14', '05-18.15', '05-18.16', '05-18.17', '05-18.18',
     '05-18.19', '05-18.20', '05-18.21', '05-18.22', '05-18.23', '05-18.24', '05-18.25', '05-18.26', '05-18.27',
     '05-18.28', '05-18.29', '05-18.30', '05-18.31', '05-18.32', '05-18.33', '05-18.34', '05-18.35', '05-18.36',
     '05-18.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-18数据\5-18日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-18数据/5-18日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-18数据\5-18日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-18数据/5-18日志上报数据.xlsx", index=False)

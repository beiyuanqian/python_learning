# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-19数据\5-19日志\\'
log.catalogue(path)
a = ['05-19.0', '05-19.1', '05-19.2', '05-19.3', '05-19.4', '05-19.5', '05-19.6', '05-19.7', '05-19.8', '05-19.9',
     '05-19.10', '05-19.11', '05-19.12', '05-19.13', '05-19.14', '05-19.15', '05-19.16', '05-19.17', '05-19.18',
     '05-19.19', '05-19.20', '05-19.21', '05-19.22', '05-19.23', '05-19.24', '05-19.25', '05-19.26', '05-19.27',
     '05-19.28', '05-19.29', '05-19.30', '05-19.31', '05-19.32', '05-19.33', '05-19.34', '05-19.35', '05-19.36',
     '05-19.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-19数据\5-19日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-19数据/5-19日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-19数据\5-19日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-19数据/5-19日志上报数据.xlsx", index=False)

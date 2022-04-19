# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-17数据\5-17日志\\'
log.catalogue(path)
a = ['05-17.0', '05-17.1', '05-17.2', '05-17.3', '05-17.4', '05-17.5', '05-17.6', '05-17.7', '05-17.8', '05-17.9',
     '05-17.10', '05-17.11', '05-17.12', '05-17.13', '05-17.14', '05-17.15', '05-17.16', '05-17.17', '05-17.18',
     '05-17.19', '05-17.20', '05-17.21', '05-17.22', '05-17.23', '05-17.24', '05-17.25', '05-17.26', '05-17.27',
     '05-17.28', '05-17.29', '05-17.30', '05-17.31', '05-17.32', '05-17.33', '05-17.34', '05-17.35', '05-17.36',
     '05-17.37', '05-17.38',]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-17数据\5-17日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-17数据/5-17日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-17数据\5-17日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-17数据/5-17日志上报数据.xlsx", index=False)

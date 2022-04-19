# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-23数据\5-23日志\\'
log.catalogue(path)
a = ['05-23.0', '05-23.1', '05-23.2', '05-23.3', '05-23.4', '05-23.5', '05-23.6', '05-23.7', '05-23.8', '05-23.9',
     '05-23.10', '05-23.11', '05-23.12', '05-23.13', '05-23.14', '05-23.15', '05-23.16', '05-23.17', '05-23.18',
     '05-23.19', '05-23.20', '05-23.21', '05-23.22', '05-23.23', '05-23.24', '05-23.25', '05-23.26', '05-23.27',
     '05-23.28', '05-23.29', '05-23.30', '05-23.31', '05-23.32', '05-23.33', '05-23.34', '05-23.35', '05-23.36',
     '05-23.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-23数据\5-23日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-23数据/5-23日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-23数据\5-23日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-23数据/5-23日志上报数据.xlsx", index=False)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-8数据\5-8日志\\'
log.catalogue(path)
a = ['05-08.0', '05-08.1', '05-08.2', '05-08.3', '05-08.4', '05-08.5', '05-08.6', '05-08.7', '05-08.8', '05-08.9',
     '05-08.10', '05-08.11', '05-08.12', '05-08.13', '05-08.14', '05-08.15', '05-08.16', '05-08.17', '05-08.18',
     '05-08.19', '05-08.20', '05-08.21', '05-08.22', '05-08.23', '05-08.24', '05-08.25', '05-08.26', '05-08.27',
     '05-08.28', '05-08.29', '05-08.30', '05-08.31', '05-08.32', '05-08.33', '05-08.34', '05-08.35', '05-08.36',
     '05-08.37']

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-8数据\5-8日志\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-8数据/5-8日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-8数据\5-8日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-8数据/5-8日志上报数据.xlsx", index=False)

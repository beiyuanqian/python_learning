# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-12数据\5-12日志\\'
log.catalogue(path)
a = ['05-12.0', '05-12.1', '05-12.2', '05-12.3', '05-12.4', '05-12.5', '05-12.6', '05-12.7', '05-12.8', '05-12.9',
     '05-12.10', '05-12.11', '05-12.12', '05-12.13', '05-12.14', '05-12.15', '05-12.16', '05-12.17', '05-12.18',
     '05-12.19', '05-12.20', '05-12.21', '05-12.22', '05-12.23', '05-12.24', '05-12.25', '05-12.26', '05-12.27',
     '05-12.28', '05-12.29', '05-12.30', '05-12.31', '05-12.32', '05-12.33', '05-12.34', '05-12.35', '05-12.36',
     '05-12.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-12数据\5-12日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-12数据/5-12日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-12数据\5-12日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-12数据/5-12日志上报数据.xlsx", index=False)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-10数据\5-10日志\\'
log.catalogue(path)
a = ['05-10.0', '05-10.1', '05-10.2', '05-10.3', '05-10.4', '05-10.5', '05-10.6', '05-10.7', '05-10.8', '05-10.9',
     '05-10.10', '05-10.11', '05-10.12', '05-10.13', '05-10.14', '05-10.15', '05-10.16', '05-10.17', '05-10.18',
     '05-10.19', '05-10.20', '05-10.21', '05-10.22', '05-10.23', '05-10.24', '05-10.25', '05-10.26', '05-10.27',
     '05-10.28', '05-10.29', '05-10.30', '05-10.31', '05-10.32', '05-10.33', '05-10.34', '05-10.35', '05-10.36',
     '05-10.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-10数据\5-10日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-10数据/5-10日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-10数据\5-10日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-10数据/5-10日志上报数据.xlsx", index=False)

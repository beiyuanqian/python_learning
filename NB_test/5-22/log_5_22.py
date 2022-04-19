# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-22数据\5-22日志\\'
log.catalogue(path)
a = ['05-22.0', '05-22.1', '05-22.2', '05-22.3', '05-22.4', '05-22.5', '05-22.6', '05-22.7', '05-22.8', '05-22.9',
     '05-22.10', '05-22.11', '05-22.12', '05-22.13', '05-22.14', '05-22.15', '05-22.16', '05-22.17', '05-22.18',
     '05-22.19', '05-22.20', '05-22.21', '05-22.22', '05-22.23', '05-22.24', '05-22.25', '05-22.26', '05-22.27',
     '05-22.28', '05-22.29', '05-22.30', '05-22.31', '05-22.32', '05-22.33', '05-22.34', '05-22.35', '05-22.36',
     '05-22.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-22数据\5-22日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-22数据/5-22日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-22数据\5-22日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-22数据/5-22日志上报数据.xlsx", index=False)

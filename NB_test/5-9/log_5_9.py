# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-9数据\5-9日志\\'
log.catalogue(path)
a = ['05-09.0', '05-09.1', '05-09.2', '05-09.3', '05-09.4', '05-09.5', '05-09.6', '05-09.7', '05-09.8', '05-09.9',
     '05-09.10', '05-09.11', '05-09.12', '05-09.13', '05-09.14', '05-09.15', '05-09.16', '05-09.17', '05-09.18',
     '05-09.19', '05-09.20', '05-09.21', '05-09.22', '05-09.23', '05-09.24', '05-09.25', '05-09.26', '05-09.27',
     '05-09.28', '05-09.29', '05-09.30', '05-09.31', '05-09.32', '05-09.33', '05-09.34', '05-09.35', '05-09.36',
     '05-09.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-9数据\5-9日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-9数据/5-9日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-9数据\5-9日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-9数据/5-9日志上报数据.xlsx", index=False)

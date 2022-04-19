# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-21数据\5-21日志\\'
log.catalogue(path)
a = ['05-21.0', '05-21.1', '05-21.2', '05-21.3', '05-21.4', '05-21.5', '05-21.6', '05-21.7', '05-21.8', '05-21.9',
     '05-21.10', '05-21.11', '05-21.12', '05-21.13', '05-21.14', '05-21.15', '05-21.16', '05-21.17', '05-21.18',
     '05-21.19', '05-21.20', '05-21.21', '05-21.22', '05-21.23', '05-21.24', '05-21.25', '05-21.26', '05-21.27',
     '05-21.28', '05-21.29', '05-21.30', '05-21.31', '05-21.32', '05-21.33', '05-21.34', '05-21.35', '05-21.36',
     '05-21.37', '05-21.38', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-21数据\5-21日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-21数据/5-21日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-21数据\5-21日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-21数据/5-21日志上报数据.xlsx", index=False)

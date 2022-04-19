# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-13数据\5-13日志\\'
log.catalogue(path)
a = ['05-13.0', '05-13.1', '05-13.2', '05-13.3', '05-13.4', '05-13.5', '05-13.6', '05-13.7', '05-13.8', '05-13.9',
     '05-13.10', '05-13.11', '05-13.12', '05-13.13', '05-13.14', '05-13.15', '05-13.16', '05-13.17', '05-13.18',
     '05-13.19', '05-13.20', '05-13.21', '05-13.22', '05-13.23', '05-13.24', '05-13.25', '05-13.26', '05-13.27',
     '05-13.28', '05-13.29', '05-13.30', '05-13.31', '05-13.32', '05-13.33', '05-13.34', '05-13.35', '05-13.36',
     '05-13.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-13数据\5-13日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-13数据/5-13日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-13数据\5-13日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-13数据/5-13日志上报数据.xlsx", index=False)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-25数据\5-25日志\\'
log.catalogue(path)
a = ['05-25.0', '05-25.1', '05-25.2', '05-25.3', '05-25.4', '05-25.5', '05-25.6', '05-25.7', '05-25.8', '05-25.9',
     '05-25.10', '05-25.11', '05-25.12', '05-25.13', '05-25.14', '05-25.15', '05-25.16', '05-25.17', '05-25.18',
     '05-25.19', '05-25.20', '05-25.21', '05-25.22', '05-25.23', '05-25.24', '05-25.25', '05-25.26', '05-25.27',
     '05-25.28', '05-25.29', '05-25.30', '05-25.31', '05-25.32', '05-25.33', '05-25.34', '05-25.35', '05-25.36',
     '05-25.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-25数据\5-25日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-25数据/5-25日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-25数据\5-25日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-25数据/5-25日志上报数据.xlsx", index=False)

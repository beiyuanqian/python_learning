# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-20数据\5-20日志\\'
log.catalogue(path)
a = ['05-20.0', '05-20.1', '05-20.2', '05-20.3', '05-20.4', '05-20.5', '05-20.6', '05-20.7', '05-20.8', '05-20.9',
     '05-20.10', '05-20.11', '05-20.12', '05-20.13', '05-20.14', '05-20.15', '05-20.16', '05-20.17', '05-20.18',
     '05-20.19', '05-20.20', '05-20.21', '05-20.22', '05-20.23', '05-20.24', '05-20.25', '05-20.26', '05-20.27',
     '05-20.28', '05-20.29', '05-20.30', '05-20.31', '05-20.32', '05-20.33', '05-20.34', '05-20.35', '05-20.36',
     '05-20.37', '05-20.38', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-20数据\5-20日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-20数据/5-20日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-20数据\5-20日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-20数据/5-20日志上报数据.xlsx", index=False)

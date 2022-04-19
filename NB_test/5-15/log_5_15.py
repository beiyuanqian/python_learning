# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-15数据\5-15日志\\'
log.catalogue(path)
a = ['05-15.0', '05-15.1', '05-15.2', '05-15.3', '05-15.4', '05-15.5', '05-15.6', '05-15.7', '05-15.8', '05-15.9',
     '05-15.10', '05-15.11', '05-15.12', '05-15.13', '05-15.14', '05-15.15', '05-15.16', '05-15.17', '05-15.18',
     '05-15.19', '05-15.20', '05-15.21', '05-15.22', '05-15.23', '05-15.24', '05-15.25', '05-15.26', '05-15.27',
     '05-15.28', '05-15.29', '05-15.30', '05-15.31', '05-15.32', '05-15.33', '05-15.34', '05-15.35', '05-15.36',
     '05-15.37', '05-15.38']

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-15数据\5-15日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-15数据/5-15日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-15数据\5-15日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-15数据/5-15日志上报数据.xlsx", index=False)

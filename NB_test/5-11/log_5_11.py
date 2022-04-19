# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\5-11数据\5-11日志\\'
log.catalogue(path)
a = ['05-11.0', '05-11.1', '05-11.2', '05-11.3', '05-11.4', '05-11.5', '05-11.6', '05-11.7', '05-11.8', '05-11.9',
     '05-11.10', '05-11.11', '05-11.12', '05-11.13', '05-11.14', '05-11.15', '05-11.16', '05-11.17', '05-11.18',
     '05-11.19', '05-11.20', '05-11.21', '05-11.22', '05-11.23', '05-11.24', '05-11.25', '05-11.26', '05-11.27',
     '05-11.28', '05-11.29', '05-11.30', '05-11.31', '05-11.32', '05-11.33', '05-11.34', '05-11.35', '05-11.36',
     '05-11.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-11数据\5-11日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-11数据/5-11日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\5-11数据\5-11日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/5-11数据/5-11日志上报数据.xlsx", index=False)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import log

# 设置文件夹所在路径
path = r'F:\测试项目\门锁\5-24数据\5-24日志\\'
log.catalogue(path)
a = ['05-24.0', '05-24.1', '05-24.2', '05-24.3', '05-24.4', '05-24.5', '05-24.6', '05-24.7', '05-24.8', '05-24.9',
     '05-24.10', '05-24.11', '05-24.12', '05-24.13', '05-24.14', '05-24.15', '05-24.16', '05-24.17', '05-24.18',
     '05-24.19', '05-24.20', '05-24.21', '05-24.22', '05-24.23', '05-24.24', '05-24.25', '05-24.26', '05-24.27',
     '05-24.28', '05-24.29', '05-24.30', '05-24.31', '05-24.32', '05-24.33', '05-24.34', '05-24.35', '05-24.36',
     '05-24.37', ]

for i in range(0, len(a)):
    for line in open(r'F:\测试项目\门锁\5-24数据\5-24日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.xia(line)

# print(data)
date = log.id_xia(log.data)
dataAll_1 = log.transform_array(date, 3)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel(r"F:\测试项目\门锁\5-24数据/5-24日志下发数据.xlsx", index=False)

for i in range(0, len(a)):
    for line in open(r'F:\测试项目\门锁\5-24数据\5-24日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        log.shang(line)
# print(data1)
date1 = log.id_shang(log.data1)
dataAll1_1 = log.transform_array(date1, 3)
print(dataAll1_1)
df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel(r"F:\测试项目\门锁\5-24数据/5-24日志上报数据.xlsx", index=False)

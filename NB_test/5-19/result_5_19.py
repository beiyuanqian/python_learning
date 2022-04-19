# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import pandas as pd
import csv
import result

# 上报数据源
logPath = r"F:\刘小涵\测试项目\门锁\5-19数据\5-19日志上报数据.xlsx"
dic1 = result.redExcel(logPath, 0)
print('上传数据源\n', dic1)
print('上传数据源总数为：', len(dic1))

# 下发数据源
logPath = r"F:\刘小涵\测试项目\门锁\\5-19数据\\5-19日志下发数据.xlsx"
dic2 = result.redExcel(logPath, 0)
print('下发数据源\n', dic2)
print('下发数据源总数为：', len(dic2))

# 理想数据源
dic3 = []
time = []
with open(r'F:\刘小涵\测试项目\门锁\模拟测试数据.csv', 'r') as myFile:
    lines = csv.reader(myFile)
    for line in lines:
        line[0] = line[0].rstrip()
        line[1] = result.format_time(line[1])
        dic3.append(line)
print('理想数据源\n', dic3)
print('理想数据源总数为：', len(dic3))


# 总数据量的对比
result.sum1(dic1, dic2, dic3)
sumAll_1 = result.transform_array(result.sum_1, 10)
# print(sumAll_1)
# 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
df1 = pd.DataFrame(sumAll_1,
                   columns=['imei', "开始时间", '结束时间', "模拟上报总量", "日志上报总量", '日志下发总量',
                            '模拟上报总量-日志上报总量', "模拟上报总量-日志下发总量",
                            "日志上报总量-日志下发总量", "偏差率((日志上报总量-模拟上报总量)/模拟上报总量)"])
sumAll_1_1 = result.transform_array(result.sum_1_1, 2)
# print(sumAll_1_1)
# 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
df1_1 = pd.DataFrame(sumAll_1_1,
                     columns=['imei', "偏差率((日志上报总量-模拟上报总量)/模拟上报总量)"])

# 5个服务标识数据量的对比
result.sum2(dic1, dic2, dic3)
sumAll_2 = result.transform_array(result.sum_2, 12)
print(sumAll_2)
df2 = pd.DataFrame(sumAll_2,
                   columns=['imei', "开始时间", '结束时间', "模拟上报服务标识", "模拟上报总量", "上报服务标识", "日志上报总量", "下发服务标识", "日志下发总量",
                            "模拟上报总量-日志上报总量",
                            "模拟上报总量-日志下发总量", "日志上报总量-日志下发总量"
                            ])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据

# # 查看某个服务标识的离散情况
# result.sum3(dic1)
# sumAll_3 = result.transform_array(result.sum_3, 2)
# print(sumAll_3)
# df3 = pd.DataFrame(sumAll_3,
#                    columns=['imei', "上报时间"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据

# 有误差的设备的信息，如没有异常数据，则该表为空
result.sum4(dic1, dic2)
sumAll_4 = result.transform_array(result.sum_4, 4)
print(sumAll_4)
df4 = pd.DataFrame(sumAll_4,
                   columns=['imei', "上报服务标识", "上报时间", "下发时间"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据

# 保存到本地excel
with pd.ExcelWriter(r'F:\刘小涵\测试项目\门锁\5-19数据\5-19数据对比结果汇总.xlsx') as writer:
    df1.to_excel(writer, sheet_name='总数据量对比')
    df2.to_excel(writer, sheet_name='五个服务标识的总量对比')
    # df3.to_excel(writer, sheet_name='离散时间')
    df4.to_excel(writer, sheet_name='有误差的设备信息')
    df1_1.to_excel(writer, sheet_name='偏差率')

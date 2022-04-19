# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/2/3}


import xlrd
from xlutils.copy import copy
import pandas as pd

path = "D:/PYproject/suguanDATA/上报数据.xlsx"


# 用于处理和获取Excel文件中的测试数据
def redExcel(path, sheet_num):
    # 打开excel，获取【workBook】对象
    workBook = xlrd.open_workbook(path)
    # print(workBook.nsheets)   # 工作簿个数
    # 从工作簿中，获取【workSheet】对象
    workSheet = workBook.sheet_by_index(sheet_num)
    # print(workSheet.nrows)   # 工作表行数
    # 对【workSheet】工作表进行循环-逐行取出数据放入列表中
    retList = []
    for i in range(1, workSheet.nrows):
        oneRow = workSheet.row_values(i)
        retList.append(oneRow)
    # 返回数据列表
    return retList


# 上报数据源
logPath = "F:\刘小涵\测试项目\门锁\日志上报数据.xlsx"
dic1 = redExcel(logPath, 0)
print('上传数据源\n', dic1)
print('上传数据源总数为：', len(dic1))

# 提取设备信息，统计设备个数
equipments = []
for i in range(0, len(dic1)):
    equipments.append(dic1[i][1])
# 统计设备个数，应为67
print('设备数据', set(equipments))
print('设备总个数为：', len(set(equipments)))
equipment = list(set(equipments))
print(equipment)

# 选取时间段
StartDatatime = '2021-03-12 00:00:00.000'
EndDatatime = '2021-03-13 00:00:00.000'

r_xls = xlrd.open_workbook(path)
excel = copy(r_xls)
table = excel.get_sheet(1)

sum = []


def sum1(dic1, dic2):
    for j in range(0, len(equipment)):
        sum.append(equipment[j])

        count1_dic1 = 0

        for i in range(0, len(dic1)):
            if dic1[i][1] == equipment[j]:
                # 将str类型转为时间类型
                datatime = pd.to_datetime(dic1[i][0])  # dic1[i][0]提取时间
                # 判断时间范围
                if (datatime >= pd.to_datetime(StartDatatime)) & (
                        datatime <= pd.to_datetime(EndDatatime)):
                    # 将时间类型转换为str类型
                    dic1[i][0] = str(datatime)
                    # 统计某一时间段内某一设备的数据包实际上报总量
                    if dic1[i][2] != 'login(注册)' and dic1[i][2] != 'bind(绑定)' and dic1[i][2] != 'offlineReport' and \
                            dic1[i][2] != 'onlineReport' and dic1[i][2] != 'lock_info_report' and dic1[i][
                        2] != 'app_version_report' \
                            and dic1[i][2] != 'tem_limit_report' and dic1[i][2] != 'wire_info_report' and dic1[i][
                        2] != 'machine_data_report' \
                            and dic1[i][2] != 'dataReport':
                        count1_dic1 += 1

        print('\n' + StartDatatime + '到' + EndDatatime + '内设备' + str(equipment[j]) + '的统计量分别如下：')
        print('实际上报总量为：', count1_dic1)


sum1(dic1)

table.write(0, 0, 'imei')
table.write(0, 1, '上报时间')
table.write(0, 2, '上报服务标识')
for i in range(1, len(dic1)):
    table.write(i, 0, dic1[i - 1][0])
    table.write(i, 1, dic1[i - 1][1])
    table.write(i, 2, dic1[i - 1][2])
excel.save(path)

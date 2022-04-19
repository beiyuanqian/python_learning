# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import xlrd
import pandas as pd
from result_configuration import equipment, StartDatatime, EndDatatime


# 实现把一维列表转换成二维列表
def transform_array(l, length):
    r = []
    m = []
    for i in range(len(l)):
        m.append(l[i])
        if len(m) == length:
            r.append(m)
            m = []
    return r


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
        # print(oneRow)
        retList.append(oneRow)
    # 返回数据列表
    return retList


# 调整时间为同一格式，例如格式为2016年5月17日，月日可能不足两位的
def format_time(date):
    a = date.replace('/', '-')
    b = a.split(' ')
    b[0] = b[0].split('-')
    b[0][1] = b[0][1].zfill(2)  # 左填充，使2021-2-2格式显示为2021-02-02格式
    b[0][2] = b[0][2].zfill(2)
    date = '-'.join(b[0]) + ' ' + b[1] + ".000"
    return date


# 总数据量的对比
sumAll_1 = []
sum_1 = []
sum_1_1 = []


def sum1(dic1, dic2, dic3):
    for j in range(0, len(equipment)):
        sum_1.append(equipment[j])
        sum_1_1.append(equipment[j])

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
                    if dic1[i][2] == 'data_request(NFC更新)' or dic1[i][2] == 'lockalarm_upload(门锁告警上报)' or \
                            dic1[i][2] == 'data_request(密码更新)' or dic1[i][2] == 'lockdata_upload(门锁状态上报)' or dic1[i][
                        2] == 'opendoor_record(开门记录上报)':
                        count1_dic1 += 1

        print('\n' + StartDatatime + '到' + EndDatatime + '内设备' + str(equipment[j]) + '的统计量分别如下：')
        print('实际上报总量为：', count1_dic1)

        count1_dic2 = 0
        for i in range(0, len(dic2)):
            if dic2[i][1] == equipment[j]:
                # 将str类型转为时间类型
                datatime = pd.to_datetime(dic2[i][0])  # dic2[i][0]提取时间
                # 判断时间范围
                if (datatime >= pd.to_datetime(StartDatatime)) & (
                        datatime <= pd.to_datetime(EndDatatime)):
                    # 将时间类型转换为str类型
                    dic2[i][0] = str(datatime)
                    # 统计某一时间段内某一设备的数据包实际下发总量
                    if dic2[i][2] == 'key_updata(密码更新)' or dic2[i][2] == 'lockalarm_ret(门锁告警上报)' or dic2[i][
                        2] == 'nfc_updata(NFC更新)' or dic2[i][2] == 'lockdata_ret(门锁状态上报)' or dic2[i][
                        2] == 'opendoor_ret(开门记录上报)':
                        count1_dic2 += 1
        print('实际下发总量为：', count1_dic2)

        count1_dic3 = 180
        # for i in range(0, len(dic3)):
        #     if dic3[i][0] == equipment[j]:
        #         StartDatatime_1 = '2021-03-22 00:00:00.000'
        #         EndDatatime_1 = '2021-03-23 10:00:00.000'
        #         # 将str类型转为时间类型
        #         datatime = pd.to_datetime(dic3[i][1])  # 提取时间
        #         # 判断时间范围
        #         if (datatime >= pd.to_datetime(StartDatatime_1)) & (
        #                 datatime <= pd.to_datetime(EndDatatime_1)):
        #             # 将时间类型转换为str类型
        #             dic3[i][1] = str(datatime)
        #             # 统计某一时间段内某一设备的数据包实际上报总量
        #             if dic3[i][2] == 'data_request(NFC更新)' or dic3[i][2] == 'lockalarm_upload(门锁告警上报)' or \
        #                     dic3[i][2] == 'data_request(密码更新)' or dic3[i][2] == 'lockdata_upload(门锁状态上报)' or dic3[i][
        #                 2] == 'opendoor_record(开门记录上报)':
        #                 count1_dic3 += 1
        print('模拟上报总量为：', count1_dic3)

        # 添加设备的统计总数据
        sum_1.append(StartDatatime)
        sum_1.append(EndDatatime)
        sum_1.append(count1_dic3)
        sum_1.append(count1_dic1)
        sum_1.append(count1_dic2)
        # 计算模拟数据与日志上报数据的差异
        sum_1.append(count1_dic3 - count1_dic1)
        # 计算模拟数据与日志下发数据的差异
        sum_1.append(count1_dic3 - count1_dic2)
        # 计算日志上报数据与日志下发数据的差异
        sum_1.append(count1_dic1 - count1_dic2)
        # 计算偏差率((日志上报总量-模拟上报总量)/模拟上报总量)
        sum_1.append(round((count1_dic1 - count1_dic3) / count1_dic3, 5))
        sum_1_1.append(round((count1_dic1 - count1_dic3) / count1_dic3, 5))

    print(sum_1)
    print(sum_1_1)


# 5个服务标识数据量的对比
sumAll_2 = []
sum_2 = []


def sum2(dic1, dic2, dic3):
    for j in range(0, len(equipment)):
        count1_dic1 = 0
        count2_dic1 = 0
        count3_dic1 = 0
        count4_dic1 = 0
        count5_dic1 = 0
        count6_dic1 = 0

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
                    if dic1[i][2] == 'data_request(NFC更新)' or dic1[i][2] == 'lockalarm_upload(门锁告警上报)' or \
                            dic1[i][2] == 'data_request(密码更新)' or dic1[i][2] == 'lockdata_upload(门锁状态上报)' or dic1[i][
                        2] == 'opendoor_record(开门记录上报)':
                        count1_dic1 += 1
                    # 统计某一时间段内不同数据包对应的上报数据总量
                    if dic1[i][2] == 'data_request(密码更新)':
                        count2_dic1 += 1
                    if dic1[i][2] == 'data_request(NFC更新)':
                        count3_dic1 += 1
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)':
                        count4_dic1 += 1
                    if dic1[i][2] == 'opendoor_record(开门记录上报)':
                        count5_dic1 += 1
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)':
                        count6_dic1 += 1
        print('\n' + StartDatatime + '到' + EndDatatime + '内设备' + str(equipment[j]) + '的统计量分别如下：')
        print('实际上报总量为：', count1_dic1)
        print('data_request(密码更新)的总量为：', count2_dic1)
        print('data_request(NFC更新)的总量为：', count3_dic1)
        print('lockdata_upload(门锁状态上报)的总量为：', count4_dic1)
        print('opendoor_record(开门记录上报)的总量为：', count5_dic1)
        print('lockalarm_upload(门锁告警上报)的总量为：', count6_dic1)

        count1_dic2 = 0
        count2_dic2 = 0
        count3_dic2 = 0
        count4_dic2 = 0
        count5_dic2 = 0
        count6_dic2 = 0
        for i in range(0, len(dic2)):
            if dic2[i][1] == equipment[j]:
                # 将str类型转为时间类型
                datatime = pd.to_datetime(dic2[i][0])  # dic1[i][0]提取时间
                # 判断时间范围
                if (datatime >= pd.to_datetime(StartDatatime)) & (
                        datatime <= pd.to_datetime(EndDatatime)):
                    # 将时间类型转换为str类型
                    dic2[i][0] = str(datatime)
                    # 统计某一时间段内某一设备的数据包实际下发总量
                    if dic2[i][2] == 'key_updata(密码更新)' or dic2[i][2] == 'lockalarm_ret(门锁告警上报)' or dic2[i][
                        2] == 'nfc_updata(NFC更新)' or dic2[i][2] == 'lockdata_ret(门锁状态上报)' or dic2[i][
                        2] == 'opendoor_ret(开门记录上报)':
                        count1_dic2 += 1
                    # 统计某一时间段内不同数据包对应的下发数据总量
                    if dic2[i][2] == 'key_updata(密码更新)':
                        count2_dic2 += 1
                    if dic2[i][2] == 'nfc_updata(NFC更新)':
                        count3_dic2 += 1
                    if dic2[i][2] == 'lockdata_ret(门锁状态上报)':
                        count4_dic2 += 1
                    if dic2[i][2] == 'opendoor_ret(开门记录上报)':
                        count5_dic2 += 1
                    if dic2[i][2] == 'lockalarm_ret(门锁告警上报)':
                        count6_dic2 += 1
        print('\n' + StartDatatime + '到' + EndDatatime + '内设备' + str(equipment[j]) + '的统计量分别如下：')
        print('实际下发总量为：', count1_dic2)
        print('key_updata(密码更新)的总量为：', count2_dic2)
        print('nfc_updata(NFC更新)的总量为：', count3_dic2)
        print('lockdata_ret(门锁状态上报)的总量为：', count4_dic2)
        print('opendoor_ret(开门记录上报)的总量为：', count5_dic2)
        print('lockalarm_ret(门锁告警上报)的总量为：', count6_dic2)

        count1_dic3 = 180
        count2_dic3 = 36
        count3_dic3 = 36
        count4_dic3 = 36
        count5_dic3 = 36
        count6_dic3 = 36
        # for i in range(0, len(dic3)):
        #     if dic3[i][0] == equipment[j]:
        #         StartDatatime_1 = '2021-03-22 00:00:00.000'
        #         EndDatatime_1 = '2021-3-23 10:00:00.000'
        #         # # 将str类型转为时间类型
        #         datatime = pd.to_datetime(dic3[i][1])  # dic1[i][0]提取时间
        #         # 判断时间范围
        #         if (datatime >= pd.to_datetime(StartDatatime_1)) & (
        #                 datatime <= pd.to_datetime(EndDatatime_1)):
        #             # 将时间类型转换为str类型
        #             dic3[i][1] = str(datatime)
        #             # 统计某一时间段内某一设备的数据包实际上报总量
        #             count1_dic3 += 1
        #             # 统计某一时间段内不同数据包对应的数据总量
        #             if dic3[i][2] == 'data_request(密码更新0)':
        #                 count2_dic3 += 1
        #             if dic3[i][2] == 'data_request(NFC更新1)':
        #                 count3_dic3 += 1
        #             if dic3[i][2] == 'lockdata_upload(开门状态上报)':
        #                 count4_dic3 += 1
        #                 # if dic3[i][2] == 'opendoor_record(开门记录上报)':
        #                 count5_dic3 += 1
        #             if dic3[i][2] == 'lockalarm_upload(门锁告警上报)':
        #                 count6_dic3 += 1
        print('\n' + StartDatatime + '到' + EndDatatime + '内设备' + str(equipment[j]) + '的统计量分别如下：')
        print('理想上报总量为：', count1_dic3)
        print('data_request(密码更新0)的总量为：', count2_dic3)
        print('data_request(NFC更新1)的总量为：', count3_dic3)
        print('lockdata_upload(开门状态上报)的总量为：', count4_dic3)
        print('opendoor_record(开门记录上报)的总量为：', count5_dic3)
        print('lockalarm_upload(门锁告警上报)的总量为：', count6_dic3)

        # 添加设备的五种服务标识的统计数据
        sum_2.append(equipment[j])  # 添加设备信息
        sum_2.append(StartDatatime)
        sum_2.append(EndDatatime)
        sum_2.append('data_request(密码更新0)')
        sum_2.append(count2_dic3)
        sum_2.append('data_request(密码更新)')
        sum_2.append(count2_dic1)
        sum_2.append('key_updata(密码更新)')
        sum_2.append(count2_dic2)
        # 计算密码更新状态的模拟数据与日志上报数据的差异
        sum_2.append(count2_dic3 - count2_dic1)
        # 计算密码更新状态的模拟数据与日志下发数据的差异
        sum_2.append(count2_dic3 - count2_dic2)
        # 计算密码更新状态的日志上报数据与日志下发数据的差异
        sum_2.append(count2_dic1 - count2_dic2)

        sum_2.append(equipment[j])  # 添加设备信息
        sum_2.append(StartDatatime)
        sum_2.append(EndDatatime)
        sum_2.append('data_request(NFC更新1)')
        sum_2.append(count3_dic3)
        sum_2.append('data_request(NFC更新)')
        sum_2.append(count3_dic1)
        sum_2.append('nfc_updata(NFC更新)')
        sum_2.append(count3_dic2)
        sum_2.append(count3_dic3 - count3_dic1)
        sum_2.append(count3_dic3 - count3_dic2)
        sum_2.append(count3_dic1 - count3_dic2)

        sum_2.append(equipment[j])  # 添加设备信息
        sum_2.append(StartDatatime)
        sum_2.append(EndDatatime)
        sum_2.append('lockdata_upload(开门状态上报)')
        sum_2.append(count4_dic3)
        sum_2.append('lockdata_upload(门锁状态上报)')
        sum_2.append(count4_dic1)
        sum_2.append('lockdata_ret(门锁状态上报)')
        sum_2.append(count4_dic2)
        sum_2.append(count4_dic3 - count4_dic1)
        sum_2.append(count4_dic3 - count4_dic2)
        sum_2.append(count4_dic1 - count4_dic2)

        sum_2.append(equipment[j])  # 添加设备信息
        sum_2.append(StartDatatime)
        sum_2.append(EndDatatime)
        sum_2.append('opendoor_record(开门记录上报)')
        sum_2.append(count5_dic3)
        sum_2.append('opendoor_record(开门记录上报)')
        sum_2.append(count5_dic1)
        sum_2.append('opendoor_ret(开门记录上报)')
        sum_2.append(count5_dic2)
        sum_2.append(count5_dic3 - count5_dic1)
        sum_2.append(count5_dic3 - count5_dic2)
        sum_2.append(count5_dic1 - count5_dic2)

        sum_2.append(equipment[j])  # 添加设备信息
        sum_2.append(StartDatatime)
        sum_2.append(EndDatatime)
        sum_2.append('lockalarm_upload(门锁告警上报)')
        sum_2.append(count6_dic3)
        sum_2.append('lockalarm_upload(门锁告警上报)')
        sum_2.append(count6_dic1)
        sum_2.append('lockalarm_ret(门锁告警上报)')
        sum_2.append(count6_dic2)
        sum_2.append(count6_dic3 - count6_dic1)
        sum_2.append(count6_dic3 - count6_dic2)
        sum_2.append(count6_dic1 - count6_dic2)

    print(sum_2)


# # 查看密码更新和NFC更新服务标识的离散情况
# sumAll_3_1 = []
# sum_3_1 = []
#
# datatime_1 = []
#
#
# def sum3_1(dic1):
#     for j in range(0, len(equipment)):
#         for i in range(0, len(dic1)):
#             if dic1[i][1] == equipment[j]:
#                 if dic1[i][2] == 'data_request(密码更新)' or dic1[i][2] == 'data_request(NFC更新)':
#                     datatime_1.append(dic1[i][0])
#                     sum_3_1.append(equipment[j])
#                     sum_3_1.append(dic1[i][2])
#                     sum_3_1.append(dic1[i][0])
#     # print("密码更新和NFC更新服务标识的离散情况")
#     # print(datatime_1)
#
#
# # 查看门锁状态上报服务标识的离散情况
# sumAll_3_2 = []
# sum_3_2 = []
#
# datatime_2 = []
#
#
# def sum3_2(dic1):
#     for j in range(0, len(equipment)):
#         for i in range(0, len(dic1)):
#             if dic1[i][1] == equipment[j]:
#                 if dic1[i][2] == 'lockdata_upload(门锁状态上报)':
#                     datatime_2.append(dic1[i][0])
#                     sum_3_2.append(equipment[j])
#                     sum_3_2.append(dic1[i][2])
#                     sum_3_2.append(dic1[i][0])
#     # print("门锁状态上报服务标识的离散情况")
#     # print(datatime_2)
#
#
# # 查看开门记录上报服务标识的离散情况
# sumAll_3_3 = []
# sum_3_3 = []
#
# datatime_3 = []
#
#
# def sum3_3(dic1):
#     for j in range(0, len(equipment)):
#         for i in range(0, len(dic1)):
#             if dic1[i][1] == equipment[j]:
#                 if dic1[i][2] == 'opendoor_record(开门记录上报)':
#                     datatime_3.append(dic1[i][0])
#                     sum_3_3.append(equipment[j])
#                     sum_3_3.append(dic1[i][2])
#                     sum_3_3.append(dic1[i][0])
#     # print("开门记录上报服务标识的离散情况")
#     # print(datatime_3)
#
#
# # 查看门锁告警上报服务标识的离散情况
# sumAll_3_4 = []
# sum_3_4 = []
#
# datatime_4 = []
#
#
# def sum3_4(dic1):
#     for j in range(0, len(equipment)):
#         for i in range(0, len(dic1)):
#             if dic1[i][1] == equipment[j]:
#                 if dic1[i][2] == 'lockalarm_upload(门锁告警上报)':
#                     datatime_4.append(dic1[i][0])
#                     sum_3_4.append(equipment[j])
#                     sum_3_4.append(dic1[i][2])
#                     sum_3_4.append(dic1[i][0])
#     # print("门锁告警上报服务标识的离散情况")
#     # print(datatime_4)


# 有误差的设备的信息，如没有异常数据，则该表为空
sumAll_4 = []
sum_4 = []


def sum4(dic1, dic2):
    dic1_1 = []
    dic1_2 = []
    dic1_3 = []
    dic1_4 = []
    dic1_5 = []
    dic2_1 = []
    dic2_2 = []
    dic2_3 = []
    dic2_4 = []
    dic2_5 = []

    for j in range(0, len(equipment)):

        count1_dic1 = 0
        count2_dic1 = 0
        count3_dic1 = 0
        count4_dic1 = 0
        count5_dic1 = 0
        count6_dic1 = 0
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
                    count1_dic1 += 1
                    # 统计某一时间段内不同数据包对应的上报数据总量
                    if dic1[i][2] == 'data_request(密码更新)':
                        count2_dic1 += 1
                    if dic1[i][2] == 'data_request(NFC更新)':
                        count3_dic1 += 1
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)':
                        count4_dic1 += 1
                    if dic1[i][2] == 'opendoor_record(开门记录上报)':
                        count5_dic1 += 1
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)':
                        count6_dic1 += 1

        count1_dic2 = 0
        count2_dic2 = 0
        count3_dic2 = 0
        count4_dic2 = 0
        count5_dic2 = 0
        count6_dic2 = 0
        for i in range(0, len(dic2)):
            if dic2[i][1] == equipment[j]:
                # 将str类型转为时间类型
                datatime = pd.to_datetime(dic2[i][0])  # dic1[i][0]提取时间
                # 判断时间范围
                if (datatime >= pd.to_datetime(StartDatatime)) & (
                        datatime <= pd.to_datetime(EndDatatime)):
                    # 将时间类型转换为str类型
                    dic2[i][0] = str(datatime)
                    # 统计某一时间段内某一设备的数据包实际下发总量
                    count1_dic2 += 1
                    # 统计某一时间段内不同数据包对应的下发数据总量
                    if dic2[i][2] == 'key_updata(密码更新)':
                        count2_dic2 += 1
                    if dic2[i][2] == 'nfc_updata(NFC更新)':
                        count3_dic2 += 1
                    if dic2[i][2] == 'lockdata_ret(门锁状态上报)':
                        count4_dic2 += 1
                    if dic2[i][2] == 'opendoor_ret(开门记录上报)':
                        count5_dic2 += 1
                    if dic2[i][2] == 'lockalarm_ret(门锁告警上报)':
                        count6_dic2 += 1

        # 密码更新的异常数据
        # 判断原始列表是否为空，如果不为空，会出现多个设备的同一服务标识的数据写到一起，造成数据错误
        if dic1_1 != [] and dic2_1 != []:
            dic1_1 = []
            dic2_1 = []
            for i in range(0, len(dic1)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic1[i][2] == 'data_request(密码更新)' and dic1[i][1] == equipment[j]:
                        # 把有问题的设备的密码更新状态的上报时间写到一个列表里
                        dic1_1.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic2[i][2] == 'key_updata(密码更新)' and dic2[i][1] == equipment[j]:
                        # 把有问题的设备的密码更新状态的下发时间写到一个列表里
                        dic2_1.append(dic2[i][0])
            # 如果两个时间列表的长度不一样，则匹配时间字符串，使列表的长度与长列表保持一致，在长度较短的列表里不对应的时间位置上加null,使列表保持一致
            if len(dic1_1) > len(dic2_1):
                # 如果列表为空则无法匹配时间字符串，因此列表为空时，在空列表加上对应数量的null值，若列表不为空，则在不对应的时间位置上加null
                if dic2_1 == []:
                    for i in range(0, len(dic1_1)):
                        dic2_1.insert(i, "null")
                elif dic2_1 != []:
                    for i in range(0, len(dic1_1)):
                        if dic1_1[i][0:17] != dic2_1[i][0:17]:
                            dic2_1.insert(i, "null")
            elif len(dic1_1) < len(dic2_1):
                if dic1_1 == []:
                    for i in range(0, len(dic2_1)):
                        dic2_1.insert(i, "null")
                elif dic1_1 != []:
                    for i in range(0, len(dic2_1)):
                        if dic1_1[i][0:17] != dic2_1[i][0:17]:
                            dic1_1.insert(i, "null")
            # 当上报与下发数量不一致时，循环查找该设备的密码更新状态，及添加对应上报与下发时间
            k = 0
            for i in range(0, len(dic1)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic1[i][2] == 'data_request(密码更新)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_1):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('data_request(密码更新)')
                            sum_4.append(dic1_1[k])
                            sum_4.append(dic2_1[k])
                            k = k + 1
        elif dic1_1 == [] and dic2_1 == []:
            for i in range(0, len(dic1)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic1[i][2] == 'data_request(密码更新)' and dic1[i][1] == equipment[j]:
                        dic1_1.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic2[i][2] == 'key_updata(密码更新)' and dic2[i][1] == equipment[j]:
                        dic2_1.append(dic2[i][0])
            if len(dic1_1) > len(dic2_1):
                if dic2_1 == []:
                    for i in range(0, len(dic1_1)):
                        dic2_1.insert(i, "null")
                elif dic2_1 != []:
                    for i in range(0, len(dic1_1)):
                        if dic1_1[i][0:17] != dic2_1[i][0:17]:
                            dic2_1.insert(i, "null")
            elif len(dic1_1) < len(dic2_1):
                if dic1_1 == []:
                    for i in range(0, len(dic2_1)):
                        dic2_1.insert(i, "null")
                elif dic1_1 != []:
                    for i in range(0, len(dic2_1)):
                        if dic1_1[i][0:17] != dic2_1[i][0:17]:
                            dic1_1.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count2_dic1 - count2_dic2) != 0:
                    if dic1[i][2] == 'data_request(密码更新)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_1):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('data_request(密码更新)')
                            sum_4.append(dic1_1[k])
                            sum_4.append(dic2_1[k])
                            k = k + 1

        # NFC更新的异常数据
        if dic1_2 != [] and dic2_2 != []:
            dic1_2 = []
            dic2_2 = []
            for i in range(0, len(dic1)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic1[i][2] == 'data_request(NFC更新)' and dic1[i][1] == equipment[j]:
                        dic1_2.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic2[i][2] == 'nfc_updata(NFC更新)' and dic2[i][1] == equipment[j]:
                        dic2_2.append(dic2[i][0])
            if len(dic1_2) > len(dic2_2):
                if dic2_2 == []:
                    for i in range(0, len(dic1_2)):
                        dic2_2.insert(i, "null")
                elif dic2_2 != []:
                    for i in range(0, len(dic1_2)):
                        if dic1_2[i][0:17] != dic2_2[i][0:17]:
                            dic2_2.insert(i, "null")
            elif len(dic1_2) < len(dic2_2):
                if dic1_2 == []:
                    for i in range(0, len(dic2_2)):
                        dic2_2.insert(i, "null")
                elif dic1_2 != []:
                    for i in range(0, len(dic2_2)):
                        if dic1_2[i][0:17] != dic2_2[i][0:17]:
                            dic1_2.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic1[i][2] == 'data_request(NFC更新)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_2):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('data_request(NFC更新)')
                            sum_4.append(dic1_2[k])
                            sum_4.append(dic2_2[k])
                            k = k + 1
        elif dic1_2 == [] and dic2_2 == []:
            for i in range(0, len(dic1)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic1[i][2] == 'data_request(NFC更新)' and dic1[i][1] == equipment[j]:
                        dic1_2.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic2[i][2] == 'nfc_updata(NFC更新)' and dic2[i][1] == equipment[j]:
                        dic2_2.append(dic2[i][0])
            if len(dic1_2) > len(dic2_2):
                if dic2_2 == []:
                    for i in range(0, len(dic1_2)):
                        dic2_2.insert(i, "null")
                elif dic2_2 != []:
                    for i in range(0, len(dic1_2)):
                        try:
                            if dic1_2[i][0:17] != dic2_2[i][0:17]:
                                dic2_2.insert(i, "null")
                        except:
                            dic2_2.insert(i, "error")
            elif len(dic1_2) < len(dic2_2):
                if dic1_2 == []:
                    for i in range(0, len(dic2_2)):
                        dic2_2.insert(i, "null")
                elif dic1_2 != []:
                    for i in range(0, len(dic2_2)):
                        if dic1_2[i][0:17] != dic2_2[i][0:17]:
                            dic1_2.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count3_dic1 - count3_dic2) != 0:
                    if dic1[i][2] == 'data_request(NFC更新)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_2):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('data_request(NFC更新)')
                            sum_4.append(dic1_2[k])
                            sum_4.append(dic2_2[k])
                            k = k + 1

        # 门锁状态上报的异常数据
        if dic1_3 != [] and dic2_3 != []:
            dic1_3 = []
            dic2_3 = []
            for i in range(0, len(dic1)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)' and dic1[i][1] == equipment[j]:
                        dic1_3.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic2[i][2] == 'lockdata_ret(门锁状态上报)' and dic2[i][1] == equipment[j]:
                        dic2_3.append(dic2[i][0])
            if len(dic1_3) > len(dic2_3):
                if dic2_3 == []:
                    for i in range(0, len(dic1_3)):
                        dic2_3.insert(i, "null")
                elif dic2_3 != []:
                    for i in range(0, len(dic1_3)):
                        if dic1_3[i][0:17] != dic2_3[i][0:17]:
                            dic2_3.insert(i, "null")
            elif len(dic1_3) < len(dic2_3):
                if dic1_3 == []:
                    for i in range(0, len(dic2_3)):
                        dic2_3.insert(i, "null")
                elif dic1_3 != []:
                    for i in range(0, len(dic2_3)):
                        if dic1_3[i][0:17] != dic2_3[i][0:17]:
                            dic1_3.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_3):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('lockdata_upload(门锁状态上报)')
                            sum_4.append(dic1_3[k])
                            sum_4.append(dic2_3[k])
                            k = k + 1
        elif dic1_3 == [] and dic2_3 == []:
            for i in range(0, len(dic1)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)' and dic1[i][1] == equipment[j]:
                        dic1_3.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic2[i][2] == 'lockdata_ret(门锁状态上报)' and dic2[i][1] == equipment[j]:
                        dic2_3.append(dic2[i][0])
            if len(dic1_3) > len(dic2_3):
                if dic2_3 == []:
                    for i in range(0, len(dic1_3)):
                        dic2_3.insert(i, "null")
                elif dic2_3 != []:
                    for i in range(0, len(dic1_3)):
                        if dic1_3[i][0:17] != dic2_3[i][0:17]:
                            dic2_3.insert(i, "null")
            elif len(dic1_3) < len(dic2_3):
                if dic1_3 == []:
                    for i in range(0, len(dic2_3)):
                        dic2_3.insert(i, "null")
                elif dic1_3 != []:
                    for i in range(0, len(dic2_3)):
                        if dic1_3[i][0:17] != dic2_3[i][0:17]:
                            dic1_3.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count4_dic1 - count4_dic2) != 0:
                    if dic1[i][2] == 'lockdata_upload(门锁状态上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_3):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('lockdata_upload(门锁状态上报)')
                            sum_4.append(dic1_3[k])
                            sum_4.append(dic2_3[k])
                            k = k + 1

        # 开门记录上报的异常数据
        if dic1_4 != [] and dic2_4 != []:
            dic1_4 = []
            dic2_4 = []
            for i in range(0, len(dic1)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic1[i][2] == 'opendoor_record(开门记录上报)' and dic1[i][1] == equipment[j]:
                        dic1_4.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic2[i][2] == 'opendoor_ret(开门记录上报)' and dic2[i][1] == equipment[j]:
                        dic2_4.append(dic2[i][0])
            if len(dic1_4) > len(dic2_4):
                if dic2_4 == []:
                    for i in range(0, len(dic1_4)):
                        dic2_4.insert(i, "null")
                elif dic2_4 != []:
                    for i in range(0, len(dic1_4)):
                        if dic1_4[i][0:15] != dic2_4[i][0:15]:
                            dic2_4.insert(i, "null")
            elif len(dic1_4) < len(dic2_4):
                if dic1_4 == []:
                    for i in range(0, len(dic2_4)):
                        dic2_4.insert(i, "null")
                elif dic1_4 != []:
                    for i in range(0, len(dic2_4)):
                        if dic1_4[i][0:15] != dic2_4[i][0:15]:
                            dic1_4.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic1[i][2] == 'opendoor_record(开门记录上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_4):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('opendoor_record(开门记录上报)')
                            sum_4.append(dic1_4[k])
                            sum_4.append(dic2_4[k])
                            k = k + 1
        elif dic1_4 == [] and dic2_4 == []:
            for i in range(0, len(dic1)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic1[i][2] == 'opendoor_record(开门记录上报)' and dic1[i][1] == equipment[j]:
                        dic1_4.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic2[i][2] == 'opendoor_ret(开门记录上报)' and dic2[i][1] == equipment[j]:
                        dic2_4.append(dic2[i][0])
            if len(dic1_4) > len(dic2_4):
                if dic2_4 == []:
                    for i in range(0, len(dic1_4)):
                        dic2_4.insert(i, "null")
                elif dic2_4 != []:
                    for i in range(0, len(dic1_4)):
                        try:
                            if dic1_4[i][0:15] != dic2_4[i][0:15]:
                                dic2_4.insert(i, "null")
                        except:
                            dic2_4.insert(i, "error")
            elif len(dic1_4) < len(dic2_4):
                if dic1_4 == []:
                    for i in range(0, len(dic2_4)):
                        dic2_4.insert(i, "null")
                elif dic1_4 != []:
                    for i in range(0, len(dic2_4)):
                        try:
                            if dic1_4[i][0:15] != dic2_4[i][0:15]:
                                dic1_4.insert(i, "null")
                        except:
                            dic1_4.insert(i, "error")
            k = 0
            for i in range(0, len(dic1)):
                if (count5_dic1 - count5_dic2) != 0:
                    if dic1[i][2] == 'opendoor_record(开门记录上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_4):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('opendoor_record(开门记录上报)')
                            try:
                                sum_4.append(dic1_4[k])
                                sum_4.append(dic2_4[k])
                            except:
                                sum_4.append(dic1_4[k])
                                sum_4.append("error")
                            k = k + 1

        # 门锁告警上报的异常数据
        if dic1_5 != [] and dic2_5 != []:
            dic1_5 = []
            dic2_5 = []
            for i in range(0, len(dic1)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)' and dic1[i][1] == equipment[j]:
                        dic1_5.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic2[i][2] == 'lockalarm_ret(门锁告警上报)' and dic2[i][1] == equipment[j]:
                        dic2_5.append(dic2[i][0])
            if len(dic1_5) > len(dic2_5):
                if dic2_5 == []:
                    for i in range(0, len(dic1_5)):
                        dic2_5.insert(i, "null")
                elif dic2_5 != []:
                    for i in range(0, len(dic1_5)):
                        if dic1_5[i][0:17] != dic2_5[i][0:17]:
                            dic2_5.insert(i, "null")
            elif len(dic1_5) < len(dic2_5):
                if dic1_5 == []:
                    for i in range(0, len(dic2_5)):
                        dic2_5.insert(i, "null")
                elif dic1_5 != []:
                    for i in range(0, len(dic2_5)):
                        if dic1_5[i][0:17] != dic2_5[i][0:17]:
                            dic1_5.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_5):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('lockalarm_upload(门锁告警上报)')
                            sum_4.append(dic1_5[k])
                            sum_4.append(dic2_5[k])
                            k = k + 1
        elif dic1_5 == [] and dic2_5 == []:
            for i in range(0, len(dic1)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)' and dic1[i][1] == equipment[j]:
                        dic1_5.append(dic1[i][0])
            for i in range(0, len(dic2)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic2[i][2] == 'lockalarm_ret(门锁告警上报)' and dic2[i][1] == equipment[j]:
                        dic2_5.append(dic2[i][0])
            if len(dic1_5) > len(dic2_5):
                if dic2_5 == []:
                    for i in range(0, len(dic1_5)):
                        dic2_5.insert(i, "null")
                elif dic2_5 != []:
                    for i in range(0, len(dic1_5)):
                        if dic1_5[i][0:17] != dic2_5[i][0:17]:
                            dic2_5.insert(i, "null")
            elif len(dic1_5) < len(dic2_5):
                if dic1_5 == []:
                    for i in range(0, len(dic2_5)):
                        dic2_5.insert(i, "null")
                elif dic1_5 != []:
                    for i in range(0, len(dic2_5)):
                        if dic1_5[i][0:17] != dic2_5[i][0:17]:
                            dic1_5.insert(i, "null")
            k = 0
            for i in range(0, len(dic1)):
                if (count6_dic1 - count6_dic2) != 0:
                    if dic1[i][2] == 'lockalarm_upload(门锁告警上报)' and dic1[i][1] == equipment[j]:
                        while k < len(dic1_5):
                            sum_4.append(equipment[j])  # 添加设备信息
                            sum_4.append('lockalarm_upload(门锁告警上报)')
                            sum_4.append(dic1_5[k])
                            sum_4.append(dic2_5[k])
                            k = k + 1

    print(sum_4)

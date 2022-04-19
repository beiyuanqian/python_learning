# -*- coding: utf-8 -*-
import re  # 导入包：re 模块使 Python 语言拥有全部的正则表达式功能
import pandas as pd
import os


def transform_array(l, length):  # 实现把一维列表转换成二维列表
    r = []
    m = []
    for i in range(len(l)):
        m.append(l[i])
        if len(m) == length:
            r.append(m)
            m = []
    return r



def id_xia(list1):
    list = []
    for i in list1:
        if i == 'nfc_updata':
            list.append('nfc_updata(NFC更新)')
        elif i == 'opendoor_ret':
            list.append('opendoor_ret(开门记录上报)')
        elif i == 'lockdata_ret':
            list.append('lockdata_ret(门锁状态上报)')
        elif i == 'key_updata':
            list.append('key_updata(密码更新)')
        elif i == 'lockalarm_ret':
            list.append('lockalarm_ret(门锁告警上报)')
        elif i == 'login_ret':
            list.append('login_ret(注册)')
        elif i == 'bind_ret':
            list.append('bind_ret(绑定)')
        else:
            list.append(i)
    return list


def id_shang(list1):
    list = []
    for i in list1:
        # if i == 'data_request':
        #     list.append('data_request(NFC更新)')
        if i == 'opendoor_record':
            list.append('opendoor_record(开门记录上报)')
        elif i == 'lockdata_upload':
            list.append('lockdata_upload(门锁状态上报)')
        # elif i == 'data_request':
        #     list.append('data_request(密码更新)')
        elif i == 'lockalarm_upload':
            list.append('lockalarm_upload(门锁告警上报)')
        elif i == 'login':
            list.append('login(注册)')
        elif i == 'bind':
            list.append('bind(绑定)')
        else:
            list.append(i)
    return list


# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\4-25数据\4-25日志\\'
# 列出路径下所有的文件
files = os.listdir(path)
a = []
for i in range(len(files)):
    a.append(files[i].split('log-info-2021-')[1].split('.log')[0])
print(a)
a = ['04-25.0', '04-25.1', '04-25.2', '04-25.3', '04-25.4', '04-25.5', '04-25.6', '04-25.7', '04-25.8', '04-25.9',
     '04-25.10', '04-25.11', '04-25.12', '04-25.13', '04-25.14', '04-25.15', '04-25.16', '04-25.17', '04-25.18',
     '04-25.19', '04-25.20', '04-25.21', '04-25.22', '04-25.23', '04-25.24', '04-25.25', '04-25.26', '04-25.27',
     '04-25.28', '04-25.29', '04-25.30', '04-25.31', '04-25.32', '04-25.33', '04-25.34', '04-26.0', '04-26.1',
     '04-26.2', '04-26.3', '04-26.4', '04-26.5', '04-26.6', '04-26.7', '04-26.8', '04-26.9', '04-26.10', '04-26.11', ]

dataAll_1 = []
dataAll_2 = []
data = []
date = []

for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\4-25数据\4-25日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        if (line.find("imeiList") > 0):
            imeirIndex = line.index("imeiList") + 12
            imeir = line[imeirIndex: imeirIndex + 15]  # imei值长度固定，直接通过字符串位置截取数据，也可以用正则表达式截取
            cmdTypeData = re.findall(r"cmdType\":\"(.*?)\",", line)
            cmdType = cmdTypeData[0]
            timer = line[:23]  # time值长度固定，直接通过字符串位置截取数据，也可以用正则表达式截取
            data.append(timer)
            data.append(imeir)
            data.append(cmdType)

# print(data)
date = id_xia(data)
dataAll_1 = transform_array(date, 3)
print(dataAll_1)
# for j in range(0, len(equipment)):
#     for i in range(0, len(dataAll_1)):
#         if dataAll_1[i][1] == equipment[j]:
#             # datatime = pd.to_datetime(dataAll_1[i][0])  # dic1[i][0]提取时间
#             # # 判断时间范围
#             # if (datatime >= pd.to_datetime(StartDatatime)) & (
#             #         datatime <= pd.to_datetime(EndDatatime)):
#             #     # 将时间类型转换为str类型
#             #     dataAll_1[i][0] = str(datatime)
#             if dataAll_1[i][2] == 'key_updata(密码更新)' or dataAll_1[i][2] == 'lockalarm_ret(门锁告警上报)' or dataAll_1[i][
#                 2] == 'nfc_updata(NFC更新)' or dataAll_1[i][2] == 'lockdata_ret(门锁状态上报)' or dataAll_1[i][
#                 2] == 'opendoor_ret(开门记录上报)':
#                 dataAll_2.append(dataAll_1[i])
# print('dataAll2:', dataAll_2)
df = pd.DataFrame(dataAll_1,
                  columns=["下发时间", '下发imei', "下发服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/4-25数据/4-25日志下发数据.xlsx", index=False)

dataAll1_1 = []
dataAll1_2 = []
data1 = []
date1 = []

for i in range(0, len(files)):
    for line in open(r'F:\刘小涵\测试项目\门锁\4-25数据\4-25日志\\log-info-2021-' + a[i] + '.log', "r", encoding='UTF-8'):
        if (line.find("OkHttp") > 0):
            times = line[:23]
            imeisIndex = line.index("imei") + 7
            imeis = line[imeisIndex: imeisIndex + 15]  # imei值长度固定，直接通过字符串位置截取数据，也可以用正则表达式截取
            data1.append(times)
            data1.append(imeis)
            # if (line.find('\\\"request_type\\\"')>0):
            # eventTypeDatas = re.findall(r"request_type\\\":(.*?),", line)
            eventTypeData = re.findall(r"eventType\":\"(.*?)\"},", line)  # eventType值长度不固定，通过re.findall函数，采用正则表达式截取
            eventType = eventTypeData[0]  # re.findall函数返回结果是List列表形式，得到列表中eventType数据
            requestType = re.findall(r"request_type\\\":(.*?),", line)  # eventType值长度不固定，通过re.findall函数，采用正则表达式截取
            if requestType == []:
                # data1.append('')
                data1.append(eventType)
            elif requestType == ['1'] and eventType == 'data_request':
                # data1.append(requestType[0])
                data1.append(eventType + "(NFC更新)")
            elif requestType == ['0'] and eventType == 'data_request':
                # data1.append(requestType[0])
                data1.append(eventType + "(密码更新)")
# print(data1)
date1 = id_shang(data1)
dataAll1_1 = transform_array(date1, 3)
print(dataAll1_1)
# for j in range(0, len(equipment)):
#     for i in range(0, len(dataAll1_1)):
#         if dataAll1_1[i][1] == equipment[j]:
#             # datatime = pd.to_datetime(dataAll_1[i][0])  # dic1[i][0]提取时间
#             # # 判断时间范围
#             # if (datatime >= pd.to_datetime(StartDatatime)) & (
#             #         datatime <= pd.to_datetime(EndDatatime)):
#             #     # 将时间类型转换为str类型
#             #     dataAll_1[i][0] = str(datatime)
#             if dataAll1_1[i][2] == 'data_request(NFC更新)' or dataAll1_1[i][2] == 'lockalarm_upload(门锁告警上报)' or \
#                     dataAll1_1[i][2] == 'data_request(密码更新)' or dataAll1_1[i][2] == 'lockdata_upload(门锁状态上报)' \
#                     or dataAll1_1[i][2] == 'opendoor_record(开门记录上报)':
#                 dataAll1_2.append(dataAll1_1[i])
# print('dataAll2:', dataAll1_2)

df = pd.DataFrame(dataAll1_1,
                  columns=["上报时间", '上报imei', "上报服务标识"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/4-25数据/4-25日志上报数据.xlsx", index=False)

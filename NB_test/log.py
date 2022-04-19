# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/6}

import os
import re


def catalogue(path):
    # 列出路径下所有的文件
    files = os.listdir(path)
    a = []
    for i in range(len(files)):
        a.append(files[i].split('log-info-2021-')[1].split('.log')[0])
    print(a)


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


dataAll1_1 = []
dataAll1_2 = []
data1 = []
date1 = []


def shang(line):
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
    return data1


dataAll_1 = []
dataAll_2 = []
data = []
date = []


def xia(line):
    if (line.find("imeiList") > 0):
        imeirIndex = line.index("imeiList") + 12
        imeir = line[imeirIndex: imeirIndex + 15]  # imei值长度固定，直接通过字符串位置截取数据，也可以用正则表达式截取
        cmdTypeData = re.findall(r"cmdType\":\"(.*?)\",", line)
        cmdType = cmdTypeData[0]
        timer = line[:23]  # time值长度固定，直接通过字符串位置截取数据，也可以用正则表达式截取
        data.append(timer)
        data.append(imeir)
        data.append(cmdType)
    return data

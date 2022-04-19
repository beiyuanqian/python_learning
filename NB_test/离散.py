# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/15}

import pandas as pd
import os
import datetime
from datetime import datetime


# # a="04747 05-14#18:57:11.989 182 00000 Recive result:0"
# # print(a.split(" "))
# # b="!!ERROR!!  04762 2021-05-14#18:57:13.261 [Log Missing] log buffer is full!!!"
# # print(b.split(" "))
#
def catalogue(path):
    # 列出路径下所有的文件
    files = os.listdir(path)
    a = []
    for i in range(len(files)):
        a.append(files[i].split('COM6_2021-05-')[1].split('.log')[0])
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


# 设置文件夹所在路径
path = r'F:\刘小涵\测试项目\门锁\离散数据\离散日志\\'
catalogue(path)
a = ['17_15-37-14', '18_09-48-04']

data = []
for i in range(0, len(a)):
    for line in open(r'F:\刘小涵\测试项目\门锁\离散数据\离散日志\\COM6_2021-05-' + a[i] + '.log', "r", encoding='UTF-8'):
        # if "#" in line or "!!ERROR!!" in line:
        #     if "#" in line:
        #         data.append("2021-" + line[line.index("#") - 5:line.index("#") + 13].replace("#", " "))
        #     elif "!!ERROR!!" in line and line.index("!!ERROR!!") == 0 and "2021" in line:
        #         data.append(line.split(" ")[4] + " " + line.split(" ")[5])
        if "random_ret time" in line:
            print(line)
            data.append(int(line.split("random_ret time")[1].replace(":", "").replace("\n", "")) * 5)
print(len(data))
print(data)

dataAll_1 = transform_array(data, 1)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["下发时间"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/离散数据/时间数据.xlsx", index=False)

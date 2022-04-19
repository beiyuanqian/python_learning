# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/15}

import xlrd
import pandas as pd
from datetime import datetime


def transform_array(l, length):  # 实现把一维列表转换成二维列表
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


# 上报数据源
logPath = r"F:/刘小涵/测试项目/门锁/离散数据/时间数据.xlsx"
dic = redExcel(logPath, 0)
print('时间\n', dic)
print('时间总数为：', len(dic))
data = []
for i in range(len(dic) - 1):
    # print(dic[i][0])
    # print(dic[i+1][0])
    starttime = datetime.strptime(dic[i][0], "%Y-%m-%d %H:%M:%S.%f")
    endtime = datetime.strptime(dic[i + 1][0], "%Y-%m-%d %H:%M:%S.%f")
    data.append(str(endtime - starttime))
    print(endtime - starttime)
dataAll_1 = transform_array(data, 1)
print(dataAll_1)

df = pd.DataFrame(dataAll_1,
                  columns=["时间间隔"])  # 使用pd.DataFrame对dataAll创建一个矩阵数据，columns为表头，dataAll为表的数据
# 保存到本地excel
df.to_excel("F:/刘小涵/测试项目/门锁/离散数据/时间间隔.xlsx", index=False)

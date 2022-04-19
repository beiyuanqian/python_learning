# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/25}
import xlrd
from xlutils.copy import copy


# 一、设计一个读取excel中数据的函数，功能：传递excel的路径+名称，第几个工作表,返回数据列表
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


# 二、实现工作簿复制函数，返回新的工作簿
def getNewExcel(path):
    # 打开工作簿
    workBook = xlrd.open_workbook(path,formatting_info=True)
    # print(workBook.nsheets)
    # 复制
    newWorkBook = copy(workBook)
    return newWorkBook

# path = 'D:\PYproject\APITest\data\教管系统-测试用例V1.2.xls'
# # retList = redExcel(path, 0)
# # # print(retList)
# # newPath=""
# # newWorkBook = getNewExcel(path)
# # newWorkBook.save(newPath)
# newWorkBook=getNewExcel(path)
# savePath='D:\PYproject\APITest\data\教管系统-测试用例V1.3.xls'
# newWorkBook.save(savePath)

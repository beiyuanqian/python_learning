# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/27}
from APITestWork.lib.excelManagerlib import redExcel
from APITestWork.lib.courselib import add, list, delete
import json
import time


# 实现发送课程管理请求的函数，传入的是excel中的一行参数
def sendCourseReq(row):
    # 传入的是一行数据，也就是一个测试用例
    # print(row)
    # 第五列的值
    colus5 = row[4]
    # print(colus5)
    # 第六列的值,为字符串，需要转为字典格式,用loads方法
    colus6 = json.loads(row[5])
    # print(colus6['name'])
    url = row[9]
    method = row[10]
    header = json.loads(row[11])
    # print(method)

    ret = None
    if colus5 == 'add':
        # 获取课程名称
        courseName = colus6['name']
        # 把关键字替换成时间戳
        courseName = courseName.replace('{{courseName}}', str(int(time.time() * 10000000)))
        ret = add(courseName, colus6['desc'], colus6['display_idx'], url, method, header)
    elif colus5 == 'list':
        ret = list(colus6['pagenum'], colus6['pagesize'], url, method, header)
    elif colus5 == 'delete':
        ret = delete(colus6['id'], url, method, header)
    return ret

# path = 'D:\PYproject\APITestWork\data\教管系统-测试用例V1.2.xls'
# retList = redExcel(path, 2)
# print(retList[25])
# sendCourseReq(retList[25])

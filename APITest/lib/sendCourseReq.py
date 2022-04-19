# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/27}
from APITest.lib.excelManagerlib import redExcel
from APITest.lib.courselib import add, list, delete
import json
import time


# 实现发送课程管理请求的函数，传入的书excel中的一行参数
def sendCourseReq(row):
    # 传入的是一行数据，也就是一个测试用例
    # print(row)
    # 第五列的值
    colus5 = row[4]
    # print(colus5)
    # 第六列的值,为字符串，需要转为字典格式,用loads方法
    colus6 = json.loads(row[5])
    # print(colus6['name'])

    ret = None
    if colus5 == 'add':
        # 获取课程名称
        courseName = colus6['name']
        # 把关键字替换成时间戳
        courseName = courseName.replace('{{courseName}}', str(int(time.time() * 10000000)))
        ret = add(courseName, colus6['desc'], colus6['display_idx'])
    elif colus5 == 'list':
        ret = list(colus6['pagenum'], colus6['pagesize'])
    elif colus5 == 'delete':
        ret = delete(colus6['id'])
    return ret
# path = 'D:\PYproject\APITest\data\教管系统-测试用例V1.2.xls'
# retList = redExcel(path, 0)
# sendCourseReq(retList[0])

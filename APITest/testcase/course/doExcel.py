# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/27}
from APITest.lib.excelManagerlib import redExcel, getNewExcel
from APITest.lib.sendCourseReq import sendCourseReq
import json

path = 'D:\PYproject\APITest\data\教管系统-测试用例V1.2.xls'
newPath = 'D:\PYproject\APITest\\report\教管系统-测试结果.xls'

newWorkBook = getNewExcel(path)
# print(newWorkBook)
newWorkSheet = newWorkBook.get_sheet(0)
# print(newWorkSheet.nrows)
# newWorkBook.save(newPath)
# 从Excel中读取工作表中的测试用例
retList = redExcel(path, 0)
# print(retList)

for i in range(0, len(retList)):
    row = retList[i]
    # print(row)
    ret = sendCourseReq(row)
    # print(ret)
    colus7 = json.loads(row[6])
    # print(colus7)
    if ret['retcode'] == colus7['code']:
        print(row[0] + '测试通过')
        newWorkSheet.write(i + 1, 7, '测试通过')
    else:
        print(row[0] + '测试不通过')
        newWorkSheet.write(i + 1, 7, '测试不通过')
        if 'reason' in ret.keys():
            newWorkSheet.write(i + 1, 8, ret['reason'])

newWorkBook.save(newPath)

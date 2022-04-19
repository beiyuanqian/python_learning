# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/28}

from APITest.lib.courselib import add, list
import time

retlist = list(1, 20)
# 新增课程
courseName = '大学英语' + str(int(time.time() * 10000))
ret = add(courseName, '课程描述', '0')

print(retlist['total'])
if ret['retcode'] == 0:
    print(">>>>>>>>新增课程测试成功1")
    # 列出课程
    retlist1 = list(1, 20)
    print(retlist1['total'])
    if retlist['total']+1==retlist1['total']:
        print('>>>>>>新增课程测试成功2')
    # isExit = True
    # for data in retlist['retlist']:
    #     print(data)
    #     if courseName == data['name']:
    #         print('>>>>>>新增课程测试成功2')
    #         isExit = False
    #         break
    # if isExit:
    #     print('>>>>>>测试不通过，列表中不存在')

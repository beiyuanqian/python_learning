# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/28}
import unittest
from APITest.lib.excelManagerlib import redExcel, getNewExcel
from APITest.lib.sendCourseReq import sendCourseReq
import json
from APITest.lib.courselib import add, list
import time
from APITest.lib.courselib import add, list, delete


class DemoUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print('>>>>>>类级别的数据初始化运行了')
        cls.clearData()

    @classmethod
    def clearData(cls):
        retlist = list(1, 100)
        num = 0
        for data in retlist['retlist']:
            delete(data['id'])
            num = num + 1
        print("共删除了：", num, '条数据')

    @classmethod
    def tearDownClass(cls):
        # print('>>>>>>类级别的环境清除运行了')
        cls.clearData()

    def test001(self):
        pass
        # print('方法1调用了')
        # if 1 == 1:
        #     print('测试通过')
        # self.assertEqual(1, 2, '输出到报告中的内容')  # 断言
        # path = r'D:\PYproject\APITest\data\教管系统-测试用例V1.2.xls'
        #
        # # 从Excel中读取工作表中的测试用例
        # retList = redExcel(path, 0)
        # # print(retList)
        # # 循环发送请求
        # for i in range(0, len(retList)):
        #     row = retList[i]
        #     # print(row)
        #     ret = sendCourseReq(row)
        #     # print(ret)
        #     colus7 = json.loads(row[6])
        #     # print(colus7)
        #     # 断言
        #     if ret['retcode'] == colus7['code']:
        #         print(row[0] + '测试通过')
        #     else:
        #         print(row[0] + '测试不通过')

    @unittest.skip('skip的原因')
    def test002(self):
        print('方法2调用了')

    def test003(self):
        # print('方法3调用了')
        retlist = list(1, 20)
        # 新增课程
        courseName = '大学英语' + str(int(time.time() * 10000))
        ret = add(courseName, '课程描述', '0')
        print(ret)
        self.assertEqual(ret['retcode'], 0, '新增课程失败1')
        print(">>>>>>>>新增课程测试成功1")

        # 列出课程
        retlist1 = list(1, 20)
        self.assertEqual(retlist['total'] + 1, retlist1['total'], '新增课程失败2')
        print(">>>>>>>>新增课程测试成功2")

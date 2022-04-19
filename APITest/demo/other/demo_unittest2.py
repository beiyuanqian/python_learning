# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/28}

import unittest


class DemoUnittest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('>>>>>>类级别的数据初始化运行了')

    @classmethod
    def tearDownClass(cls):
        print('>>>>>>类级别的环境清除运行了')

    def test021(self):
        print('方法21调用了')
        if 1 == 1:
            print('测试通过')
        self.assertEqual(1, 1, '输出到报告中的内容')  # 断言

    @unittest.skip('skip的原因')
    def test022(self):
        print('方法22调用了')

    def test023(self):
        print('方法23调用了')

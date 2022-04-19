# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/17}
import unittest
from APITest.demo.other.demo_unittest import DemoUnittest
from APITest.demo.other.demo_unittest2 import DemoUnittest2
from ClassicHTMLTestRunner import HTMLTestRunner

# 构建测试套件test_suite(可以重复)
suite = unittest.TestSuite()

# 方法一：用例逐个添加到suite
# suite.addTest(DemoUnittest("test001"))
# suite.addTest(DemoUnittest("test002"))
# suite.addTest(DemoUnittest("test003"))
# suite.addTest(DemoUnittest2("test023"))

# 方法二：用例放入列表中，再添加到suite
# list=[DemoUnittest("test001"),DemoUnittest("test002"),DemoUnittest("test003"),DemoUnittest2("test023")]
# suite.addTests(list)

# 方法三：通过TestLoader类的discover 方法来（使用）,*代表模糊匹配
suite = unittest.defaultTestLoader.discover('demo.other', pattern='demo_unittest*.py')

# 测试运行器----testrunner查看结果
# 第一种，不使用HtmlTestRunner插件
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第二种，使用【经典版】HtmlTestRunner插件（使用）
path = r"D:\PYproject\APITest\report\htmlReport.html"
reportFile=open(path, 'wb')
# 第三方插件HTMLTestRunner，可以返回一个runner对象
runner = HTMLTestRunner(stream=reportFile, verbosity=2, description='用例执行明细', title='xxx项目测试报告', tester='刘小涵')
runner.run(suite)

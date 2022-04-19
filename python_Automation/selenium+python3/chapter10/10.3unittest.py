# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/27}

import unittest
from selenium import webdriver
from time import sleep

class add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")

    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(u"python")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        assert u"python" in self.driver.page_source, "页面中不存在要搜索的关键字"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__mian__':
    unittest.main()

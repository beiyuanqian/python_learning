# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/8}

# ================================= 11.1测试函数 =================================
# from chapter11.name_function import get_formatted_name
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name:")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name: " + formatted_name + ".")

import unittest
from chapter11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 方法名必须以test_开头，才能自动运行
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()

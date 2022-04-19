# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/9}
import unittest
from chapter11.employee import Employee

# my_employee = Employee('Janis', 'Joplin', 100000)
# my_employee.show_employee()
# my_employee.give_raise()
# my_employee.show_employee()


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Janis', 'Joplin', 100000)

    def test_give_default_raise(self):
        """测试默认年薪增加量"""
        self.employee.give_raise()
        self.assertEqual(105000, self.employee.annual_salary)

    def test_give_custom_raise(self,):
        """测试随意增加年薪量"""
        self.employee.give_raise(80)
        self.assertEqual(100080, self.employee.annual_salary)


unittest.main()

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/9}

class Employee():
    """雇员信息"""

    def __init__(self, first_name, last_name, annual_salary):
        """存储雇员信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def show_employee(self):
        """显示雇员信息"""
        print(self.first_name + " " + self.last_name + "的年薪为" + str(self.annual_salary))

    def give_raise(self, increment=5000):
        """年薪增加量默认为5000"""
        self.annual_salary += increment

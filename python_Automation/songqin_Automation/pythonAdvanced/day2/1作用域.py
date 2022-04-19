# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/13}


#
"""
作用域是程序运行时变量可被访问的范围
定义在函数内的变量是局部变量
定义在模块最外层的变量是全局变量
"""
# L(Local):局部作用域
def foo():
    a = "hello world"
    print(a)
    def bar():
        b = "hello world"
        print(a)
print(foo())









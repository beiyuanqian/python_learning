# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/13}

# 在一个内部函数里边，对在外部作用域（不能是全局作用域）的变量进行调用
# 那么这个内部函数就被称之为闭包
def outer():
    x = 10
    def inner():
        print(x)
    return inner
outer()()  # inner
# 可以拆分为下面两行
a = outer()  # a = inner
a()   # inner


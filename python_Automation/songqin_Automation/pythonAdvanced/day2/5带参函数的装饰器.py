# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/13}


def bar(func):
    def inner():
        func()
        # 此处是装饰器为函数新增的功能
        print("学会了神奇的知识")
    return inner
@bar
def foo(something):
    print("do", something)
foo("看电视")





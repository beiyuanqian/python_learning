# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/13}

@bar
def foo():
    print("over")

def bar(func):
    def inner():
        func()
        print("成功捕获手机壳颜色")
        print("成功调整界面主题")
    return inner
foo = bar(foo)
print(foo)
foo()



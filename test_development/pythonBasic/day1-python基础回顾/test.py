#-*- coding: utf-8 -*-
#@File    : test.py
#@Time    : 2021/4/13 20:09
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/4/13
print()
"""
json格式：
    1- 自动化测试：做接口自动化测试  响应数据里  resp.json()  接收数据
    2- 测试开发：做后端服务--接口返回数据类型json
转化方法：
    1- json--转--字典     import json   json.loads()
    2- 字典--转--json     import json   json.dumps()
常见报错
    JSONDecodeError
    在  json  false  true      空值 null
    python    False  True      空值 None
    键值对的字符串  双引号！ 
"""
# josn1 = '{"info":null}'
# import json
# print(json.loads(josn1))

#2- 集合
# a = [1,2,3,4]
# b = [2,3,4,5]
#
# print(set(a) & set(b))#交集  共同数据
# print(set(a) | set(b))#并集
# print(set(b) - set(a))#插集

#3- 函数
"""
装包/封包
    在函数定义的时候 def test(*args,**kwargs)
解包
    在函数调用的时候，传递的实参 需要解包
    test(*[1,2],**{"name":"tom"})
    
使用场景：
    接口自动化测试---读取excel测试用例
    
"""
# def test(a,b=0,*args,**kwargs):
#     """
#     :param a: 必填
#     :param b: 可缺省  不传就默认值
#     :param args: 元组
#     :param kwargs: 字典
#     :return:
#     """
#     print(a,b,args,kwargs)
#
# if __name__ == '__main__':
#     test(1,2,3,4,5,6,**{"name":"hello"})#name="hello"


#4- 装饰器
import time

def show_time(func):#test函数名
    def inner():
        startTime = time.time()#开始时间
        #执行的接口测试
        func()#test()----函数调用
        endTime = time.time()#结束时间
        print('自动化测试耗时>>> ',endTime-startTime)
    return inner#函数名---函数对象

@show_time #等价  test=show_time(test)
def test():
    print('---我正在执行自动化测试-1--')
    time.sleep(2)#模拟请求时间

@show_time
def xt():
    print('---我在操作---')



if __name__ == '__main__':
    test()
    xt()

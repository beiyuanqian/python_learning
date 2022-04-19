# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/7}

# 可引入输出报错信息
import traceback

# 1-if过滤：事先已知的问题，事前处理
# 2-事后处理:可以处理未知的异常，异常机制
# while True:
#     num = input("input a number:")
#     try:
#         print("100 / %s = %s" % (num, 100.0 / int(num)))
#     # 捕获处理一种异常（类）----对号入座
#     # except ZeroDivisionError:
#     #     print("处理方案1--除数不能为0！")
#     # except ValueError:
#     #     print("处理方案2--除数不能为非数字字符！")
#     # 打印出异常
#     # except ValueError as error:
#     #     print("处理方案2--除数不能为非数字字符！", error)
#     # 捕获所有异常
#     # except Exception as error:
#     # except:
#     # except Exception:
#     #     print("有异常了---具体什么异常不知道")
#     except:
#         print("输出异常的详细信息，包括行号", traceback.format_exc())
#     else:
#         print("无异常时执行，必须放在所有except后，finally之前")
#     finally:
#         print("只能放在最后，不管是否异常，都要执行的代码")

# 异常：从下往上抛出
"""
具体报错的那行代码，在最后一个报错信息
如果调用第三方库报错：
1、最后一行报错是底层内部代码报错，你不知道具体是什么错误
2、看你在哪里调用了这个第三方方法（参数类型错误、个数错误......）
"""


# 自定义异常
class UserValueError(Exception):
    print("")


class NameTooLongError(Exception):
    err = 'name.long'
    print("NameTooLongError")

    def methFun(selfself):
        pass


class NameTooShortError(Exception):
    print("NameTooShortError")


def inputName():
    name = input("请输入用户名：")
    if len(name) > 10:
        # 自定义的异常要自行抛出
        raise NameTooLongError
    elif len(name) < 5:
        raise NameTooShortError


try:
    inputName()
except NameTooShortError:
    print("您输入的用户名过短！")
except NameTooLongError as e:
    print("您输入的用户名过长！", e.err)
    e.methFun()

# 断言 assert-检查点-如果后续代码比较重要，且很依靠前面的数据或状态
tel = input("请输入手机号：")
assert len(tel) == 11, "手机位数有误！"
print("我在处理手机运营商操作")

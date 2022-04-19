# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/30}

import uuid

user_dict = {
    # 存用户名和密码
    "user1": "123",
    "user2": "123",
}
 
token = None


def auth(func):

    def inner(*args, **kwargs):
        global token
        if token:  # token有效
            func(*args, **kwargs)
        else:  # token无效
            userName = input("请输入用户名>>>")
            userPwd = input("请输入密码>>>")
            if userName in user_dict and userPwd == user_dict[userName]:
                func(*args, **kwargs)
                token = str(uuid.uuid4())  # 生成一个uuid作为token
            else:
                print("账户名或密码错误")

    return inner


@auth
def my_log():
    print("this is my_log")


@auth
def my_name(name):
    print("欢迎登录", name)


@auth
def my_shopping_mall():
    print("商城购物")


while True:
    choose_num = input("\n1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项(输入q退出)>>>")
    if choose_num == "q" or choose_num == "Q":
        break
    elif choose_num == "1":
        my_log()
    elif choose_num == "2":
        my_name("张三")
    elif choose_num == "3":
        my_shopping_mall()
    else:
        print("输入不合法")

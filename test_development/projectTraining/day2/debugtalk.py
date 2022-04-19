# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/6/10}

# 函数返回的参数，在此处定义
import requests


def login_variables():
    return {"user": "auto", "psw": "sdfsdfsdf"}


def login_parameters():
    return [
        {"user": "auto", "psw": "sdfsdfsdf", "code": 0},
        {"user": "auto1", "psw": "sdfsdf", "code": 1},
        {"user": "auto", "psw": "sdfsdfsdf1", "code": 1}
    ]


def hook_setup():
    with open('setup.txt', 'w', encoding='utf-8') as f:
        f.write('执行初始化')


def hook_teardown():
    with open('teardown.txt', 'w', encoding='utf-8') as f:
        f.write('执行清除')


def add_course(name):
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'
    payload = {
        "action": "add_course",
        "data": f'{"name":{{name}},"desc":{{name}}描述,"display_idx":"4"}'
    }
    resp = requests.post(url, data=payload)
    return resp.json()


def delete_course(_id):
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'
    payload = {
        "action": "delete_course",
        "id": _id
    }
    resp = requests.delete(url, data=payload)
    return resp.json()

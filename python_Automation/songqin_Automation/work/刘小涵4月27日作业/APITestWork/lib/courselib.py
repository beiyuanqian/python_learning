# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}
import requests


def add(name, desc, display_idx, url, method, header):
    # 教管系统新增课程1
    payload = {'action': 'add_course', 'data': f"""{{"name": "{name}",
                        "desc": "{desc}",
                        "display_idx": "{display_idx}"}}"""}
    if method == 'post':
        r = requests.post(url, headers=header, data=payload)
        try:
            return r.json()
        except:
            return {{"reason": '添加课程失败'}}


# print(add(5,8,'1'))
def list(pagenum, pagesize, url, method, header):
    # 教管系统列出课程
    payload = {"action": "list_course", "pagenum": pagenum, "pagesize": pagesize}
    if method == 'get':
        r = requests.get(url, headers=header, params=payload)
    return r.json()


def modify(id, name, desc, display_idx, url, method, header):
    payload = {'action': 'modify_course', 'id': id,
               'newdata': f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'
               }
    if method == 'put':
        r = requests.put(url, headers=header, data=payload)
    return r.json()


def add2(name, desc, display_idx, url, method, header):
    # 教管系统新增课程2
    payload = {
        'action': 'add_course_json',
        'data': {"name": name, "desc": desc, "display_idx": display_idx}
    }
    if method == 'post':
        r = requests.post(url, headers=header, json=payload)
    return r.json()


def delete(id, url, method, header):
    # 教管系统删除课程
    payload = {'action': 'delete_course', 'id': id}
    if method == 'delete':
        r = requests.delete(url, headers=header, data=payload)
        try:
            return r.json()
        except:
            return {'retcode': 888, 'reason': '项目异常'}

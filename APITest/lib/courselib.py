# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}
import requests
from APITest.config import HOST


def add(name, desc, display_idx):
    # 教管系统新增课程1
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {'action': 'add_course', 'data': f"""{{"name": "{name}",
                        "desc": "{desc}",
                        "display_idx": "{display_idx}"}}"""}

    r = requests.post(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return r.json()
    except:
        return {{"reason": '添加课程失败'}}


# print(add(5,8,'1'))
def list(pagenum, pagesize):
    # 教管系统列出课程
    payload = {"action": "list_course", "pagenum": pagenum, "pagesize": pagesize}
    r = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload)
    return r.json()


def modify(id, name, desc, display_idx):
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {'action': 'modify_course', 'id': id,
               'newdata': f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'
               }
    r = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    return r.json()


def add2(name, desc, display_idx):
    # 教管系统新增课程2
    header = {"Content-Type": "application/json"}
    payload = {
        'action': 'add_course_json',
        'data': {"name": name, "desc": desc, "display_idx": display_idx}
    }
    r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', headers=header, json=payload)
    return r.json()


def delete(id):
    # 教管系统删除课程
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {'action': 'delete_course', 'id': id}
    r = requests.delete(f'{HOST}/apijson/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}

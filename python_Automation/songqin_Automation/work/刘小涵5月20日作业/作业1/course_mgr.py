# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/8}
import requests


def listCourse():
    resp = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    courses = resp.json()['retlist']
    return [c['name'] for c in courses]

def get_hot_goods():
    pass
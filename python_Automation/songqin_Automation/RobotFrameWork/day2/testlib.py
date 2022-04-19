# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/6}
import time


def gettime1():
    return time.time()


def webapi(url):
    import requests
    resp = requests.get(url)
    return resp.text

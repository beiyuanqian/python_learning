# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}
import requests
import time
from APITest.config import HOST

# 教管系统新增课程1
header = {"Content-Type": "application/x-www-form-urlencoded"}
cookie = {'sessionid': 'szm1jbjly2w04hte6d8qc91m179haaao'}
name = "大学英语" + str(int(time.time() * 100))
payload = {'action': 'add_course',
           'data': f"""{{"name": "{name}",
"desc": "初中化学课程",
"display_idx": "4"}}"""}

r = requests.post(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload, cookies=cookie)
print(r.text)
r.encoding = 'unicode_escape'
print(r.text)

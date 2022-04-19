# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}
import requests
from APITest.config import HOST
# 教管系统新增课程2
header = {"Content-Type": "application/json"}
# 口诀4：如果传递的参数是一个字典，request库会自动转为json字符串
payload = {
    'action': 'add_course_json',
    'data': {"name": "初中化学1", "desc": "初中化学课程", "display_idx": "4"}
}
r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', headers=header, json=payload)
print(r.text)

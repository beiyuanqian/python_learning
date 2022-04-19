# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}

import requests
from APITest.config import HOST
# 教管系统登录
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = {'username': 'auto', 'password': 'sdfsdfsdf'}
r = requests.post(f'{HOST}/api/mgr/loginReq', headers=header, data=payload)
print(r.text)
print(r.cookies['sessionid'])

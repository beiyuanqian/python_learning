# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}

import requests
from APITest.config import HOST
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = {'action': 'delete_course', 'id': '122abc'}
r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
print(r.text)

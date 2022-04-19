# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}

import requests
from APITest.config import HOST
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = {'action': 'modify_course', 'id': '1588', 'newdata': '{"name":"3","desc":"2","display_idx":"3"}'
           }
r = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
print(r.text)

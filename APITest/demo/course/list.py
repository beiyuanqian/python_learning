# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/19}
import requests
from APITest.config import HOST
# 教管系统列出课程
payload = {"action": "list_course", "pagenum": "1", "pagesize": "20"}
r = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload)
print(r.text)
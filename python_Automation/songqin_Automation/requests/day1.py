# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/17}

import requests

# # 以百度为例
# r = requests.get('http://www.baidu.com')
# r.encoding = "utf-8"
# print(r.text)  # 响应消息体

# 教管系统列出课程
# 写法1
# r = requests.get('http://127.0.0.1/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
# 写法2
# payload = {"action": "list_course", "pagenum": "1", "pagesize": "20"}
# r = requests.get('http://127.0.0.1/api/mgr/sq_mgr/', params=payload)
# print(r.text)
# print(r.json()['retlist'])

# 教管系统新增课程1
# header = {"Content-Type": "application/x-www-form-urlencoded"}
# # 口诀2：如果传递的参数是一个字典，request库会自动编码为表单
# payload = {'action': 'add_course', 'data': """{"name": "初中化学",
#                     "desc": "初中化学课程",
#                     "display_idx": "4"}"""}
# # 口诀3：如果传递的参数是一个字符串，request库会自动按原格式发送
# payload1 = '''action=add_course&data={"name": "初中化学",
#                     "desc": "初中化学课程",
#                     "display_idx": "4"}'''
# payload1=payload1.encode(encoding='utf-8')
# r = requests.post('http://127.0.0.1/api/mgr/sq_mgr/', headers=header, data=payload1)
# print(r.text)

# 教管系统新增课程2
# header = {"Content-Type": "application/json"}
# # 口诀4：如果传递的参数是一个字典，request库会自动转为json字符串
# payload1 = {
#     'action': 'add_course_json',
#     'data': {"name": "初中化学1","desc": "初中化学课程","display_idx": "4"}
# }
# r = requests.post('http://127.0.0.1/apijson/mgr/sq_mgr/', headers=header, json=payload)
# print(r.text)

# 教管系统登录
# header = {"Content-Type": "application/x-www-form-urlencoded"}
# payload = {'username': 'auto', 'password': 'sdfsdfsdf'}
# r = requests.post('http://127.0.0.1/api/mgr/loginReq', headers=header, data=payload)
# print(r.text)

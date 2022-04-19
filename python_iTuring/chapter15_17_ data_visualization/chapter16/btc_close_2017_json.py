# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/10}

from __future__ import (absolute_import, division, print_function, unicode_literals)
# python3.x版本
from urllib.request import urlopen
import json, requests

json_url = "file:///D:/PYproject/python_iTuring/chapter15_17_%20data_visualization/chapter16/btc_close_2017.json"

# 使用urlopen方法读取数据
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open("btc_close_2017_urllib.json", "wb") as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)

# # 使用requests方法读取数据
# req = requests.get(json_url)
# # 将数据写入文件
# with open("btc_close_2017_request.json", "w") as f:
#     f.write(req.text)
# file_requests = req.json()
# print(file_requests)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}

from selenium import webdriver
from time import sleep

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置隐性等待
driver.implicitly_wait(10)
# 访问网址
driver.get("https://pan.baidu.com/")
# 设置全屏显示
driver.maximize_window()
sleep(5)

"""
print("登陆前")
cookies = driver.get_cookies()
print(cookies)
sleep(30)
# print("登陆后")
# cookies = driver.get_cookies()
"""
# 通过cookie操作的形式来绕过验证码甚至是二维码等安全机制
coo = [{'domain': '.pan.baidu.com', 'expiry': 1589617790.420229, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '2943177036130555455%3ADJI9ZdfpjgIZum8lD9VYuYYFB6Yu73HpLCBwnKh4IIRmdgH80XY%2BhUci2O0YbEjpMqnk%2F6iU0GN84gtjpWZ8zqKK%2FFH5WUxXqxTrnWunDcjXwwaw%2BFngCnZNBoZ8i0CTW8pfgMw2m%2FrQ8rlESRQE3CZTnz2RR6t%2BZFCUk453j8DrbkBUnMiFfw%3D%3D'}, {'domain': '.baidu.com', 'expiry': 1590395390, 'httpOnly': False, 'name': 'cflag', 'path': '/', 'secure': False, 'value': '13%3A3'}, {'domain': '.pan.baidu.com', 'expiry': 1592123387.992698, 'httpOnly': True, 'name': 'SCRC', 'path': '/', 'secure': False, 'value': '851fe000e51718d85092f8e9de38fd98'}, {'domain': '.pan.baidu.com', 'expiry': 1592123387.99266, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '1a37d4894d691cd6872b7b4fc2885e1da1720bc062ab944bc8aa750d48759d27'}, {'domain': 'pan.baidu.com', 'expiry': 4181531387.725298, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1848731386.636256, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'HF0NHpvcjhmRXpJbnh5eVo3ek5ObS1WSGpOcWtoNUk2OGg4NnhRc09UUDYzLVZlRVFBQUFBJCQAAAAAAAAAAAEAAAAR6teEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPpSvl76Ur5eS'}, {'domain': '.pan.baidu.com', 'expiry': 1621067387.808113, 'httpOnly': False, 'name': 'PANWEB', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1621067357.407032, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'D429B31717BD372D2E858E8B948D9E37:FG=1'}]

for cookie in coo:
    # 直接添加cookie会报错，解决办法如下
    # 删除该字段
    if 'expiry' in cookie:
        del cookie['expiry']

    # 将expiry类型变为int
    # if isinstance(cookie.get('expiry'), float):
    #      cookie['expiry'] = int(cookie['expiry'])
    driver.add_cookie(cookie)

sleep(5)
driver.get("https://pan.baidu.com/")


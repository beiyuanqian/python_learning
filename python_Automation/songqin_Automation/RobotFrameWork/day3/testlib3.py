# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/8}
from robot.api.logger import console


def check_score(score):
    if int(score) >= 60:
        print("恭喜及格")
        console("恭喜及格")
    else:
        print("回去复习")
        console("回去复习")
# 嵌套循环——多重判断


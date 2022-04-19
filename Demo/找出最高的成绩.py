# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/12/27}

grade_name = {'xiaoming': '85', 'xiaoli': '74', 'xiaohong': '92'}


def test1(grade_name):
    c = []
    for grade in grade_name.values():
        c.append(grade)
    c.sort(reverse=True)
    print("最高的成绩是" + c[0])


def test2(name, grade):
    grade_name[name]=grade
    print(grade_name)


test1(grade_name)
test2("xiaoming", "88")

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

# 读文件
# f = open("w.txt", 'r')
# print(f.read(2))
# print(f.readline())
# print(f.readline())
# print(f.readlines()[1])

# 写文件
# f = open("w.txt", 'w')
# f.write("test")
# f.write("python")

# 处理CSV文件
# import csv
# csvfile = "test.csv"
# c = csv.reader(open(csvfile, "r"))
# for cs in c:
#     # print(type(c)
#     # print(cs)
#     for i in range(len(cs)):
#         # print(type(cs[i]))
#         print(cs[i])

# 处理Excel文件
# import xlrd
# xls = xlrd.open_workbook("test.xlsx")
# # 通过sheets()方法获取sheet
# # sheet = xls.sheets()[0]
# # 通过sheet名称获取
# # sheet = xls.sheet_by_name("sheet1")
# # 通过sheet索引获取
# sheet = xls.sheet_by_index(0)
# print(sheet.nrows)  # 打印表格总行数
# print(sheet.ncols)  # 打印表格总列数
# print(sheet.row_values(1)[0])  # 打印表格第二行，第一列的数据
# for r in range(sheet.nrows):
#     for c in range(sheet.ncols):
#         print(sheet.row_values(r)[c])

# 写入Excel操作
# import xlwt
# wb = xlwt.Workbook()
# sheet = wb.add_sheet(u"测试")
# sheet.write(0, 0, "automation")
# sheet.write(0, 1, "selenium course")
# wb.save("automate1.xls")

# json文件操作
# # dumps()方法：将python对象编码成json字符串
# import json
# json_dada = {'j1': 1, 'j2': 2, 'j3': 3, 'j4': 4}
# json_1 = json.dumps(json_dada)
# print(json_1)
# print(type(json_1))
# # 打印python的字典元素
# dict_data = {'j1': 1, 'j2': 2, 'j3': 3, 'j4': 4}
# print(dict_data)
# # loads()方法：将json字符串编码成python对象
# json_dada1 = '{"j1": 1, "j2": 2, "j3": 3, "j4": 4}'
# text_json = json.loads(json_dada1)
# print(text_json)
# print(type(text_json))

# 读取json文件
# import json
# f = open('test.json', 'r')
# print(json.load(f))

# 写入json文件
# import json
# f = open("ttt.json", "w")
# js = {'j1': 'a', 'j2': 'b', 'j3': 'c', 'j4': 'd'}
# json.dump(js, f)

# xml文件操作
# import xml.dom.minidom
# # 返回文档节点对象
# dom = xml.dom.minidom.parse('user.xml')
# root = dom.documentElement
# # 返回带有指定名称的所有元素的节点列表
# list = root.getElementsByTagName("user")
# # 读取用户信息
# # 返回某一元素的属性值
# # print(list[0].getAttribute("id"))
# # print(list[0].getElementsByTagName("password")[0].childNodes[0].nodeValue)
# # 遍历xml文件中的所有值
# for l in list:
#     print(l.getAttribute("id"))
#     print(l.getElementsByTagName("password")[0].childNodes[0].nodeValue)
#     print(l.getElementsByTagName("username")[0].childNodes[0].nodeValue)


# YAML文件操作
import yaml
file_1 = open('config.yml')
# # 返回一个字典对象
# yml = yaml.load(file_1, Loader=yaml.FullLoader)
# print(yml)
# print(type(yml))
# # yaml.dump将一个python对象转化成YAML文档
# object_1 = {'name': 'Jack', 'age': 23, 'children': {'name': 'Jason', 'age': 2, 'name_1': 'Jeff', 'age_1': 4}}
# print(yaml.dump(object_1,))

# 将YAML格式的数据转化成python list类型的数据
# file_2 = open('config6.yml')
# yml = yaml.load(file_2, Loader=yaml.FullLoader)
# print(yml)
# print(type(yml))
# # 将YAML格式的数据转化为复合类型的数据，其中包含list和字典数据类型
# file_3 = open('config5.yml')
# yml_3 = yaml.load(file_3, Loader=yaml.FullLoader)
# print(yml_3)
# print(type(yml_3))

# 文件夹操作
# import os
# # 打印当前执行脚本所在目录
# print(os.getcwd())
# # 如果当前路径存在则返回“True”，不存在则返回“False”
# print(os.path.exists('D:\PYproject\w.txt'))
# # 判断当前路径是否是一个文件，如果是，则返回“True”
# print(os.path.isfile(r'D:\PYproject\w.txt'))
# # 可以删除多级目录
# # os.removedirs(r'D:\PYproject\123')
# # 在当前目录下创建‘test1221’单个文件夹
# os.mkdir("test1221")
# # 可以创建多级目录
# os.makedirs(r'D:\PYproject\123\1\2')

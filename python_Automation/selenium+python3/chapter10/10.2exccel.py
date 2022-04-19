# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/22}

# 10.2.1创建Excel文件，维护测试数据
# import xlrd
# def read_excel(filename, index):
#     # 用xlrd模块的open方法打开Excel文件
#     xls = xlrd.open_workbook(filename)
#     # 指定要选择的表格
#     sheet = xls.sheet_by_index(index)
#     # 打印选定表格的行数
#     print(sheet.nrows)
#     # 打印选定表格的列数
#     print(sheet.ncols)
#     # # 用列表的方式存储Excel中读取的数据
#     # data = []
#     # # 将遍历Excel中的第一列数据，并添加到列表data中
#     # for i in range(sheet.nrows):
#     #     data.append(sheet.row_values(i)[0])
#     #     print(sheet.row_values(i)[0])
#     # return data
#     # 用字典的形式存储数据
#     dic = {}
#     for j in range(sheet.ncols):
#         data = []
#         for i in range(sheet.nrows):
#             data.append(sheet.row_values(i)[j])
#         dic[j] = data
#     return dic
#
# print(read_excel("testdata.xlsx", 0))

# 10.2.2 Framework Log设置
import logging

# 只输出Warnning级别之上的日志
# logging.debug("I am a debug level log.")
# logging.info("I am a info level log.")
# logging.warning("I am a warning level log.")
# logging.error("I am a error level log.")
# logging.critical("I am a critical level log.")

# 输出全部日志
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("I am a debug level log.")
# logging.info("I am a info level log.")
# logging.warning("I am a warning level log.")
# logging.error("I am a error level log.")
# logging.critical("I am a critical level log.")

# 配置日志
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename="log1.log", level=logging.DEBUG, format=LOG_FORMAT)
# logging.debug("I am a debug level log.")
# logging.info("I am a info level log.")
# logging.warning("I am a warning level log.")
# logging.error("I am a error level log.")
# logging.critical("I am a critical level log.")

# 配置日期/时间
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename="log2.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.debug("I am a debug level log.")
logging.info("I am a info level log.")
logging.warning("I am a warning level log.")
logging.error("I am a error level log.")
logging.critical("I am a critical level log.")

# 定义一个log函数
def log(str):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H: %M:%S',
                        filename='log-selenium.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/1/7}

# 目标：获取符合要求的岗位
import xlwt
import requests
import re

# ---------------------创建一个excel文件---------------------
workBook = xlwt.Workbook(encoding="utf-8")
# ---------------------创建一个子表---------------------
workSheet = workBook.add_sheet("51job")
colName = ["岗位名称", "公司名称", "地址", "薪资", "发布时间"]
for one in range(0, len(colName)):
    # 写单元格,行编号、列编号、内容
    workSheet.write(0, one, colName[one])


# 获取页数
def get_pageNum():
    web_url = 'http://news.baidu.com/'
    resp = requests.get(web_url)
    resp.encoding = "gbk"
    pags = int(re.findall('<span class="td">共(.*?)页,到第</span>', resp.text, re.S)[0])
    return pags


for one in range(1, get_pageNum() + 1):
    # ---------------------1、构建请求---------------------
    web_url = f'http://news.baidu.com/,{one}'
    resp = requests.get(web_url)
    resp.encoding = "gbk"
    # # 查看发出去的请求头或者请求体：fiddler抓包，或者代码
    # print(resp.request.headers)
    # print(resp.request.body)
    # ---------------------2、解析响应数据---------------------
    print(resp.text)
    # ---------------------3、提取有效数据---------------------
    info = re.findall('<div class="el">(.*?)</div>', resp.text, re.S)
    # ---------------------4、存储数据---------------------
    row = 1
    for line in info:
        temp = re.findall('<a target="_blank" title="(.*?)" href', line, re.S)
        # 获取岗位名称
        jobName = temp[0].strip()
        workSheet.write(row, 0, jobName)
        # 获取公司名称
        company = temp[1].strip()
        workSheet.write(row, 1, company)
        # 获取地址
        address = re.findall('<span class="t3">(.*?)</span>', line, re.S)[0]
        workSheet.write(row, 2, address)
        # 获取薪资
        salary = re.findall('<span class="t4">(.*?)</span>', line, re.S)[0]
        workSheet.write(row, 3, salary)
        # 发布时间
        jobTime = re.findall('<span class="t5">(.*?)</span>', line, re.S)[0]
        workSheet.write(row, 4, jobTime)
        print(jobName, company, address, salary, jobTime)
        row += 1

# ---------------------保存---------------------
workBook.save("f:\\res_51jobs.xls")

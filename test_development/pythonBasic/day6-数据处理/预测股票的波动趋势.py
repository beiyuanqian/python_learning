# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/24}
"""
数据挖掘的流程：
    1、获取数据
        从固有的本地获取
        互联网动态获取
    2、存储数据
        大量数据-数据库
        部署太大数据--使用文件存储txt、excel、csv
    3、清洗数据
    4、算法的介入
    5、结果展示
    6、分析汇总·
"""
import requests
import csv
import time
import pprint
import threading
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

fo = open('股票数据.csv', mode='w', encoding='utf-8')
csv_write = csv.DictWriter(fo, fieldnames=['股票名称', '股票代码', '当前价格', '成交量'])
# 写入列名
csv_write.writeheader()
urlList = ["".format(page, round(time.time() * 1000)) for page in range(1, 3)]


def request_data(url):
    # 请求头，做一些处理防爬机制
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
    # 发送请求
    resp = requests.get(url, headers=header)
    print(resp.json())
    dataList = resp.json()['data']['list']
    print(dataList)
    pprint.pprint(dataList)
    # 3、获取你需要的数据
    for one in dataList:  # one就是一支股票
        dictTmp = {}
        # 股票名称
        dictTmp['股票名称'] = one['name']
        # 股票代码
        dictTmp['股票代码'] = one['symbol']
        # 当前价格
        dictTmp['当前价格'] = one['current']
        # 成交量
        dictTmp['成交量'] = one['volume']
        csv_write.writerow(dictTmp)


# 多线程操作爬虫
def request_threads():
    threadList = []
    for url in urlList:
        threadList.append(threading.Thread(target=request_data, args=(url,)))
    # 启动线程
    for one in threadList:
        one.start()
        time.sleep(2)
    # 阻塞
    for one in threadList:
        one.join()


# 4、数据清洗
def show_data(fileName='股票数据.csv'):
    # 从csv文件导入数据
    data_pd = pd.read_csv(fileName)
    # 剔除缺失的行
    df = data_pd.dropna()
    # 需要获取对应的数据
    df1 = df[['股票名称', '当前价格']]
    df2 = df1.iloc[:10]
    print(df2)

    # 5、算法介入-每一个操盘机构都有自己的一套规则
    # 6、展示效果：Web端
    plt.bar(df2['股票名称'].values, df2['当前价格'].values, label='股票分析结果')  # (横坐标，总=纵坐标)
    for a,b in zip(df2['股票名称'].values, df2['当前价格'].values):
        print(a,b)
        plt.text(a,b+5,b,horizontalaligment='center',verticalaligment='bottom',fontsize=10,)



    plt.xticks(rotation=-90)
    plt.xlabel('股票名称')
    plt.ylabel('当前价格')
    plt.show()


if __name__ == "__main":
    # res = request_data(urlList[0])
    # print(res)
    # request_data(urlList)
    request_threads()
    fo.close()
    show_data()

# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/9}

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    # next方法返回文件中的下一行，调用一次，只显示第一行
    header_row = next(reader)

    print(header_row)

    # # 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取日期和最高气温、最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 将日期和最高气温传递给plot(),alpha指定颜色的透明度（0完全透明，1为默认设置，完全不透明）
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 接受一个x值，两个y值系列，并填充两个y值之间的空间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    # 绘制斜的日期标签，以免彼此重叠
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()

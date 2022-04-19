# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/10}


import json
import pygal
import math

# 将数据加载到一个列表中
filename = "btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    # # 打印每一天的信息
    # date = btc_dict['date']
    # month = int(btc_dict['month'])
    # week = int(btc_dict['week'])
    # weekday = btc_dict['weekday']
    # close = int(float(btc_dict['close']))
    # print("{} is month {} week {},{}, the close price is {} RMB".format(date, month, week, weekday, close))

    # 每一天的信息
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
print(dates)

# 绘制收盘价折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价对数变换（￥）"
line_chart.x_labels = dates
# X轴坐标每隔20显示一次
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add("收盘价", close_log)
line_chart.render_to_file("收盘价对数变换折线图（￥）.svg")

from itertools import groupby


# 收盘价均值
def draw_line(x_data, y_data, title, y_lengend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_lengend, y_mean)
    line_chart.render_to_file(title + ".svg")
    return line_chart


# 收盘价月日均值
idx_month = dates.index("2017-12-01")
line_chart_month = draw_line(months[:idx_month], close[:idx_month], "收盘价月日均值（￥）", "月日均值")

# 收盘价周日均值
idx_week = dates.index("2017-12-01")
line_chart_week = draw_line(weeks[:idx_week], close[:idx_week], "收盘价周日均值（￥）", "周日均值")

# 收盘价星期均值
idx_week = dates.index("2017-12-01")
wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[:idx_week], "收盘价星期均值（￥）", "星期均值")
line_chart_weekday.x_labels = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

# 将每幅图都添加到网页中
with open("收盘价Dashboard.html", "w", encoding="utf8") as html_file:
    html_file.write('<html><head><meta charset="UTF-8"><title>收盘价Dashboard</title></head><body>\n')
    for svg in ["收盘价折线图（￥）.svg", "收盘价对数变换折线图（￥）.svg", "收盘价月日均值（￥）.svg",
                "收盘价周日均值（￥）.svg", "收盘价星期均值（￥）.svg", ]:
        html_file.write('    <object type="image/svg+xml" data="{0}" height="500"></object>\n'.format(svg))
    html_file.write("</body></html>")

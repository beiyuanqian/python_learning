# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/8}

import matplotlib.pyplot as plt
from chapter15.random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置窗口的尺寸,dpi指定屏幕分辨率，figure指定图表的宽度、高度
    plt.figure(dpi=128, figsize=(10, 6))

    # 隐藏坐标轴,在该位置才生效
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    point_numbers = list(range(rw.num_points))
    # 给点着色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors="none", s=100)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

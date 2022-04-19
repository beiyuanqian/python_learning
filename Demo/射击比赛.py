# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/4}

"""/*
给定一个射击比赛成绩单,包含多个选手若干次射击的成绩分数
请对每个选手按其最高三个分数之和进行降序排名,输出降序排名后的选手id序列
条件如下
    1. 一个选手可以有多个射击成绩的分数，且次序不固定
    2. 如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手
    3. 如果选手的成绩之和相等，则相等的选手按照其id降序排列
输入描述:
     输入第一行
         一个整数N
         表示该场比赛总共进行了N次射击
         产生N个成绩分数
         2<=N<=100

     输入第二行
       一个长度为N整数序列
       表示参与每次射击的选手id
       0<=id<=99

     输入第三行
        一个长度为N整数序列
        表示参与每次射击选手对应的成绩
        0<=成绩<=100

   输出描述:
      符合题设条件的降序排名后的选手ID序列

   示例一
      输入:
        13
        3,3,7,4,4,4,4,7,7,3,5,5,5
        53,80,68,24,39,76,66,16,100,55,53,80,55
      输出:
        5,3,7,4
      说明:
        该场射击比赛进行了13次
        参赛的选手为{3,4,5,7}
        3号选手成绩53,80,55 最高三个成绩的和为188
        4号选手成绩24,39,76,66  最高三个成绩的和为181
        5号选手成绩53,80,55  最高三个成绩的和为188
        7号选手成绩68,16,100  最高三个成绩的和为184
        比较各个选手最高3个成绩的和
        有3号=5号>7号>4号
        由于3号和5号成绩相等  且id 5>3
        所以输出5,3,7,4
"""
# 输入第一行
#          一个整数N
#          表示该场比赛总共进行了N次射击
#          产生N个成绩分数
#          2<=N<=100

# import random
#
# number_games = input("该场比赛总共进行射击的次数：")
# score_list = []
# print("参赛选手的分级分别为：", end='')
# for i in range(0, int(number_games)):
#     score_list.append(random.randint(2, 100))
#     print(score_list[i], end=", ")

"""
13
        3,3,7,4,4,4,4,7,7,3,5,5,5
        53,80,68,24,39,76,66,16,100,55,53,80,55
        3号选手成绩53,80,55 最高三个成绩的和为188"""

number_games = 15
score_list = [53, 80, 68, 24, 39, 76, 66, 16, 100, 55, 53, 80, 55, 33, 56]
id_games = [3, 3, 7, 4, 4, 4, 4, 7, 7, 3, 5, 5, 5, 2, 2]

print("该场比赛总共进行射击的次数:" + str(number_games))
print("参赛的选手id为：" + str(set(id_games)))

# 找出每个id出现的下标
dict = {}
sum_list = []
for id in list(set(id_games)):
    print("选手 " + str(id) + " 的比赛信息如下:")
    flag = 0
    lis = []
    dict_1 = {}

    for i in range(id_games.count(id)):
        sec = flag
        flag = id_games[flag:].index(id)
        lis.append(flag + sec)
        flag = lis[-1:][0] + 1
    print("  出场的次数：" + str(id_games.count(id)))
    print("  出场的顺序为：" + ', '.join(map(str, lis)))
    dict_1['number'] = id_games.count(id)
    dict_1['order'] = lis

    score = []
    for i in lis:
        score.append(score_list[i])
        # sum = sum + score_list[i]
    print("  分数分别为：" + ', '.join(map(str, score)))

    sum = 0
    if len(score) > 3:
        score.sort()
        for j in score[-3:]:
            sum = sum + j
        print("  总分数为：" + str(sum))
    elif len(score) == 3:
        for j in score[-3:]:
            sum = sum + j
        print("  总分数为：" + str(sum))
    else:
        print("  比赛次数少于3，不计入统计")

    dict_1['score'] = score
    dict_1['sum_score'] = sum
    if sum != 0:
        sum_list.append(sum)
    else:
        pass
    dict[id] = dict_1
print(dict)
sum_list.sort(reverse=True)
print(sum_list)
# 比较总分大小并排序输出

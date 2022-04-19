# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/12/28}

# def f(x):
#     result = 0
#     for i in range(1, x + 1):
#         result = result + i * i
#     return result
# 
# 
# print(f(5))


def sim_distance(prefs, person1, person2):
    si = {}
    print(prefs[person1])
    for item in prefs[person1]:
        print(item)
        if item in prefs[person2]:
            si[item] = 1
        if len(si) == 0:
            return 0
    sum_of_squares = sum(
        [pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sum_of_squares)


critics = {'Lisa Rose': {'Lady in the Water': 5.0, 'Snakes on a Plane': 5.0},
           'Toby': {'Lady in the Water': 4.0, 'Snakes on a Plane': 4.0}}
print(sim_distance(critics, 'Lisa Rose', 'Toby'))

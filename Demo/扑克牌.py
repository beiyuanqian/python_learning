# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/12/27}

def eq_lt_gt(a):
    """
    将AJQK小王大王转换为对应的数字1,11,12,13，50,99
    其他的数字转换为本身数字
    :param a:
    :return:
    """
    if a == 'J':
        a_t = 11
    elif a == 'Q':
        a_t = 12
    elif a == 'K':
        a_t = 13
    elif a == 'A':
        a_t = 1
    elif a == 'joker':
        a_t = 50
    elif a == 'JOKER':
        a_t = 99
    else:
        a_t = a
    return int(a_t)


m = []


def test1(n):
    m = n.split("-")
    print(n.split("-"))
    if "joker JOKER" in n.split("-"):
        print("最大的牌是" + "joker JOKER")
    else:
        if len(m[0]) == len(m[1]):
            if len(m[0]) == 1:
                if eq_lt_gt(m[0]) > eq_lt_gt(m[1]):
                    print("最大的牌是" + m[0])
                else:
                    print("最大的牌是" + m[1])
            else:
                if eq_lt_gt(m[0].split(" ")[0]) > eq_lt_gt(m[1].split(" ")[0]):
                    print("最大的牌是" + m[0])
                else:
                    print("最大的牌是" + m[1])
        else:
            if len(m[0]) == 4:
                print("最大的牌是" + n.split("-")[0])
            else:
                print("最大的牌是" + n.split("-")[1])


test1("2-J J J J")
test1("4 4-J J J J")
test1("J J J J-joker JOKER")
test1("3 3-Q Q")
test1("5 5 5-3 3 3 3")
test1("K-joker")

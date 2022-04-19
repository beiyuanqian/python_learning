# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/13}


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

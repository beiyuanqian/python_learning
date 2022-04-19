# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/13}


# ================================= 8.3返回值 =================================
# 8.3.1返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# 8.3.2让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)


# 为让中间名变为可选的，可给形参middle_name指定一个默认值——空字符串
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "lee", "hooker")
print(musician)


# 8.3.3返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)


def build_person(first_name, last_name, age=""):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)


# 8.3.4结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == "q":
        break
    l_name = input("Last name")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# ================================= 8.4传递列表 =================================
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 8.4.1在函数中修改列表
def print_models(unprinted_designs, completed_models):
    # 模拟打印每个设计，直到没有未打印的设计为止，打印每个设计后，都将其移到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # 显示打印好的所有模型
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.4.2禁止函数修改列表，切片表示法[:]创建列表的副本
print_models(unprinted_designs[:], completed_models)


# ================================= 8.5传递任意数量的实参 =================================
# 形参名*toppings中的*号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 对配料表进行遍历
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 8.5.1结合使用位置实参和任意数量实参
# 如果函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# 8.5.2使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('alert', 'einstein', location='princeton', field='physics')
print(user_profile)

# ================================= 8.6将函数存储在模块中 =================================
# 8.6.1导入整个模块
import chapter8.pizza

chapter8.pizza.make_pizza(16, "pepperoni")
chapter8.pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.2导入特定的函数
# 导入模块中的特定函数
# from module_name import function_name
# 逗号分割函数名，导入任意数量的函数
# from module_name import function_0, function_1, function_2
from chapter8.pizza import make_pizza

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.3使用as给函数指定别名
from chapter8.pizza import make_pizza as mp

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.4使用as给模块指定别名
import chapter8.pizza as mp

mp.make_pizza(16, "pepperoni")
mp.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.5导入模块中的所有函数
from chapter8.pizza import *

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

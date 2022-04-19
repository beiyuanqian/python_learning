# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/14}

# ================================= 10.1从文件中读取数据 =================================
"""读取文件时，python将其中的所有文本都解读为字符串"""
# 10.1.1读取整个文件
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    # rstrip()删除字符串末尾的空白
    print(contents.rstrip())

# 10.1.3逐行读取
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 10.1.4创建一个包含文件各行内容的列表
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 10.1.5使用文件的内容
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# 10.1.6包含100万位的大型文件
print(pi_string[:52] + "...")

# 10.1.7圆周率包含你的生日吗
filename = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in zhe first million digits of pi!")
else:
    print("Your birthday does not appear ")

# ================================= 10.2写入文件 =================================
# 10.2.1写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!")

# 10.2.2写入多行
filename = 'programming_1.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3附加到文件a
filename = 'programming_1.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# ================================= 10.3异常 =================================
# 10.3.2使用try-except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero")

# 10.3.3使用异常避免崩溃
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == "q":
#         break
#     second_number = input("Second number:")
#     if second_number == "q":
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# 10.3.4else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == "q":
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 10.3.5处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# 10.3.6分析文本
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


# 10.3.7使用多个文件
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算一个文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# 10.3.8失败时一声不吭，使用pass
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass

# ================================= 10.4存储数据 =================================
# 10.4.1使用json.dump()和json.load()
"""
json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
json.load()将数据读取到内存中
"""
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

# 10.4.2保存和读取用户生成的数据
# import json
#
# filename = "username.json"
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What's your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

# 10.4.3重构
import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w')as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()

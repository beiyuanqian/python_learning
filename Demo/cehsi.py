# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/6}

info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '北京'}
age = info.get('age')
print(age)
age = info.get('age', 18)
print(age)

k = 1000
while k > 1:
    print(k)
    k = k / 2

lists = [1, 2, 3, 4]
tmp = 0
for i, j in enumerate(lists):
    tmp += i * j
print(tmp)

str1 = "exam is a example!"
str2 = "exam"
print(str1.find(str2, 7))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1::2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_odd(n):
    return n % 2 == 0


print(list(filter(is_odd, a)))

list = [8764.95, 8217.67, 11220.13, 8910.67, 8997.63, 9180.47, 8613.73, 8491.72, 9205.42, 8393.53, 9318.32, 9979.41,
        9448.42]
sum = 0
for i in range(0, len(list)):
    sum = sum + list[i]
print(sum)
print(sum / len(list))

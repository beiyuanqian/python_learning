# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/9}

"""
# 将字符转为整数表示，只接受一个字符
print(ord("刘"))
# 将整数表示转为字符
print(chr(65+32))
"""

"""
a = "abc"
b = b"abc"
print(type(a))
print(type(b))

# str和bytes互转
a = "自君之出矣，不复理残机"
b = a.encode("gbk")  # 把str转成bytes
print(b)
c = b.decode("gbk")  # 把bytes转为str
print(c)
"""

with open("a.txt", "w", encoding="gb2312") as f:
    f.write("何路向家园,历历残山剩水")
with open("a.txt", "r", encoding="gb2312") as f:
    data = f.read()
    print(data)
with open("1.png", "rb") as f:
    data = f.read()
with open("2.png", "wb") as f:
    f.write(data)
with open("b.txt", "wb") as f:
    f.write(b"abc")



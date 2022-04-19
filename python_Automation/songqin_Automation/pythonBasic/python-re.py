# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/7}

# 正则表达式
import re

# .表示通配符--除换行符之外的符号，返回一个元素
str1 = "songqin"
# 查找所有符合要求的内容，有时候不止一个，返回值为list
# re.findall(“正则表达式”，需要处理的字符串)
res = re.findall('s..', str1)
print(res)

# *表示前面元素出现过0次或n次
str1 = "songqins"
res = re.findall('so*', str1)
print(res)

# +表示前面元素出现过1次或n次
str1 = "songqinso"
res = re.findall('so.+', str1)
print(res)

# ?组合用法(.+?)
str1 = "a1111b"
res = re.findall('a(.*?)b', str1)
print(res)

# \w,匹配字母数字及下划线-一个元素
str1 = "songqin*ab"
res = re.findall('\w{3}', str1)  # 3个连续的元素
print(res)

# \W,匹配非字母数字及下划线
str1 = "songqin*ab###"
res = re.findall('\W{3}', str1)
print(res)

# \S,匹配任意非空字符
str1 = "songqin*ab###"
res = re.findall('\S', str1)
print(res)

# \d,匹配任意数字
str1 = "abc1234587dg4gf"
res = re.findall('\d.+\d', str1)
print(res)

# \D,匹配任意非数字
str1 = "abc1234587dg4gf"
res = re.findall('\D', str1)
print(res)

#re.I--表示大小写不敏感
str1 = "songqinS\n"
res = re.findall('s.', str1,re.I|re.S)
print(res)
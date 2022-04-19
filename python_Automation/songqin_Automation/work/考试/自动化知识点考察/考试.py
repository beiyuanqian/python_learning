# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/7/3}

# 1、用if语句判断字符串变量var的长度是否大于10，并且其中是否包含'ok'，如果两个条件都满足，就打印ok
var = "sddfgergfd vcxgokbfd"
if len(var) > 10 and "ok" in var:
    print("OK")
else:
    print("NO")

# 2、for循环 写一段代码打印其中所有包含ok的字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
for i in range(0, len(info)):
    if "ok" in info[i]:
        print(info[i])
# 3、用while 循环 写一段代码打印其中所有包含ok的字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
i = 0
while i < len(info):
    if "ok" in info[i]:
        print(info[i])
    i = i + 1


# 4、把参数字符串倒序返回，请补全代码，完成功能,下面的程序用来将字符串倒序，

def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()

    return ''.join(tmp)


print(reverseStr('hello'))

# 5、用一行代码，得到其中的年龄数字，不要数索引
info = '姓名=小王&年龄=16&身高=175'
print(info.split("&")[1].split("=")[1])

# 6、用一行代码，打印出如下格式的字符串，姓名=xx&年龄=xx&身高=xx
name = '小明'
age = 16
height = 170






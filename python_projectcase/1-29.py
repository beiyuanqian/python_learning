# read()方法读取全部内容
hellofile = open(r"D:\PYproject\python_projectcase\Hello")
fileContent = hellofile.read()
hellofile.close()
print(fileContent)

# 设置最大读入字符来限制read()函数一次返回的大小
hellofile = open(r"D:\PYproject\python_projectcase\Hello")
fileContent = ""
while True:
    fragment = hellofile.read(3)
    if fragment == "":
        break
    fileContent += fragment

hellofile.close()
print(fileContent)

# readline()方法从文件中获取一个字符串，每个字符串就是文件的每一行
hellofile = open(r"D:\PYproject\python_projectcase\Hello")
fileContent = ""
while True:
    line = hellofile.readline()
    # print("每一行",line)
    if line == "":
        break
    fileContent += line
hellofile.close()
print(fileContent)

# readlines()方法返回字符串列表，每一项是文件中每一行的字符串
hellofile = open(r"D:\PYproject\python_projectcase\Hello")
fileContent = hellofile.readlines()
hellofile.close()
print(fileContent)

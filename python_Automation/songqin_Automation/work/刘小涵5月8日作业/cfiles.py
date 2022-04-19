# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/30}

utf8Path = "D:\PYproject\\test\work\刘小涵5月8日作业\python进阶测试-作业2-字符编码集-task07\cfiles\\utf8编码.txt"
gbkPath = "D:\PYproject\\test\work\刘小涵5月8日作业\python进阶测试-作业2-字符编码集-task07\cfiles\gbk编码.txt"

newStr = ""
with open(utf8Path, "r", encoding="utf8") as f:
    newStr += f.read()
newStr += "\n"
with open(gbkPath, "r", encoding="gbk") as f:
    newStr += f.read()
print(newStr)

fileName = input("请输入>>>")
with open("./%s" % fileName,"w", encoding="utf8") as f:
    f.write(newStr)



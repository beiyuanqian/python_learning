# author:刘小涵  time:2020/4/6
"""
1、可以根据标签名称选择
2、.代表当前目录
3、..代表上层目录，即父目录
4、@ 选取元素属性
5、/ 相当于css中的 > ;也相当于顶层目录
6、//相当于css中的空格，后代元素选择器
7、下标选择和Python的列表下标操作相同，但是从1开始计算
8、* 代表通配符，可以匹配所有类型的标签
"""
"""
1、parent 选取当前节点的父节点
//*[@id="kwdselectid"]/parent::p
//*[@id="kwdselectid"]/..
2、descendant 后代选择
//*[@id="kwdselectid"]/../../descendant::li
//*[@id="kwdselectid"]/../..//li
3、ancestor 先辈（父、祖父）
//*[@id="kwdselectid"]//ancestor::div
4、ancestor-or-self 选取当前节点的所有先辈元素，并且包括自己
//*[@id="kwdselectid"]//ancestor-or-self::p
5、following-sibling 后续兄弟选择器
/html/body/div[3]/div/div[1]/p[1]/a/following-sibling::a
6、following 选中当前节点的结束标签之后的所有节点（不包括自己及后代）
/html/body/div[3]/div/div[1]/p[1]/a/following::a
7、preceding 选取文档中当前节点开始标签之前的所有节点
//*[@id='kwdselectid']/preceding::ul
8、preceding-sibling 前续兄弟选择器（当前节点前的所有节点）
//*[@id='searchHistory']/span[4]/preceding-sibling::span
"""
from selenium import webdriver
driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
driver.get('http://www.51job.com')

# ele=driver.find_element_by_xpath('/html/body/div[3]/div')
# ele.find_element_by_xpath('./div/div/div/p/input').send_keys("200")
# 相对路径的./可以省略，如./a,a，打印出来一样，..代表上层目录
ele=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]')
# aSli=ele.find_elements_by_xpath('a')
# aSli=ele.find_elements_by_xpath('./a')
# print(len(aSli))
aSli=ele.find_element_by_xpath('./..').text
print(aSli)
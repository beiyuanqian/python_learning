# author:刘小涵  time:2020/3/27

"""
iframe，又叫浮动帧标记，是内嵌的网页元素，可以将一个html文件嵌入到另一个html文件中显示
对iframe进行操作，需要用到以下三种方法：
switch_to_iframe()                       切换到iframe上
switch_to.frame()                         切换到iframe上
switch_to.default_content()         切换回原主页面
通过如下方式进行切换操作
定位到iframe
iframe=driver.find_element_by_id("x-URS-iframe")
切换到iframe
driver.switch_to_frame(iframe)
"""

from selenium import webdriver

driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
driver.get("E:\PyProgram\\test\selenium\day3\\test.html")

# 找到嵌套元素
iframe = driver.find_element_by_id("abd")
# 切入嵌套元素
driver.switch_to.frame(iframe)
driver.find_element_by_id("kw").send_keys("web")

"""
# 隐式等待
driver.implicitly_wait(5)
# 对iframe进行操作，需要用到以下三种方法：
# 切换到iframe上,未来会被弃用，不建议使用
driver.switch_to_iframe()
# 切换到iframe上                  
driver.switch_to.frame()
# 切换回原主页面                       
driver.switch_to.default_content()
"""

"""
元素定位失败的原因：
1、表达式写的不对
2、元素未加载
3、元素不可见
4、iframe标签的使用
"""

# iframe = driver.find_element_by_id("f91fb5bc-bd95-45bf-bd77-977a2afbd25f")
# driver.switch_to.frame(iframe)
# driver.find_element_by_id("e4890ded-16e1-4445-bf8e-7f655793f332").send_keys("haha")

# time.sleep(5)
# driver.quit()

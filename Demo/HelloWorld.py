
# def mySort(alist,blist):
#     for i in range(0,len(alist)-1):
#         for j in range(0,len(alist)-1-i):  #依次找出最大值，并
#             if alist[j]<alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],alist[j]
#         blist.append(alist[len(alist)-1-i])  #把最大值
#     blist.append(alist[0])
#     print(blist)
#
# mySort(alist=[1,3,5,7,34,23,55,56,2,3,4],blist=[])
#
# for i in range(1,10):
#     for j in range(1,10):
#         print('{0}*{1}={2}'.format(i,j,i*j))
#     print('\n')

# nameList=['Mike','Jack','Mary']
# i=0
# while i <= len(nameList)-1:
#     print(nameList[i])
#     i+=1
# dict={'name':'Jack','age':12}
# print(dict.items())
# for a,b in dict.items():
#     print(a,b)

# def func(a,*args,b=2):
#     print(a,args,b)
# func(1,2,3,4,b=100)

# def func(a,**kargs):
#     print(a,kargs)
# dict={'name':'Jack','age':18}
# func(10,**dict)
# print(10,**dict)

# a=[1,2,3,4,5]
# print(*a)
# dict={'name':'Jack','age':18}
# print(**dict)

# def favorite_book(title):
#     print('One of my favorite books is '+title)
# favorite_book('Alice in Wonderful')

# def display_message(message):
#     print('我学到了'+message)
# display_message('func')

# def make_skirt(size='L',style='I Love Python'):
#     print("This shirt's size is",size)
#     print("This shirt's style is “",style,'"')
# make_skirt()
# make_skirt("M")
# make_skirt(style='ABC')

# def describe_city(city,country='china'):
#     print(city.title(),'is in',country.title())
# describe_city("beijing")
# describe_city('shanghai')
# describe_city('london','UK')

# message=input("请输入车的品牌： ")
# print("Let me see if I can find you a",message.title())

# message=input('Please enter the number of diners: ')
# if int(message)>8:
#     print('There is no empty table')
# else:
#     print('Have a free table, please')

# number=input('Please enter a number: ')
# if int(number) % 10==0:
#     print("It's an integer multiple of 10")
# else:
#     print("It's not an integer multiple of 10"

# current_number=0
# while current_number<100:
#     current_number+=1
#     if current_number%2==0:
#         continue
#     else:
#         print(current_number)

# print('Please enter the pizza toppings you want to add: ')
# active=True
# while active:
#     message=input()
#     if message=='quit':
#         active=False
#     else:
#         print("We're going to add "+message.title()+" to the pizza")

# active=True
# while active:
#     age=input("Please enter your age:")
#     if age=='quit':
#         active=False
#     else:
#         if int(age)<=3:
#             print("The price of the ticket is 0")
#         elif int(age)<=12:
#             print("The price of the ticket is 10")
#         elif int(age)>12:
#             print("The price of the ticket is 15")

# responses={}
# active=True
# while active:
#     message=input("Would you like to response this question? (yes/no)")
#     if message=='no':
#         active=False
#     elif message=='yes':
#         name=input('What is your name?' )
#         response=input('Which mountain would you like to climb someday? ')
#         responses[name.title()]=response.title()
#     else:
#         print("Error")
# print(responses)
# for name,response in responses.items():
#     print(name.title(),"would like to climb ",response.title())

# sandwich_orders=['tuna sandwich','pastrami','rutn sandwich','pastrami','pastrami','gduunn sandwich']
# finished_orders=[]
# while sandwich_orders:
#     sandwich_order=sandwich_orders.pop()
#     print("I made your " + sandwich_order)
#     finished_orders.append(sandwich_order)
# print(finished_orders)
# print(sandwich_orders)

# print("五香烟熏牛肉卖完了")
# sandwich_orders=['tuna sandwich','pastrami','rutn sandwich','pastrami','pastrami','gduunn sandwich']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化属性restaurant_name和cuisine_type（烹饪类型）"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#
#     def describe_restaurant(self):
#         print("This restaurant's name is "+self.restaurant_name)
#         print("This restaurant's type is "+self.cuisine_type)
#
#     def open_reataurant(self):
#         print("The restaurant is open.\n")
#
# restaurant_1=Restaurant('老灶台火锅店','重庆风味麻辣火锅')
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()
#
# restaurant_1=Restaurant('愿者上钩纸包鱼','麻辣风味')
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()
#
# restaurant_1=Restaurant('一烧一烤','锦州特色烧烤')
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()

# class User():
#     def __init__(self,first_name,last_name,age,gender,adress):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.gender=gender
#         self.adress=adress
#     def describe_user(self):
#         print("This user's name is "+self.first_name+" "+self.last_name+".")
#         print("This user's age is "+self.age+", and the gender is "+self.gender+".")
#         print("The adress is "+self.adress+".")
#     def greet_user(self):
#         print(self.first_name+" "+self.last_name+", you are welcome to use this system.\n")
#
# user=User("刘","小涵",'25',"女","珠海市")
# user.describe_user()
# user.greet_user()
#
# user=User("魏","生平",'25',"男","北京市")
# user.describe_user()
# user.greet_user()
#
# user=User("王","月盈",'23',"女","沈阳市")
# user.describe_user()
# user.greet_user()

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化属性restaurant_name和cuisine_type（烹饪类型）"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         print("This restaurant's name is "+self.restaurant_name+", type is "+self.cuisine_type)
#         # print("The number of people already eating is "+str(self.number_served))
#
#     def open_reataurant(self):
#         print("The restaurant is open.")
#
#     def set_number_served(self,number_served):
#         self.number_served=number_served
#
#     def read_number_served(self):
#         print("The number of people already eating is " + str(self.number_served))
#
#     def increment_number_served(self,number_served):
#         self.number_served+=number_served
#         # print("Now,The number of people already eating is " + str(self.number_served))
#
#
#
# restaurant_1=Restaurant('老灶台火锅店','重庆风味麻辣火锅')
# # restaurant_1.number_served=10 #直接修改属性的值
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()
# restaurant_1.set_number_served(20)#通过方法修改属性的值
# restaurant_1.read_number_served()
# restaurant_1.increment_number_served(5)
# restaurant_1.read_number_served()

# restaurant_1=Restaurant('愿者上钩纸包鱼','麻辣风味')
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()
#
# restaurant_1=Restaurant('一烧一烤','锦州特色烧烤')
# restaurant_1.describe_restaurant()
# restaurant_1.open_reataurant()

# class User():
#     def __init__(self,first_name,last_name,age,gender,adress):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.gender=gender
#         self.adress=adress
#         self.login_attempts=0
#
#     def describe_user(self):
#         print("This user's name is "+self.first_name+" "+self.last_name+".")
#         print("This user's age is "+self.age+", and the gender is "+self.gender+".")
#         print("The adress is "+self.adress+".")
#
#     def greet_user(self):
#         print(self.first_name+" "+self.last_name+", you are welcome to use this system.")
#
#     def read_login_attempts(self):
#         print("The number of login_attempts are "+str(self.login_attempts))
#
#     def increment_login_attempts(self):
#         self.login_attempts+=1
#
#     def reset_login_attempts(self):
#         self.login_attempts=0
#
# user=User("刘","小涵",'25',"女","珠海市")
# user.describe_user()
# user.greet_user()
#
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.read_login_attempts()
#
# user.reset_login_attempts()
# user.read_login_attempts()


# from selenium import webdriver
# import time
# driver=webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
# driver.get("http://www.baidu.com")
# time.sleep(5)
# driver.quit()

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
# driver.get("https://m.weibo.cn/")
#
# # 找到搜索输入框并点击
# driver.find_element_by_class_name("m-search").click()
# time.sleep(1)
# # 找到 热搜榜所在大标签 card m-panel card16 m-col-2
# hotSearchEle = driver.find_element_by_class_name("m-col-2")
# # 在大标签中匹配热搜列表 m-item-box
# hotSearchSli = hotSearchEle.find_elements_by_class_name("m-item-box")
# # 取列表的最后一个元素,即微博热搜榜,并点击
# hotSearchSli[-1].click()
# time.sleep(1)
# # 找到 实时热点，每分钟更新一次
# hotSli = driver.find_element_by_css_selector(
#     "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div")
# # 从 hotSli 中找到 card m-panel card4 标签列表, 即每一行热搜标签
# hotDivSli = hotSli.find_elements_by_class_name("card4")
# # 迭代 hotSli 中的每一个 div 标签  # 注: 第一个置顶的热搜不是每分钟更新一次, 每次刷新都可能不一样
# for hotDiv in hotDivSli:
#     # 判断这一行热搜有没有图片标签
#     iconSli = hotDiv.find_elements_by_class_name("m-link-icon")
#     if iconSli:  # 如果有图片标签
#         # 获取 img 标签
#         img = iconSli[0].find_element_by_tag_name("img")
#         # 获取 src 属性
#         srcLink = img.get_attribute("src")
#         # 判断类型是 hot 还是 new 还是 fei
#         if "hot" in srcLink:
#             hotType = "热"
#             # 获取热搜文本
#             hotText = hotDiv.find_element_by_class_name("m-text-cut").text
#             print("{}: {}".format(hotType, hotText))
#         elif "new" in srcLink:
#             hotType = "新"
#             # 获取热搜文本
#             hotText = hotDiv.find_element_by_class_name("m-text-cut").text
#             print("{}: {}".format(hotType, hotText))
#         elif "fei" in srcLink:
#             hotType = "沸"
#             # 获取热搜文本
#             hotText = hotDiv.find_element_by_class_name("m-text-cut").text
#             print("{}: {}".format(hotType, hotText))
#
# time.sleep(5)
# driver.quit()


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
# driver.implicitly_wait(10)
# driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
#
# #设置全屏显示#设置全屏显示
# driver.maximize_window()
# # 出发城市写南京南
# startCity = driver.find_element_by_id("fromStationText")
# startCity.click()
# startCity.clear()
# startCity.send_keys("南京南\n")
#
# # 目的地写杭州东
# targetCity = driver.find_element_by_id("toStationText")
# targetCity.click()
# targetCity.clear()
# targetCity.send_keys("杭州东\n")
#
# # 发车时间 选 06:00--12:00
# Select(driver.find_element_by_id("cc_start_time")).select_by_visible_text("06:00--12:00")
#
# # 发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
# driver.find_element_by_css_selector("#sear-sel > div > ul > li:nth-child(2)").click()
#
# # # 获取所有的二等座元素
# # secondSeatSli = driver.find_elements_by_css_selector("#queryLeftTable td:nth-child(4)")
# # 获取所有的车次信息
# trainSli = driver.find_elements_by_css_selector("#queryLeftTable > tr[class]")
# # # 迭代列表
# # for train in trainSli:
# #     # 获取本车次的二等座信息
# #     secondSeat = train.find_elements_by_css_selector("td")[3]
# #     # secondSeat = train.find_element_by_css_selector("td:nth-child(4)")
# #     # 二等座无票, 则跳过
# #     if secondSeat.text in ["无", "--", "候补"]:
# #         continue
# #     # 有票, 获取 车次
# #     print(train.find_element_by_css_selector("a[title=\"点击查看停靠站信息\"]").text)
#
# driver.quit()



class numToCH():

    def __init__(self, num):
        dict1 = {'2': '拾', '3': '佰', '4': '仟'}
        dict2 = {'0': '零', '1': '壹', '2': '貳', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}

        self.num = num
        self.dict1 = dict1
        self.dict2 = dict2

    def thouHundTen(self, numstr):
        ch = ''
        a = 0
        for x in numstr:
            num_length = len(numstr)
            if len(str(self.num)) == 1:
                ch += self.dict2[x]
            elif len(numstr) == 1 and int(numstr) != 0:
                ch += self.dict2[x]
            elif int(numstr) == 0:
                ch += ''
            elif x == '0' and a == 0:
                a += 1
                ch += self.dict2[x]
            elif x == '0' and a != 0:
                a += 1
                ch += ''
            elif str(num_length) in self.dict1.keys():
                ch += self.dict2[x] + self.dict1['%d' % num_length]
            numstr = numstr[(numstr.index(x) + 1):]
        return ch

    def convert(self):
        conv_result = ''
        onumstr = str(self.num)
        if len(onumstr) > 4:
            numstr = onumstr[:-4]
            conv_result += self.thouHundTen(numstr) + "萬"
            numstr = onumstr[-4:]
            conv_result += self.thouHundTen(numstr)
        else:
            conv_result += self.thouHundTen(onumstr)
        return conv_result


if __name__ == '__main__':
    a = numToCH(1)
    print(a.convert())
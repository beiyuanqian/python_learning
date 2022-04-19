# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/14}

# ================================= 9.4导入类 =================================
# 9.4.1导入单个类
from chapter9.car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 9.4.2在一个模块中存储多个类
from chapter9.car import ElectricCar

my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.4.3从一个模块中导入多个类
from chapter9.car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 9.4.4导入整个模块
import chapter9.car
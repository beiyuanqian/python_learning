# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/13}


# ================================= 9.1创建和使用类 =================================
# 9.1.1创建Dog类
class Dog():
    # 一次模拟小狗的简单尝试

    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + " rolled over")


# 9.1.2根据类创建实例
my_dog = Dog('willie', 6)

# 访问属性使用句点表示法，如my_dog.name
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old\n")

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()


# 练习
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nUser's name is " + self.first_name.title() + " " + self.last_name)

    def greet_uesr(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name)


user_1 = User("jimi", "hendrix")
user_1.describe_user()
user_1.greet_uesr()


# ================================= 9.2使用类和实例 =================================
# 9.2.1Car类
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


# 9.2.2给属性指定默认值
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3修改属性的值
# 直接修改属性的值，通过实例直接访问它
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 通过方法修改属性的值
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odemeter(self, mileage):
        # 将里程表读数设置为指定值
        self.odometer_reading = mileage
        # # 将里程表读数设置为指定值，禁止将里程表读数往回调
        # if mileage >= self.odometer_reading:
        #     self.odometer_reading = mileage
        # else:
        #     print("You can't roll back an odometer!")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odemeter(23)
my_new_car.read_odometer()


# 通过方法对属性的值进行递增
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odemeter(self, mileage):
        # 将里程表读数设置为指定值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odemeter(self, miles):
        # 将里程表读数设置为指定值
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odemeter(23)
my_new_car.read_odometer()
my_new_car.increment_odemeter(5)
my_new_car.read_odometer()


# 练习
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\nUser's name is " + self.first_name.title() + " " + self.last_name)

    def greet_uesr(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("登录次数为：" + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("重置登录次数为0.")


user_1 = User("jimi", "hendrix", 0)
user_1.describe_user()
user_1.greet_uesr()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.increment_login_attempts()


# ================================= 9.3继承 =================================
# 9.3.1子类的方法__init__()
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odemeter(self, mileage):
        # 将里程表读数设置为指定值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odemeter(self, miles):
        # 将里程表读数设置为指定值
        self.odometer_reading += miles


class ElectricCar(Car):
    # 电动汽车的独特之处
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)


my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())


# 9.3.3给子类定义属性和方法
class Car():
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = "\n" + str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odemeter(self, mileage):
        # 将里程表读数设置为指定值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odemeter(self, miles):
        # 将里程表读数设置为指定值
        self.odometer_reading += miles


class ElectricCar(Car):
    # 电动汽车的独特之处
    def __init__(self, make, model, year):
        # 初始化父类的属性，再初始化电动车特有的属性
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery.\n")


my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 9.3.4重写父类的方法，如果Car类中有一个名为fill_gas_tank()的方法，重写方法如下
# class ElectricCar(Car):
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank!")


# 9.3.5将实例用作属性
class Battery():
    def __init__(self, battery_size=20):
        self.battery_size = battery_size

    def describe_battery(self):
        print("+This car has a " + str(self.battery_size) + "-KWH battery.")


class ElectricCar(Car):
    # 电动汽车的独特之处
    def __init__(self, make, model, year):
        # 初始化父类的属性，再初始化电动车特有的属性
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("+This car has a " + str(self.battery_size) + "-KWH battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge"
        print(message)


my_tesla = ElectricCar('audi', 'a4', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

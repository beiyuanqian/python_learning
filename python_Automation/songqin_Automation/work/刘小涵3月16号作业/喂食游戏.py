'''
动物园里面有10个房间，房间号从1 到 10。
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。
如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 
游戏3分钟结束后，显示每个房间的动物和它们的体重
实现过程中，有什么问题，请通过课堂上讲解的调试方法，尽量自己发现错误原因。
'''''
class Tiger():
    classname='tiger'
    def __init__(self,weight=200):
        self.weight=weight
    def roar(self):
        print('Wow!!')
        self.weight-=5

    def feed(self, food):
        if food == 'meat':
            self.weight += 10
            print('恭喜你，Tiger的体重加10斤')
        else:
            self.weight -= 10
            print('Sorry，Tiger的体重减10斤')

class Sheep():
    classname='sheep'

    def __init__(self, weight=100):
        self.weight = weight

    def roar(self):
        print('mie~')
        self.weight -= 5

    def feed(self, food):
        if food == 'grass':
            self.weight += 10
            print('恭喜你，Sheep的体重加10斤')
        else:
            self.weight -= 10
            print('Sorry，Sheep的体重减10斤')
class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal

from random import randint
import time
rooms = []
for no in range(10):
    if randint(0,1):
        ani = Tiger(200)
    else:
        ani = Sheep(100)

    room = Room(no,ani)
    rooms.append(room)

startTime = time.time()
while True:
    curTime = time.time()
    if (curTime - startTime) > 120:
        print('\n\n **********  游戏结束 ********** \n\n')
        for idx, room in enumerate(rooms):
            print('房间 :%s' % (idx + 1), room.animal.classname, room.animal.weight)
        break


    roomno = randint(1, 10)
    room = rooms[roomno-1]  # why -1 ?
    ch = input('我们来到了房间# %s, 要敲门吗?[y/n]' % roomno)
    if ch == 'y':
        room.animal.roar()

    food = input('请给房间里面的动物喂食:')
    room.animal.feed(food.strip())


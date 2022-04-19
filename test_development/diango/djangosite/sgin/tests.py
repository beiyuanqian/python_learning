from django.test import TestCase
from sgin.models import Event, Guest
from datetime import datetime


# Create your tests here.
# 发布会测试，创建临时数据库，不会对真实数据产生影响
class EventTestCase(TestCase):
    def setUp(self) -> None:
        # 测试前置--准备测试数据
        Event.objects.create(name="测开训练营1", address="软件大道23号", start_time=datetime.utcnow(), limits=1000)
        Event.objects.create(name="测开训练营2", address="花神大道23号", start_time=datetime.utcnow(), limits=500)

    def test_event_address(self):
        # 获取发布会
        event1 = Event.objects.get(name="测开训练营1")
        event2 = Event.objects.get(name="测开训练营2")
        # 校验地址
        self.assertEqual(event1.address, "软件大道23号")  # unitest内置断言方法
        self.assertEqual(event2.address, "花神大道23号")
        # assert event2.address == "花神大道23号"  # python关键字断言法

    def test_address_update(self):
        event1 = Event.objects.get(name="测开训练营1")
        event1.address = "软件大道24号"  # 更新步骤1，赋值
        event1.save()  # 更新步骤2，保存修改
        self.assertEqual(event1.address, "软件大道24号")

    def test_delete(self):
        # 删除之前列出结果
        event_list_before = Event.objects.all()
        event1 = Event.objects.get(name="测开训练营1")
        # 删除之前数据在列表里
        self.assertIn(event1, event_list_before)
        event1.delete()
        # 删除之后列出结果
        event_list_after = Event.objects.all()
        # 删除之后数据不在列表里
        self.assertNotEqual(event1, event_list_after)


class GuestTestCase(TestCase):
    # None表示没有返回值
    def setUp(self) -> None:
        # 创建嘉宾需要关联发布会
        self.event = Event.objects.create(name="测开训练营1", address="软件大道23号", start_time=datetime.utcnow(),
                                          limits=1000)
        Guest.objects.create(name="小Q", phone='13245678998', email='123@123.com', event=self.event)

    def test_update(self):
        guest = Guest.objects.get(name='小Q')
        # 更改名称
        guest.name = "小Z"
        guest.save()
        # 校验名称是否等于修改后的名称
        self.assertEqual(guest.name, "小Z")
        # 根据修改后的名称查询嘉宾
        guest2 = Guest.objects.get(name='小Z')
        self.assertEqual(guest, guest2)

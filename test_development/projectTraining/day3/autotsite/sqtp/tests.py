from multiprocessing import Value

from django.test import TestCase

# Create your tests here.
from .models import Step, Suite, Config, Case, Request


class TestRelateQuery(TestCase):
    def setUp(self) -> None:
        # 创建套件和用例
        self.config = Config.objects.create(name="用例1")
        self.case = Case.objects.create(config=self.config)
        self.suite_conf = Config.objects.create(name='套件1')
        self.suite = Suite.objects.create(config=self.suite_conf)

    def test_case_suite(self):
        self.case.suite = self.suite  # 用例关联套件
        self.case.save()  # 保存数据库
        print(self.case.suite)  # 正向查询-查询所属的套件
        print(self.case.config)  # 正向查询-查询配置
        # 未指定related_name的反向查询
        # 反向查询-多对一同多对多
        print(self.suite.case_set.all().filter())  # 套件查询关联的用例-Queryset
        # 反向查询-一对一
        print(self.config.case)  # 配置对应的用例-数据对象，反向关系模型小写

    def test_step_case(self):
        self.step = Step.objects.create(belong_case=self.case, name='步骤1')
        # 指定related_name的反向查询
        print(self.case.teststeps.all())

    def test_step_request(self):
        self.step = Step.objects.create(belong_case=self.case, name='步骤1')
        # 创建request数据
        self.request = Request.objects.create(url='/demo/example', step=self.step)
        # 1对1关系-反向查询-
        print(self.step.testrequest)


# json操作测试
class TestJsonOperate(TestCase):
    def test_add(self):
        req1 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing'})
        print(req1.data)
        req2 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing'})
        print(req2.data)

    def test_update(self):
        # req1 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing'})
        # # 整体修改
        # req1.data = {'city': 'beijing'}
        # req1.save()
        # print(req1.data)

        # # 局部修改
        # req1.data['name'] = '小红'
        # req1.save()
        # print(req1.data)

        req1 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing',
                                                          'father': {'name': 'xiaogang', 'age': 40}})
        req1.data['father']['age'] = 45
        req1.save()
        print(req1.data)

    def test_delete(self):
        # 删除整体
        req1 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing',
                                                          'father': {'name': 'xiaogang', 'age': 40}})
        # req1.data = None  # sql的none
        # req1.save()
        # res=Request.objects.filter(data__isnull=True) # 查询的时候关系字段等于sql的null
        # print(req1.data)

        req1.data = Value('null')  # json的none
        req1.save()
        res = Request.objects.filter(data=None)  # 查询的时候关系字段等于json的null
        print(req1)

    def test_query(self):
        print('===查询测试=====')
        req1 = Request.objects.create(url='/demo1', data={'name': '小明', 'age': 18, 'addr': 'nanjing',
                                                          'father': {'name': 'xiaogang', 'age': 40}})
        res = Request.objects.filter(data__age=18)
        # res = Request.objects.filter(data__father__age=18)
        print(res)

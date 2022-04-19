from django.db import models


# Create your models here.
class Event(models.Model):
    # 发布会名称 字符串 最大长度256 非空,null=True代表允许为空，默认为false
    name = models.CharField(max_length=256, verbose_name='发布会名称', unique=True)
    # name = models.CharField('发布会名称',max_length=256)
    # 发布会地点 字符串 最大长度256 非空,
    address = models.CharField('发布会地点', max_length=256)
    # 发布会人数 整形 默认为100
    limits = models.IntegerField('发布会人数', default=100)
    # 发布会状态 布尔类型 默认为True
    status = models.BooleanField('发布会状态', default=True)
    # 开始时间 日期时间类型,python的datetime.datetime的实例
    start_time = models.DateTimeField('开始时间', auto_now_add=True)

    # 修改对象显示信息
    def __str__(self):
        return self.name


# 嘉宾
class Guest(models.Model):
    # 关联发布会
    # # 外键的定义方式（多对一）
    # event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, verbose_name='关联发布会')
    # 外键的定义方式（多对多），through=表明通过哪个表
    events = models.ManyToManyField(Event, through='GuestEvent')
    # 姓名，唯一
    name = models.CharField('姓名', max_length=256, unique=True)
    # 手机号，最大长度11位 唯一
    phone = models.CharField('手机号', max_length=256, unique=True)
    # 邮箱--专属邮箱字段来管理邮箱地址
    email = models.EmailField('邮箱')

    # 此两个字段，在多对多时应放置在关联表里
    # # 加入时间, 创建数据的时候就自动取当前时间
    # join_time = models.DateTimeField(auto_now_add=True)
    # # 是否签到,默认未签到
    # is_sgin = models.BooleanField('签到状态', default=False)

    def __str__(self):
        return self.name


# 发布会嘉宾中间表
class GuestEvent(models.Model):
    # 通过外键关联关系模型
    # 当发布会1或嘉宾2任意一个被删除，这个条件对应关系也就不应该存在了
    guest = models.ForeignKey(Guest, verbose_name='嘉宾', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name='发布会', on_delete=models.CASCADE)
    # 加入时间，创建数据的时候就自动获取当前时间
    join_time = models.DateTimeField(auto_now_add=True)
    # 是否签到，默认未签到
    is_sgin = models.BooleanField('签到状态', default=False)

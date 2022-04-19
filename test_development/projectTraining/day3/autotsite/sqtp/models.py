from django.db import models


# Create your models here.
class Config(models.Model):
    name = models.CharField('名称', max_length=128)
    # 可null,可空白
    base_url = models.CharField('IP/域名', max_length=512, null=True, blank=True)
    variables = models.JSONField('变量', null=True) # 默认sqlsite不支持json字段
    # 用于参数化
    parameters = models.JSONField('参数', null=True)
    verify = models.BooleanField('https校验', default=False)
    export = models.JSONField('用例返回值', null=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    #同个模型中，两个字段关联同一个模型，必须指定related_name，且名字不能相同
    # 属于哪个用例
    belong_case = models.ForeignKey('Case', on_delete=models.CASCADE, related_name='teststeps')
    # 引用哪条用例
    linked_case = models.ForeignKey('Case', on_delete=models.SET_NULL, null=True, related_name='linked_steps')
    name = models.CharField('名称', max_length=128)
    variables = models.JSONField('变量', null=True)
    extract = models.JSONField('请求返回值', null=True)
    validate = models.JSONField('校验项', null=True)
    setup_hooks = models.JSONField('初始化', null=True)
    teardown_hooks = models.JSONField('清除', null=True)

    def __str__(self):
        return self.name


class Request(models.Model):
    method_choices = (  # method可选字段，二维数组
        (0, 'GET'),  # 参数1：保存在数据库中的值，参数2：对外显示的值
        (1, 'POST'),
        (2, 'PUT'),
        (3, 'DELETE'),
    )
    step = models.OneToOneField(Step, on_delete=models.CASCADE, null=True,related_name='testrequest')
    method = models.SmallIntegerField('请求方法', choices=method_choices, default=0)
    url = models.CharField('请求路径', default='/', max_length=1000)
    params = models.JSONField('url参数', null=True)
    headers = models.JSONField('请求头', null=True)
    cookies = models.JSONField('Cookies', null=True)
    data = models.JSONField('data参数', null=True)
    json = models.JSONField('json参数', null=True)

    def __str__(self):
        return self.url


class Case(models.Model):
    config = models.OneToOneField(Config, on_delete=models.DO_NOTHING)
    suite = models.ForeignKey('Suite', on_delete=models.DO_NOTHING, null=True)
    file = models.CharField('用例文件路径', max_length=1000, default='demo_case.json')

    def __str__(self):
        return self.config.name


class Suite(models.Model):
    config = models.OneToOneField(Config, on_delete=models.DO_NOTHING)
    file = models.CharField('用例文件路径', max_length=1000, default='demo_case.json')

    def __str__(self):
        return self.config.name

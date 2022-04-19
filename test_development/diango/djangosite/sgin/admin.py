from django.contrib import admin
from sgin import models

# Register your models here.
# 后台管理关联模型
admin.site.register(models.Event)
admin.site.register(models.Guest)

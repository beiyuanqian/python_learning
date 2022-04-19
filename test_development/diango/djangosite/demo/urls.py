# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/7/3}

from django.urls import path
from demo import views as demo_views

urlpatterns = [
    # 参数1;匹配的url,参数2：处理该url请求的视图函数，注意视图不要加上括号
    path('index/', demo_views.index),
    path('', demo_views.home),  # 默认显示该url的页面
]

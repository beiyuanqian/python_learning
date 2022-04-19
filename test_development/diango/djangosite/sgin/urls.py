# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/7/3}

from django.urls import path
from sgin import views as sgin_views

urlpatterns = [
    # 发布会相关
    path('events/', sgin_views.events),
    # path('event_detail/', sgin_views.event_detail),
    # 返回指定id的发布会
    path('event_detail/<int:event_id>', sgin_views.event_detail),

    # 嘉宾相关
    path('guests/', sgin_views.guests),
    path('guest_detail/<int:guest_id>', sgin_views.guest_detail),

    # 处理签到
    path('do_sgin/<int:event_id>', sgin_views.do_sgin),
    # 签到成功
    path('sgin_success/<str:phone>', sgin_views.sgin_success),

    # 新增发布会页面
    path('add_event_page/', sgin_views.add_event_page),
    # 新增发布会视图
    path('add_event/', sgin_views.add_event),

    # 新增嘉宾表单页面
    path('add_guest_page/', sgin_views.add_guest_page),
    # 新增嘉宾视图
    path('add_guest/', sgin_views.add_guest),
]
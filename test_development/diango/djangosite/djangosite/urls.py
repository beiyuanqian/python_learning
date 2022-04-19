"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# # 第一步导入视图函数
# from demo import views as demo_views
# from sgin import views as sgin_views

from demo import urls as demo_urls
from sgin import urls as sgin_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # # 参数1;匹配的url,参数2：处理该url请求的视图函数，注意视图不要加上括号
    # path('index/', demo_views.index),
    # path('', demo_views.home),  # 默认显示该url的页面
    # 优化处理时，demo开头的路径，统统交给demo app处理
    path('demo/', include(demo_urls)),

    # # 发布会相关
    # path('events/', sgin_views.events),
    # path('event_detail/', sgin_views.event_detail),
    # 优化处理时，sgin开头的路径，统统交给sgin app处理
    path('sgin/', include(sgin_urls))

]

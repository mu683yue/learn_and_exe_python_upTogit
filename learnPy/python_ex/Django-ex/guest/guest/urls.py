"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""
DDjango项目的URL声明
"""
from django.contrib import admin
from django.urls import path
from sign import views #导入sign应用views文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),#直接跳转到登录页面
    path('index/',views.index),#添加index/路径配置
    path('login_action/',views.login_action),#提交登录请求
    path('event_manage/',views.event_manage),#发布会管理页面
    path('accounts/login/',views.index),#直接跳转到登录页面
    path('search_name/',views.search_name),
    path('guest_manage/',views.guest_manage),
]

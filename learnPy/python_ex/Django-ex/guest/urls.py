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
from django.urls import path,re_path,include
from sign import views,urls #导入sign应用views文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),#直接跳转到登录页面
    path('index/',views.index),#添加index/路径配置
    path('login_action/',views.login_action),#提交登录请求
    path('event_manage/',views.event_manage),#发布会管理页面
    path('accounts/login/',views.index),#直接跳转到登录页面
    path('search_name/',views.search_name),
    path('guest_manage/',views.guest_manage),
    #2.0后的django路径中使用正则表达式需要使用re_path()
    re_path(r'^sign_index/(?P<eid>[0-9]+)$',views.sign_index),#添加签到页面路径的路由
    re_path(r'^sign_index_action/(?P<eid>[0-9]+)$',views.sign_index_action),#添加签到动作路径的路由
    path('logout/',views.logout),
    path('api/',include(('sign.urls','sign'),namespace="sign")), #web接口url根目录为/api/，通过二级目录表示实现具体 功能的接口
    ]
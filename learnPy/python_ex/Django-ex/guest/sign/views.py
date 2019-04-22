#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from sign.models import Event,Guest

"""
Django的视图文件，控制前端页面显示的内容
"""

# Create your views here.
def index(request):
	#return HttpResponse("Hello Django!")
	return render(request,"index.html")
#登录动作
def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user) #登录
			#response.set_cookie('user',username,3600)#添加浏览器Cookie
			request.session['user'] = username #将session信息记录到浏览器
			response = HttpResponseRedirect("/event_manage/")
			return response
		else:
			return render(request,"index.html",{'error':'username or password error!'})

#发布会管理
@login_required  #限制login_action函数必须登录才能访问
def event_manage(request):
	#username = request.COOKIES.get('user','')  #读取浏览器cookie #推荐使用较安全的session
	event_list = Event.objects.all()  #查询所有发布会对象（数据）
	username = request.session.get('user','')  #读取浏览器session
	return render(request,"event_management.html",{'user':username,'events':event_list})

#发布会名称搜索
@login_required
def search_name(request):
	username = request.session.get('user','')
	search_name = request.GET.get("name","")
	event_list = Event.objects.filter(name__contains=search_name)
	return render(request,"event_management.html",{"user":username,"events":event_list})

#嘉宾管理
@login_required
def guest_manage(request):
	userrname = request.session.get('user','')
	guest_list = Guest.objects.all()
	paginator = Paginator(guest_list,2)  #将查询处的左右嘉宾列表guest_list放到Paginator类中，划分为每页显示2条数据
	page = request.Get.get('page')#通过GET请求得到当前显示第几页数据
	try:
		contacts = paginator.page(page)#获取第page页的数据
	except PageNotAnInteger:
		#如果page不是整数，取第一页面数据
		contacts = paginator.page(1)
	except EmptyPage:
		#如果page不在范围，取最后一页面
		contacts = paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html",{"user":username,"guests":guest_list})
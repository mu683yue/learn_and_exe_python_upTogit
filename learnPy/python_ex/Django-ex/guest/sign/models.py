from django.db import models
"""
Django的模型文件，创建应用持续数据表模型（对应数据库的相关操作）
"""

# Create your models here.
#发布会表
class Event(models.Model):
	name = models.CharField(max_length=100)          #发布会标题
	limit = models.IntegerField()					 #参加人数
	status = models.BooleanField()					 #状态
	address = models.CharField(max_length=200)		 #地址
	start_time = models.DateTimeField('events time') #发布会时间
	create_time = models.DateTimeField(auto_now=True)#创建时间（自动获取当前时间）
	def __str__(self):
		return self.name
#嘉宾表
class Guest(models.Model):
	event = models.ForeignKey(Event,on_delete=models.CASCADE)                 #关联发布会ID
	realname = models.CharField(max_length=64)		 #姓名
	phone = models.CharField(max_length=16)	         #手机号
	email = models.EmailField()						 #邮箱
	sign = models.BooleanField()					 #签到状态
	create_time = models.DateTimeField(auto_now=True)#创建时间（自动获取当前时间）
	

class Meta: #Django模型的一个内部类，用于定义一些Django模型类的行为特性。
	unique_together = ("event","phone") #unique_together用于设置两个字段为联合主键
def __str__(self):
		return self.realname

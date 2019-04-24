from django.test import TestCase
from django.contrib.auth.models import User
from sign.models import Event
"""
创建Django测试用例
"""

# Create your tests here.

class LoginAction(TestCase):
	''' 测试登录动作'''

	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','admin123456')

	def test_add_admin(self):
		'''添加用户'''
		user = User.objects.get(username="admin")
		self.assertEqual(user.username,"admin")
		self.assertEqual(user.email,"admin@mail.com")

	def test_login_action_username_password_null(self):
		'''用户名密码为空'''
		test_data = {'username':'','password':''}
		response = self.client.post('/login_acyion/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn(b"username or password error!",response.content)

	def test_login_action_username_password_error(self):
		'''用户名密码错误'''
		test_data={'username':'abc','password':'123'}
		response=self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn(b"username or password error!",response.content)

	def test_login_ssuccess(self):
		'''登录成功'''
		test_data = {'username':'admin','password':'admin123456'}
		response = self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,302)

class EventManageTest(TestCase):
	'''测试发布会管理视图'''
	def setUp(self):
		User.objects.create_user('admin','admin@mail.com','admin123456')
		Event.objects.create(name="xiaomi5",limit=200,address="beijing",status=1,start_time='2019-8-10 12:30:00')
		self.login_user={'username':'admin','password':'admin123456'}

	def test_event_manage_success(self):
		'''测试发布会：xiaomi5'''
		#event_search和search_name两个试图函数被@login_required修饰，
		#所以要想测试者两个功能，必须先登录成功，并需要构造登录用户的数据
		response = self.client.post('/login_action/',data=self.login_user)
		response = self.client.post('/event_manage/')
		self.assertEqual(response.status_code,200)
		self.assertIn(b"xiaomi5",response.content)
		self.assertIn(b"beijing",response.content)

	def test_event_manage_search_success(self):
		'''测试发布会搜索'''
		response = self.client.post('/login_action/',data=self.login_user)
		response = self.client.post('/search_name/',{"name":"xiaomi5"})
		self.assertEqual(response.status_code,200)
		self.assertIn(b"xiaomi5",response.content)
		self.assertIn(b"beijing",response.content)

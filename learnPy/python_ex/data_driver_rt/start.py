#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
启动文件，用于集成所有的模块完成目标
"""
import os
import sys
from lib.common import OpCase
#from lib.send_email import send_email
from config import setting

BASE_PATH = os.path.dirname(
	os.path.diename(os.path.abspath(__file__))
)  #找到APT这个文件夹的地址
sys.path.insert(0,BASE_PATH)   #把APT目录加到环境变量中，用于在其他不能帮忙加环境变量的时候

class CaseRun(object):
	def find_cases(self):
		op = OpCase()  #实例化操作用例这个类
		for f in os.listdir(setting.CASE_PATH):   #获取到cases文件夹下的文件
			abs_path = os.path.join(setting.CASE_PATH,f)  #拼接测试用例且文件的绝对路径
			case_list = op.get_case(abs_path)   #利用get_case函数获取到每个用例的case
			res_list = []  #出啊关键一个空的list来存放测试返回的报文和测试结果
			pass_count = 0 #用来计算成功用例个数
			fail_count = 0 #用来计算失败的用例个数
			for case in case_list:
				url,method,req_data,check = case #get_case函数中提取每行用例的四个元素，分别定义一下
				res = op.my_request(url,method,req_data)   #调用my_request函数进行测试接口返回结果
				status = op.check_res(res,check)   #检查测试返回报文是否和预计测试结果相同，如果相同测试通过，否则测试失败
				res_list.append([res,status])  #为了一次性写入测试结果，先将结果放入list
				if status == '通过':
					pass_count +=1
				else:
					fail_count +=1
			op.write_excel(res_list) #写入excel
			msg = '''  #定义邮件正文
			XX你好：
					本次共允许%s条用例，通过%s条，失败%s条。
			''' % (len(res_list),pass_count,fail_count)


			
CaseRun.find_cases()  #运行find_cases函数


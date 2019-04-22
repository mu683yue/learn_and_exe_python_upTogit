#!/usr/bin/python3

import xlrd
from lib.log import apt_log
import requests
from xlutils import copy

class OpCase(object):
	def get_case(self,file_path):
		cases = []
		if file_path.endwith('.xls') or file_path.endwith('.xlsx'):  #判断路径是否存在
			try:
				book = xlrd.open_workbook(file_path)
				sheet = book.sheet_by_index(0)  #打开用例文件
				for i in range(1,sheet.nrows):    #从第二行开始遍历excel文件内容（第一行是标题）
					row_data = sheet.row_values(i) #获取每行的内容
					cases.append(row_data[4:8])  #在case这个list中存每个用例的url,method,reg_data,check
				opt_log.info('共读取%s条用例' %（len(cases))   #检查cases中的元素个数，日志记录读取几条用例
				self.file_path = file_path   #读取成功说明文件路径是正确的，那么这边定义下面写excel就可以直接使用
			except Exception as e:
				apt_log.error('【%s】用例打开失败，错误信息：%s' % (file_path,e))
		else:
			apt_log.error('用例文件不合法，%s' % file_path)
		return cases

	def dataToDict(self,data):   #将用例中的reg_data转为字典格式，可以直接用子啊reques模块
		res = {}
		data = data.split(',') #这个地方要求用例中请求参数使用英文逗号分割的
		#这边分割入参后，入参变为['a=1', 'b=2']这样的格式
		for d in data:
			k,v = d.split('=')
			#再次分割后变为['a','1']这样的模式分别用k代表a,v代表1
			res[k] = v   #存入字典中变成'a':1,这样的模式可直接在request模块接口测试中作为入参使用
		return res

	def my_request(self,url,method,data):
		method = method.upper() #首先将请求方式变为大写模式，方便后面验证
		data = self.dataToDict(data) #把a=1,b=2格式的请求参数变成字典格式
		try:
			if method == 'POST':
				res = requests.post(url,data).text  #如果请求方式是post按照post模式进行接口测试
			elif method == 'GET':
				res = requests.get(url,data).text   #按照get方式传入url和data进行接口测试
			else:
				apt_log.warning('暂时不支持该请求')  #其他请求方式不支持，打印日志并返回提示
				res = '暂时不支持该请求'
		except Exception as e:
			msg = '【%s】接口调用失败，%s' (url,e)   #请求未成功提示接口调用失败，写入日志并返回提示
			apt_log.error(msg)
			res = msg
		return res

	def check_res(self,res,check):
		res.replace('": "', '=').replace('": ', '=')   #返回报文是json格式的，利用字符替换让数据变成“a=1,b=2”的格式
		for c in check.split(','):    #判断验证数据是否在返回的报文中
			if c not in res:
				apt_log.info('结果校验失败，预期结果：【%s】,实际结果【%s】' % (c,res))  #不匹配则测试校验失败，打印日志
				return '失败'   #但会失败提示
			return '通过'   #如果存在说明测试通过

		def write_excel(self,cases_res):   #入参是每个用例的执行结果
			book = xlrd.open_workbook(self.file_path)
			new_book = copy.copy(book)
			sheet = new_book.get_sheet(0)  #复制测试用例excel文件
			row = 1
			for case_res in cases_res:    #遍历写入数据
				sheet.write(row,8,case_res[0])   #第8列写返回结果
				sheet.write(row,9,case_res[1])   #第9列写测试是否通过
				row +=1
			new_book.save(self.file_path.replace('xlsx','xls'))   #保存结果




#!usr/bin/python3
#-*- coding:utf-8 -*-

import sys
sys.path.append(r"S:\Develop\python_workplace\python_requests_excel_ddt_unittest接口自动化框架")
import os
import requests
import unittest
from ddt import (ddt,data,unpack)
from common import base_api
from common import readexcel
from common import writeexcel

'''
测试用例使用unittest框架组件，并用ddt数据驱动模式，批量执行测试用例
'''

#获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath,"demo_api.xlsx")
print(f"demo_api.xlsx的路径是{testxlsx}")

#复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath),"report")
reportxlsx = os.path.join(report_path,"result.xlsx")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()

@ddt
class Test_api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        #如果有登录的话，就在这里先登录
        writeexcel.copy_excel(testxlsx,reportxlsx)   #复制xlsx文件

    @data(*testdata)
    @unpack
    def test_api(self,data):
        #先赋值excel数据到report
        res = base_api.send_requests(self.s,data)

        base_api.write_result(res,filename=reportxlsx)
        #检查点checkpoint
        check = data["checkpoint"]
        print(f"检查点->:{check}")
        #返回结果
        res_text = res["text"]
        print(f"返回实际结果->:{res_text}")
        #断言
        self.assertTrue(check in res_text)

if __name__=="__main__":
    unittest.main()
        



#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用requests进行CS manager页面部分功能测试
"""
import unittest
import requests
import urllib
import re
from ddt import ddt,data,file_data,unpack

class MyTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://10.10.10.55"
        print("CS API test is starting!")

    def tearDown(self):
        print("test end")
    
@ddt
class CS_managerTEST(MyTest):
    
    #测试登录
    @data({'first':'test@cloudscreen.com','second':'123456','third':None})
    @unpack
    def test_login(self,first,second,third):
        login_url = urllib.parse.urljoin(self.base_url,"/csg/web/login")
        print(f"测试登录url:{login_url}")
        #请求头
        payload = {'loginName':first,'password':second,'captcha':third}
        req = requests.post(login_url,data = payload)  #发送登录请求
        print(f"请求头:{req.headers}")
        print(req.status_code,req.json(),req.text)

        #从响应头提取JsessionID
        re_jsessionID = re.compile("JSESSIONID=(.*?);")
        jsessionID = re.findall(re_jsessionID,req.headers)
        #print(f"re_jsessionID:{jsessionID}")

        #从响应信息（r.text）提取token
        re_token = re.compile('"token": "(.*?)",')
        token = re.findall(re_token,req.text)
        print(f"token:{token}")
        
        #断言是否登录成功
        self.assertIs(200,req.status_code)
        self.assertIn("恒生科技", req.text)
        self.assertTrue('"id" : 2' and '"enterpriseName" : "恒生科技"' in req.text)

##    def test_GetAuth(self):
##        print(f"re_jsessionID:{jsessionID}")
##        print(f"token:{token}")
    

if __name__=="__main__":

    '''
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTests(map(CS_managerTEST,["test_login"]))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    unittest.main()
    
        

#!/usr/bin/python3
#-*- coding:utf-8 -*-

impot unittest
from selenium import webdriver
import time

class client_device_view_test(unittest.TestCase):
    def setUp(self):
        chromedriver=r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
        print('测试终端设备内容视图')
        self.diver=webdiver.Chrome(chromedriver)

    def tearDown(self):
        print('测试结束')
        self.driver.quit()

    def test_turnToClientServiceView(self):
        admin_url="10.10.10.55/uds"
        terminalDeviceView_url="http://10.10.10.55/uds/#/terminalDeviceView"
        driver=self.driver
        
        '''
        登录成功的代码（可以考虑封装登录成功后调用）
        '''
        driver.get(admin_url)
        try:
        driver.find_element_by_text("终端设备内容视图").click()
        self.assertEqual(driver.current_url,msg="成功跳转到终端设备内容视图页面")
        except AssertionError as msg:
            print(msg)
            
    def test_clickMoreOnPage(self):
        
        
    
        

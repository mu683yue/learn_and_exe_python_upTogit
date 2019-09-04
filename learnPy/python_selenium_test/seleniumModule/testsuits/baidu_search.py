#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os

##fp = os.path.abspath(__file__)
##pro_dir = os.path.dirname(os.path.dirname(fp))
##print(pro_dir+'\\'+'framework')

sys.path.append(r"S:\Develop\python_workplace\python_selenium_test\seleniumModule")


import time
import unittest
from ddt import ddt,data
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


@ddt
class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    @data('selenium','783中文输入')
    def test_baidu_search(self,value):
        """
        这里一定要test开头，吧测试逻辑代码封装到一个test开头的方法离。
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search(value)  #调用页面对象中的方法
        homepage.send_submit_btn()   #调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()   #调用基类截图方法
        try:
            assert value in homepage.get_page_title()   #调用页面对象继承基类中的获取页面标题的方法
            print('Test Pass')
        except Exception as e:
            print('Test Fail.',e)
            
if __name__=="__main__":
    unittest.main()
        
    

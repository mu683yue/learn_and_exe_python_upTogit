#!/usr/bin/python3
#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        print('CS test start!')
       # self.chromedriver=r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
        self.driver=webdriver.Chrome(r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

    def tearDown(self):
        print('test end !!')
        self.driver.quit()
        
    def test_log_Case1(self):
        #variables
        log_url_47=r'http://10.10.11.47:8080/cuds/#/login'
        url_console_47=r'http://10.10.11.47:8080/cuds/#/console'
        username_1="huqiong.lin@cloudscreen.com"
        password_1="cs123456"
        yanzhengma_1="1111"
    #GET index logiing page
        driver=self.driver
        driver.get(log_url_47)
        print("access to %s" %(log_url_47))

    #input right username and password
        input_username=driver.find_element_by_css_selector("input[placeholder='用户名']")
        input_username.send_keys(username_1)
        input_password=driver.find_element_by_css_selector("input[placeholder='密码']")
        input_password.send_keys(password_1)
        driver.find_element_by_css_selector("input[placeholder='验证码']").send_keys(yanzhengma_1)
        try:
            driver.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div/button").click()
            self.assertEqual(driver.current_url,url_console_47, msg="没有成功跳转到总览页面")
        except AssertionError as msg:
            print(msg)
        else:
            print("成功跳转到总览页面%s" %(url_console_47))

if __name__=='__main__':
    unittest.main()

                

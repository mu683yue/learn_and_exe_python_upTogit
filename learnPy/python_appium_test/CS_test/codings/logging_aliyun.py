#!/usr/bin/python3
#-*- coding:utf-8 -*-

from appium import webdriver
import time

#变量
Mi_max_deviceName='5d5bf4e4'
remote_url=r'http://localhost:4723/wd/hub'
login_username='huqiong.lin@cloudscreen.com'
login_password='1qaz2wsx#'



caps={}
caps["platformName"]="android"
caps["deviceName"]=Mi_max_deviceName
##caps["appPackage"]="com.alibaba.cloudmail"
##caps["appActivity"]="com.squareup.leakcanary.internal.DisplayLeakActivity"
caps["platformVersion"]="6.0.1"
caps["app"]='E:\\Cloudmail_v2_7_0_0.apk'

driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
print(driver.current_activity)
#登录成功测试
driver.find_element_by_id('com.alibaba.cloudmail:id/edit_view').send_keys(login_username)
driver.find_element_by_android_uiautomator("index(\"0\")").send_kys(login_password)
driver.find_element_by_id('com.alibaba.cloudmail:id/next').click()
#获取登录后的classname，并判断是否登录成功
print(driver.current_activity)
##su_className=driver.find_element_by_calss_name('android.widget.TextView')
##if():
##    print("登录成功！")
##else:
##    print("登录失败！")




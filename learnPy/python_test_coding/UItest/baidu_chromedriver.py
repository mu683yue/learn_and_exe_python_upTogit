#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver

#-----use chromedriver
chromedriver="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver=webdriver.Chrome(chromedriver)

driver.maximize_window()
first_url="http://www.baidu.com"
driver.get(first_url)
print("access to %s" %(first_url))

driver.find_element_by_id("kw").send_keys("hello world")
driver.find_element_by_id("su").click()
#driver.quit()



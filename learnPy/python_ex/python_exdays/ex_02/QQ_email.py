#!usr/bin/python3
# -*- coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By

qq_login_url="https://mail.qq.com"
qq_username="192191237@qq.com"
qq_password="13mumujingyue99"
driver = webdriver.Chrome(r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

#登录QQ邮箱
driver.get(qq_login_url)
driver.switch_to.frame("login_frame")
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys(qq_username)
#driver.find_element(By.XPATH,"//*[@class='inputstyle' and @id='u']").send_keys(qq_username)
driver.find_element(By.ID,"p").send_keys(qq_password)
driver.find_element(By.CLASS_NAME,"btn").click()

#发邮件
#if driver

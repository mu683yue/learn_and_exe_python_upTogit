#!/usr/bin/python3
#-*- coding;utf-8 -*-

'''
登录126邮箱的公用登录模块 login_public_126.py
'''

def login(driver):
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys("username")
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys("password")
    driver.find_element_by_id("loginBtn").click()
    

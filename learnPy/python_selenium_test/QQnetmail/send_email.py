#!/usr/bin/python3
#-*- coding:utf-8 -*-

from common import Common
from selenium import webdriver


class QQsendmail():
    """
    使用QQsendmail发送邮件
    """
    def __init__(self):
        self.driver = Common.set_driver("Chrome")
        print(self.driver)
    
    def login(self,login_url):
        driver = self.driver
        driver.get(login_url)
        #login_frame = driver.find_element_by_id("login_frame")
        driver.switch_to.frame("login_frame")

        #默认使用QQ号登录
        qq_account = "192191237@qq.com"
        qq_pw = "13mumujingyue99"
        driver.find_element_by_id("u").send_keys(qq_account)
        driver.find_element_by_id("p").send_keys(qq_pw)
        driver.find_element_by_id("login_button").click()

        driver.switch_to.default_content()


if __name__=='__main__':
    login_url = "https://mail.qq.com/"
    qq_s = QQsendmail()
    qq_s.login(login_url)
        

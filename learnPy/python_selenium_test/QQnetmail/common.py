#!/usr/bin/python3
#-*- coding:utf-8 -*-

from selenium import webdriver 

class Common:
    #类变量，全局其他地方通过其中的类变量访问Common中方法对象


    def set_driver(driver_name):
        """
        设置driver为全局变量供其他用例访问
        """
        if driver_name in "Chrome" or "chrome":
            chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver)
        return driver

if __name__=='__main__':
    Common.set_driver("chrome")
        

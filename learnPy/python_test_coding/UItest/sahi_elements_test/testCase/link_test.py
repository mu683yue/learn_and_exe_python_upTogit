#!/usr/bin/python3
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,time

class Mytest(unittest.TestCase): 
    def setUp(self):
        self.driver=webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.index_url="http://sahitest.com/demo/index.htm"
        

    def tearDown(self):
        self.driver.quit()

class Demo_link_test(Mytest):
    
    def test1_get_into_linkTest(self):  #使用了main()方法执行，测试用例必须要以test开头，否则无法执行
        print("test case 1===================")
        #click link-'Link Test'
        driver= self.driver
        driver.get(self.index_url)
        try:
            driver.find_element_by_link_text("Link Test").click()
            self.assertEqual(driver.current_url, "http://sahitest.com/demo/linkTest.htm", msg="没有成功跳转到linkTest.htm")
        except AssertionError as msg:
            print(msg)
        else:
            print("成功跳转到linkTest.htm")
    
        #back to linkTest.htm
        try:
            driver.find_element_by_id("linkById").click()
            driver.find_element_by_link_text("Back").click()
            #back to linkTest.htm
            self.assertEqual(driver.current_url, "http://sahitest.com/demo/linkTest.htm", msg="没有成功返回到linkTest.htm")
        except AssertionError as msg:
            print(msg)
        else:
            print("成功返回到linkTest.htm")
        driver.close()
            
    def test2_get_into_formTest(self):
        print("test2==============")
        #link with return true
        driver=self.driver
        driver.get("http://sahitest.com/demo/linkTest.htm")
        try:
            driver.find_element_by_xpath("/html/body/a[4]").click()

            #必须点击“确定”，才显示页面内容(警告框处理)
            driver.switch_to_alert().accept()
            self.assertEqual(driver.current_url, "http://sahitest.com/demo/formTest.htm" , msg="没有成功跳转到formTest.htm")            
        except AssertionError as msg:
                print(msg)
        else:
                print("成功跳转到formTest.htm")
                
        self.assertEqual(driver.title, "Form Test", "没有成功显示formTest.htm页面内容")
        try:
            driver.back()       
            #back to linkTest.htm
            self.assertEqual(driver.current_url, "http://sahitest.com/demo/linkTest.htm", "没有成功跳转到linkTest.htm")
        except AssertionError as msg:
            print(msg)
        else:
            print("成功跳转到linkTest.htm")


        try:
             #点击search有警告框
            driver.find_element_by_xpath("/html/body/a[12]/span").click()
            alert_search=driver.switch_to_alert()
            self.assertEqual(alert_search.text, "123",msg="search不正常")
        except AssertionError as msg:
            print(msg)
        else:
            driver.switch_to_alert().accept()
            print("search正常")

        try:
            #点击"Don't use my text to identify.Use my title."，点击后有新页面产生
            driver.find_element_by_partial_link_text("Don't use my").click()
            print(driver.current_window_handle)
        except:    
            #截图
            driver.get_screenshot_as_file(r'D:\LHQ_develop\python_test_coding\sahi_elements_test\screenshot\useMyTile.png')
if __name__=='__main__':
    unittest.main()






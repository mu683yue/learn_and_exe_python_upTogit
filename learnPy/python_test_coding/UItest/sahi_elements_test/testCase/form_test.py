#!/usr/bin/python3
#-*-coding:utf-8-*-

from selenium import webdriver
import unittest

class Mytest(unittest.TestCase): 
    def setUp(self):
        self.driver=webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.index_url="http://sahitest.com/demo/index.htm"
        

    def tearDown(self):
        self.driver.quit()

class Demo_form_test(Mytest):

    def test1_

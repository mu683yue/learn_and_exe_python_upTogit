#!/usr/bin/python3
#!-*-coding:utf-8-*-

'''
#装饰器实例1（不知怎么运行正确）
def logging_tool(level):
    def decorator(func):
        def wrapper(*arg,**kwargs):
            if level=='error':
                logging.error('%s is running...' % func.__name__)
            elif level=='warn':
                logging.warn('%s is running...' % func.__name__)
            else:
                logging.info('%s is running...' % func.__name__)

            func()
        return wrapper
    return decorator

@logging_tool(level='warn')
def today(name='devin'):
    print('Hello,%s! Today is 2018-7-1' % name)

today()
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class B(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        B.dr=webdriver.Firefox(firefox_binary=FirefoxBinary(r'C:/Program Files/Mozilla Firefox/firefox.exe'))

    def get_screenshot_as_file(func):
        def wrapper(self):
            try:
                func(self)
            except:
                self.dr.get_screenshot_as_file('./{}.png'.format(func.__name__))
        return wrapper

    @get_screenshot_as_file
    def test1(self):
        self.assertTrue(True)
        self.dr=B.dr
        self.dr.get('http://www.baidu.com')
        assert False

    @get_screenshot_as_file
    def test2(self):
        assert True

    @classmethod
    def tearDownClass(cls):
        B.dr.quit()

unittest.main()


    
        


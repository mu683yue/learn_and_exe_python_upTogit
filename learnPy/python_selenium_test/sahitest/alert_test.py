#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
sahitest.com Alert Test
"""
import sys
import unittest
import datetime
from ddt import ddt,data
from selenium  import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HTMLTestRunner

class Logger():
    def __init__(self,filename='default.log',stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename,'a')

    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

@ddt
class AlertTest(unittest.TestCase):
    def setUp(self):
        self.alert_url = "http://sahitest.com/demo/alertTest.htm"
        self.chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver)
        
        print("test start")

    def tearDown(self):
        self.driver.quit()
        print('test end')

    #Click For Alert
    def test_clickforalert(self):
        driver = self.driver
        driver.get(self.alert_url)
        alert_message = driver.find_element_by_name('t1').get_attribute('value')

        driver.find_element_by_name("b1").click()
        instance = WebDriverWait(driver,10).until(EC.alert_is_present())
        print(instance.text)
        print(self.assertIn(alert_message,instance.text))  #判断成功，返回None，因为msg=None
        instance.accept()

    #click after input "林test"
    @data(u"林test",u'23235速度放缓的')
    def test_inputclick(self,message):
        driver = self.driver
        driver.get(self.alert_url)
        input_ele = driver.find_element_by_name("t1")
        input_ele.clear()
        input_ele.send_keys(message)
        alert_message = driver.find_element_by_name('t1').get_attribute('value')
        self.assertIn(message,alert_message)

        driver.find_element_by_name("b1").click()
        instance = WebDriverWait(driver,10).until(EC.alert_is_present())
        print(instance.text)
        print(self.assertIn(alert_message,instance.text))  #判断成功，返回None，因为msg=None
        instance.accept()

if __name__=='__main__':
    time = datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
    fp = open('ss.html','wb')
    
    #unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    testcase1 = loader.loadTestsFromTestCase(AlertTest)
    suite.addTest(testcase1)
    

    #runner = unittest.TextTestRunner(verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(fp,title=u'My test',description=u'This is a report test')
    runner.run(suite)

    fp.close()
##    with open("1.txt","a+") as f:
##        
##        f.write(f"{time}运行1次")
    #sys.stdout = Logger(f'{time}.log',sys.stdout)
    
    
    
    

#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
sahitest.com Prompt Test
"""
import unittest
from ddt import ddt,data
from selenium  import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



@ddt
class PromptTest(unittest.TestCase):
    def setUp(self):
        self.alert_url = "http://sahitest.com/demo/promptTest.htm"
        self.chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver)
        self.wait = WebDriverWait(self.driver,10)
        
        print("test start")

    def tearDown(self):
        self.driver.quit()
        print('test end')


    @data(u"林test",u"it's OK ")
    def prompt_input_test(self,info):
        driver = self.driver
        wait = self.wait
        driver.get(self.alert_url)
        driver.find_element_by_name("b1").click()

        prompt = wait.until(EC.alert_is_present())
        prompt.send_keys(info)
        prompt.accept()

        text = driver.find_element_by_name("t1").text
        print(text)

    def prompt_dismiss_test(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.alert_url)
        driver.find_element_by_name("b1").click()
        
        prompt = wait.until(EC.alert_is_present())
        prompt.dismiss()

if __name__=="__main__":
    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'prompt'
    
    suite = unittest.TestSuite()
    testcase = loader.loadTestsFromTestCase(PromptTest)
    suite.addTest(testcase)

    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite)
        
        
        

#!/usr/bin/python3
#-*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythoOrgSearch(unittest.TestCase):
    """
    selenium结合unittest来实现简单的测试用例，测试www.python.org
    """
    def setUp(self):
        self.driver=webdriver.Firefox()

    def test_search_in_python_org(self):
        driver=self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        elem=driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDowm(self):
        self.driver.close() #也可以使用qiut(),_close()只是关闭页面，当只有一个页面时，_close()也可以关闭整个浏览器

if __name__=="__main__":
    unittest.main()
    

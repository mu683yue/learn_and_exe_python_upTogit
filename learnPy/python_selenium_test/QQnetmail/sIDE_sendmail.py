# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SIDESendmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.qq.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_s_i_d_e_sendmail(self):
        driver = self.driver
        driver.get(self.base_url + "/cgi-bin/loginpage")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | login_frame | ]]
        driver.find_element_by_id("u").click()
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys("192191237@qq.com")
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys("13mumujingyue99")
        driver.find_element_by_id("login_button").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("composebtn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | mainFrame | ]]
        driver.find_element_by_id("subject").clear()
        driver.find_element_by_id("subject").send_keys("1")
        driver.find_element_by_name("UploadFile").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_link_text(u"发送").click()
        driver.find_element_by_css_selector("#toAreaCtrl > div.addr_text > input.js_input").clear()
        driver.find_element_by_css_selector("#toAreaCtrl > div.addr_text > input.js_input").send_keys("mu683yue@163.com")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

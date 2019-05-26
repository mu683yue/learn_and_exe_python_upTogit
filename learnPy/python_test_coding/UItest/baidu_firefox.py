#!usr/bin/python3
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary=FirefoxBinary(r'C:/Program Files/Mozilla Firefox/firefox.exe')
driver=webdriver.Firefox(firefox_binary=binary)

url1="http://www.baidu.com"
driver.get(url1)
print("access to %s" %(url1))

driver.find_element_by_id("kw").send_keys("Python")
driver.find_element_by_id("su").click()
#driver.quit()

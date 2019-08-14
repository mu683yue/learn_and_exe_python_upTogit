#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
http://sahitest.com/demo/tableTest.htm
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url = "http://sahitest.com/demo/tableTest.htm"
driver.get(url)

table_list = driver.find_elements_by_css_selector('table[border="1"]')
print(len(table_list))

def get_table_to_list():
    
    for i in range(0,len(table_list)):
        row = driver.find_elements_by_xpath(f"//table[{i+1}]/tbody/tr")

        for j in range(0,len(row)):
            col = driver.find_elements_by_xpath(f"//table[{i+1}]/tbody/tr[{j+1}]/td")
            list = [[None]*len(col) for _ in range(len(row))]
            print(len(col),len(row),list)
            for n in range(0,len(row)):             
                list[j][n]= col.text
                print(f"list[{j}][{n}]:{list[j][n]}")
        print(f"list{i}:{list}")

if __name__=='__main__':
    get_table_to_list()
    driver.quit()

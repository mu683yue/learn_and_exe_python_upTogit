#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
测试https://www.bixia.org/首页的搜索功能
-点击“搜索”会新增页面
-搜索失败，新增页面中的列表中数据空
-搜索成功，新增页面中的列表中有匹配的数据，输出列表中的数据
"""

import unittest
from ddt import (ddt,data)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@ddt
class testFirstPage(unittest.TestCase):
        
    def setUp(self):
        self.base_url = 'https://www.bixia.org/'
        self.chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver)
        self.wait = WebDriverWait(self.driver,10)
        
        print('测试首页搜索功能开始！')

    def tearDown(self):
        self.driver.quit()
        print('测试结束!')

    @data(u"心坟")
    #测试：点击“搜索”会新增页面
    def test_addNewPage(self,input_filename):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url)
        #查找输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search , #bdcsMain')))
        input.send_keys(input_filename)   #在网站搜索失败的书名
        btn = driver.find_element_by_xpath('//input[@class="searchBtn"]')
        btn.click()  

        page_list = driver.window_handles
        self.assertGreaterEqual(len(page_list),2) #判断有新增页面
        
        new_page = page_list[1]
        driver.switch_to_window(new_page)
        print(f"新页面url{driver.current_url}\n 新页面源代码：{driver.page_source}")
        ele = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="search-list"]')))
        self.assertIn(f'搜索"{input_filename}"相关小说',ele.text)
        driver.close()
        

    @data(u"心坟")
    #测试：搜索失败，新增页面中的列表中数据空   
    def test_searchFail(self,input_filename):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url)


        #查找输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search , #bdcsMain')))
        input.send_keys(input_filename)   #在网站搜索失败的书名
        btn = driver.find_element_by_xpath('//input[@class="searchBtn"]')
        btn.click()  #回车搜索
        
        page_list = driver.window_handles
        driver.switch_to_window(page_list[1])

        #搜索内容空的时候<ul>下面只有一个<li>tag
        li_list = driver.find_elements_by_tag_name('li')
        self.assertEqual(len(li_list),1)               
        driver.close()

    @data(u"厂花")
    #测试：搜索成功，新增页面中的列表中有匹配的数据，输出列表中的数据
    def test_searchSuccess(self,input_filename):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url)

        #查找输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search , #bdcsMain')))
        input.send_keys(input_filename)   #在网站搜索失败的书名
        btn = driver.find_element_by_xpath('//input[@class="searchBtn"]')
        btn.click()  #回车搜索
        
        page_list = driver.window_handles
        driver.switch_to_window(page_list[1])

        #页面至少有2个li标签，且第2个li标签中的“作品名称”的text包含“厂花”
        li_list = driver.find_elements_by_tag_name('li')
        self.assertGreaterEqual(len(li_list),1)

        li_2_span_2_text = driver.find_element_by_xpath('//li[2]/span[2]').text
        print(li_2_span_2_text)
        self.assertIn(input_filename,li_2_span_2_text)
        driver.close()

        

if __name__=='__main__':
    unittest.main()
    
            
        
        
        

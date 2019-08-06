#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
使用selenium爬取“笔下文学”网站https://www.bixia.org/中的小说内容

--根据关键字搜索获得小说列表
--进入某小说所在首页,获得小说每个章节的url
--进入某小说章节页面，模拟键盘鼠标复制小说内容至剪贴板----不能实现
--进入某小说章节页面，直接根据网页源码提取小说内容
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GetNoval(object):

    def __init__(self,
                 url=None,chromeDriver=None,name=None):

       # Default empty for params


       self.url = url
       self.name = name
       self.chromeDriver = chromeDriver

    #加载驱动
    def browser(self):
        driver = webdriver.Chrome(self.chromeDriver)    #加载谷歌浏览器驱动
        return driver
        

    
#根据关键字搜索获得小说列表
    def getNovalListWithName(self,driver,url,name):
        '''
        return:file_dict{name:url}
        '''
        wait = WebDriverWait(driver,10)
        driver.get(url)
        file_dict = {}
        
        #查找输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search , #bdcsMain')))
        input.send_keys(name)   #在网站搜索失败的书名
        btn = driver.find_element_by_xpath('//input[@class="searchBtn"]')
        btn.click()  

        page_list = driver.window_handles
        assert(len(page_list)>= 2) #判断有新增页面
        
        new_page = page_list[1]
        driver.switch_to_window(new_page)
        print(f"新页面url{driver.current_url}\n 新页面源代码：{driver.page_source}")
        ele = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="search-list"]')))
        assert(f'搜索"{name}"相关小说'in ele.text)

        #根据标签li判断搜索结果
        li_list = driver.find_elements_by_xpath('//li/span[2]/a')
        if len(li_list) >=2:
            for i in range(2,len(li_list)):
                ele_text = li_list[i].text
                ele_link = li_list[i].get_attribute('href')
                file_dict[ele_text] = ele_link
                
        print(li_list)
        print(file_dict)
        return file_dict
            
        

    #进入某小说所在首页,获得小说每个章节的url
    

    

    
    #进入某小说章节页面，直接根据源代码提取小说内容
    def getNovalContent1(self,driver,url):

        driver.get(url)
        text = driver.find_element_by_id('content').text
        return text


if __name__ == '__main__':
    chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    gn = GetNoval(chromeDriver=chromedriver)
    driver = gn.browser()

    #关键词“厂花”搜索
    base_url = "https://www.bixia.org/"
    name = u"厂花"
    #dict = getnoval.getNovalListWithName(driver,url=base_url,name=name)

    #获取章节内容
    url = "https://www.bixia.org/47_47219/2571798.html"
    print(gn.getNovalContent1(driver,url = url))
    
    #关闭浏览器
   # driver.quit()

    

    
        

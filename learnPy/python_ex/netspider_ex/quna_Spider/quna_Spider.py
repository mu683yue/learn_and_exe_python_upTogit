#!/usr/bin/python3
#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
from bs4 import BeautifulSoup
import datetime

class QunaSpider(object):

    def get_hotel(self,driver,to_city,fromdate,todate):

        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate = driver.find_element_by_id('toDate')
        ele_search = driver.find_element_by_class_name('search-btn')
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()
        page_num = 0
        while True:
            #分两次获取一页完整的数据，第二次让driver执行js脚本，把网页拉到底部
            try:
                WebDriverWait(driver,10).until(
                    EC.title_contains(unicode(to_city))
                )
            except Exception as e:
                print(e)
                break
            time.sleep(5)

            js = "window.scrollTo(0,document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)

            #使用beautifulsoup解析酒店信息并将数据进行清洗和存储
            htm_const = driver.page_source
            soup = BeautifulSoup(htm_const,'html.parser',from_encoding='utf-8')
            infos = soup.find_all(class_="item_hotel_info")
            f = codecs.open(unicode(to_city)+unicode(fromdate)+u'.html','a','utf-8')
            for info in infos:
                f.write(str(page_num)+'--'*50)
                content = info.get_text().replace(" ","").replace("\t","").strip()
                print(content)
                #报错：datetime.date没有len()
                lns=[]
                lns=[ln for ln in content.splitlines() if ln.strip()]
                for line in lns:
                    f.write(line)
                    f.write('\r\n')
                f.close()
                try:
                    #点击下一页，继续重复这一个过程
                    next_page=webDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                        )
                    next_page.click()
                    page_num+=1
                    tiem.sleep(10)
                except Exception as e:
                    print(e)
                    break

    def crawl(self,root_url,to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tommorow = tomorrow.strftime('%Y-%m-%d')
        
        binary=FirefoxBinary(r'C:/Program Files/Mozilla Firefox/firefox.exe')
        driver=webdriver.Firefox(firefox_binary=binary)

        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.get_hotel(driver,to_city,today,tomorrow)

if __name__=='__main__':
    spider = QunaSpider()
    spider.crawl('http://hotel.qunar.com/',u"上海")
        






































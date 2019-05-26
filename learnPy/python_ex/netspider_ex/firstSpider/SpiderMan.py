#!/usr/bin/python3
#-*- coding:utf-8 -*-

##from firstSpider.DataOutput import DataOutput
##from firstSpider.HtmlDownloader import HtmlDownloader
##from firstSpider.HtmlParser import HtmlParser
##from firstSpider.UrlManager import UrlManager

from DataOutPut import DataOutPut
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

'''
爬虫调度器首先初始化各个模块，然后通过crawl(root_url)方法传入入口URL，方法内部实现按照运行流程控制各个模块的工作。
'''


class SpiderMan(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
        self.output=DataOutPut()

    def crawl(self,root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从url管理器获取新的url
                new_url=self.manager.get_new_url()
                #从HTML管理器下载网页
                html=self.downloader.download(new_url)
                #HTML解析器抽取网页数据
                new_urls,data=self.parser.parser(new_url,html)
                #将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
            #数据存储器将文件输出成指定格式
                self.output.output_html()

if __name__=="__main__":
    spider_man=SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")

#!/usr/bin/python3
#-*- coding:utf-8 -*-

from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        urls=self.parser.parser_url(root_url,content)
        print(urls)
        #构造一个获取评分和票房链接
        for url in urls:
            try:
                t=time.strftime("%Y%m%d%H%M%S3282",time,localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api' \
                           '?Ajax_CallBack=true' \
                           '&Ajax_CallBackType=Mtime.Library.Services' \
                           '&Ajax_CallBackMethod=GetMovieOverViewRating' \
                           '&Ajax_CrossDomain=1' \
                           '&Ajax_RequestUrl=%s' \
                           '&t=%s' \
                           '&Ajax_CallBackArgument0-%s'%(url[0],t,url[1])
                rank_content = self.downloader.download(rank_url)
                print(rank_url,rank_content)
                data = self.parser.parser_json(rank_url,rank_content)
                self.output.store_data(data)
            except Exception as e:
                print("Crawl failed")

        self.output.output_end()
        print("Crawl finished")

if __name__=='__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing/')
        

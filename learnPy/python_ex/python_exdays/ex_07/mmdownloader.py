#!usr/bin/python3
# -*- coding:utf-8 -*-

from time import time
from threading import Thread

import requests

class DownloadHandler(Thread):
    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        filename = self.url[self.url.rfine('/')+1:]
        resp = requests.get(self.url)
        with open(r"E:/" + filename,"wb") as f:
            f.write(resp.content)

def main():
    #通过requests模块的get函数获取网络资源
    resp = requests.get("http://``````````")
    #将服务器返回的JSON格式的数据解析成字典
    data_model = resp.json()
    for mm_dict in data_model['newlist']:
        url = mm_dict['piUrl']
        #通过多线程方式实现图片下载
        DoqnloadHandler(url).start()

if __name__=='__main__':
    main()

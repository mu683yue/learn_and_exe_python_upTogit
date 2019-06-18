#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
爬虫练习-爬http://www.yiyoud.com/detail/66974网站的《九占》小说

version：1.0
date：2019/6/2

"""

import random
import requests
import re
import time

def test_getNovalContent():
	req1=requests.get("http://www.yznnw.com/files/article/html/9/9936/3367630.html")#先爬取楔子练手
	result1=req1.content.decode("gbk") #获取响应内容，并解码
	title_re=re.compile(r"<title>(.*?)</title>") #文章标题提取正则
	text_re=re.compile(r'</center>([\s\S]*?)</div>') #提取正文，由于正文有很多换行符，故要使用[\s\S]
	title = re.findall(title_re,result1)#找出标题
	text=re.findall(text_re,result1)#找出正文
	title=title[0] #由于返回的title是列表，所以取出title表第一项为文章标题
	text_list=[]#添加一个空列表，原来装处理后的正文
	print(title)
	for sentence in text:
	    #sentence=sentence.strip() #去掉每一句两边的空格
	    sentence=sentence.replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
	    sentence=sentence.replace("<br />","\t")
	    sentence=sentence.replace("热门推荐:","\t")
	    
	    print(sentence)
##	count = text_list.count('') #统计列表中空字符串
##	for i in range(count):
##	    text_list.remove('')
##	for sentence in text_list:
##	    print(sentence)

def getNovalList(firstUrl):
        req=requests.get(firstUrl,verify=False)
        result=req.content.decode("gbk")
        getlist_re=re.compile(r'<a href="([0-9]{8}.html)">')
        contents_list=re.findall(getlist_re,result)
        #print(contents_list)
        return contents_list

def getNoval(url,charSet,titleRe=r"<title>(.*?)</title>",textRe=r'<div id="content">([\s\S]*?)</div>'):
    header=[{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"},
                ]
    req_header={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "jieqiVisitId=article_articleviews%3D30527; Hm_lvt_a75168fb40a0ba6ad05a793b04d9d410=1559549103; Hm_lpvt_a75168fb40a0ba6ad05a793b04d9d410=1559549517",
        "Host": "www.45zw.la",
        "If-None-Match": "1559549166|",
        "Referer": "https://www.45zw.la/txt/30527/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }
    
    #req=requests.get(url,headers=header[0])
    req=requests.get(url,params=req_header,verify=False)
    result=req.content.decode(charSet) #获取响应内容，并解码
    title_re=re.compile(titleRe) #文章标题提取正则
    text_re=re.compile(textRe) #提取正文，由于正文有很多换行符，故要使用[\s\S]
    title= re.findall(title_re,result)#找出标题
    text=re.findall(text_re,result)#找出正文
    title=title[0] #由于返回的title是列表，所以取出title表第一项为文章标题
    text_list=[]#添加一个空列表，原来装处理后的正文
    print(title,end='\n')
    for sentence in text:
        sentence=sentence.strip() #去掉每一句两边的空格
        sentence=sentence.replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
        sentence=sentence.replace("<br/>","\t")
        sentence=sentence.replace("<br />","\t")
        sentence=sentence.replace("</div>","\t")
        print(sentence)
    time.sleep(2)
if __name__=='__main__':
        """
        爬取网站第一章和最后一章url：
        日照网在请求中必须有headers，其他小说网站可以不需要

        https://www.45zw.la/txt/30527/13765644.html 第一章
        https://www.45zw.la/txt/30527/17431132.html  最后一章
        
        """
####        first_url=r"https://www.45zw.la/txt/30527/"
####        list=getNovalList(first_url) #获取小说章节目录主页所有章节的链接号（格式：8位数字.html）
####
#####       test_getNovalContent()
##        file=r'D:\LHQ_develop\python_ex\python_exdays\九占'
##        fo=open(file,"a+")
        titleRe = r'<meta name="keywords" content="(.*?)" />'
        textRe = r'<div id="content"><p>([\s\S]*?)</p></div>'
        charset="utf-8"
        for i in range(0,101):
                url="https://www.smxs.cc/book/mrczfhyf/"+str(10010+10*i)+".html"
                #print(url)
                getNoval(url,charset,titleRe=titleRe,textRe=textRe)
##        #根据章节页来获取小说中正文和标题
##        for item in list:
##                url="https://www.45zw.la/txt/30527/"+str(item)
##                #print(url)
##                getNoval(url)








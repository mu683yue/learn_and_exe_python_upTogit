#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
爬虫练习-爬http://www.yiyoud.com/detail/66974网站的《九占》小说

version：1.4
date：2019/6/2
last modify time :2019/8/1

"""

import random
import requests
import re
import time

def test_getNovalContent():
	req1=requests.get("http://www.yznnw.com/files/article/html/9/9936/3367630.html")#先爬取楔子练手
	result1=req1.content.decode("gbk",errors="ignore") #获取响应内容，并解码
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


#获取小说主页面的各个分页url，以列表形式返回获取到的结果
def getNovalList(firstUrl,charSet,getlistRe):
        #req = requests.get(firstUrl,verify=False) #https且需要证书
        req = requests.get(firstUrl)   #http或https不需要证书
        result = req.content.decode(charSet,errors="ignore")
        getlist_re = re.compile(getlistRe)
        contents_list = re.findall(getlist_re,result)
        #print(contents_list)
        return contents_list

#获取玄界小说网小说简介
def get_bookintro(firstUrl,bookintroRe,charSet):

    #req = requests.get(firstUrl,verify=False) #https且需要证书
    req = requests.get(firstUrl)   #http或https不需要证书
    result = req.content.decode(charSet,errors="ignore")
    bookintro_re = re.compile(bookintroRe) #提取简介，由于正文有很多换行符，故要使用[\s\S]
    bookintro = re.findall(bookintro_re,result)#找出正文
    #bookintro_list = []#添加一个空列表，原来装处理后的正文
    print("小说简介：")
    for sentence in bookintro:
        sentence=sentence.strip() #去掉每一句两边的空格
        sentence=sentence.replace("&nbsp;","")
        sentence=sentence.replace("<br/>","\t")
        sentence=sentence.replace("<br />","\t")
        sentence=sentence.replace("</div>","\t")
        sentence=sentence.replace("&lt;/br&gt;&lt;/br&gt;","\t")
        print(sentence)
    time.sleep(2)

#获取小说各分页正文
def getNoval(url,charSet,titleRe,textRe):
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
    
    req=requests.get(url,headers=header[0])
    #req=requests.get(url,params=req_header,verify=False)
    while req.status_code == "503":
            time.sleep(20)  #爬取速度过快会服务器超时，添加等待时间

    result=req.content.decode(charSet,errors="ignore") #获取响应内容，并解码

    title_re=re.compile(titleRe) #文章标题提取正则
    text_re=re.compile(textRe) #提取正文，由于正文有很多换行符，故要使用[\s\S]
    title= re.findall(title_re,result)#找出标题
    text=re.findall(text_re,result)#找出正文
    title=title[0] #由于返回的title是列表，所以取出title表第一项为文章标题
    text_list=[]#添加一个空列表，原来装处理后的正文
    print(title,end='\n')
    for sentence in text:
        sentence=sentence.strip() #去掉每一句两边的空格
        sentence=sentence.replace("&nbsp;","")
        sentence=sentence.replace("&quot;","")
        sentence=sentence.replace("<br/>","\t")
        sentence=sentence.replace("<br />","\t")
        sentence=sentence.replace("</div>","\t")
        sentence=sentence.replace("&lt;/br&gt;","\t")
        print(sentence)
    time.sleep(2)
    return sentence
    
if __name__=='__main__':
        """
        爬取网站第一章和最后一章url：
        日照网在请求中必须有headers，其他小说网站可以不需要

        https://www.45zw.la/txt/30527/13765644.html 第一章
        https://www.45zw.la/txt/30527/17431132.html  最后一章

        
        """
        #玄界小说网站
        #first_url = r"http://www.xuanjiexiaoshuo.com/jKrV2/"
        first_url = r"http://www.shubao8.org/26/26928/"
        #getlistRe = r'<li><a href="([\w]{5,7}.html)">'
        getlistRe = r'<dd><a href="/26/26928/([\d]{7}.html)">'
        bookintro_re = r'<div id="bookintro"><p>([\s\S]*?)</p></div>'

        #titleRe = r'<meta name="keywords" content="(.*?)" />'
        titleRe=r"<title>(.*?)</title>"
        #textRe = r'<div id="content">([\s\S]*?)</div>'
        textRe =r'<div id="content">([\s\S]*?)</div>'
        charset="gbk"


        list=getNovalList(first_url,charSet=charset,getlistRe=getlistRe) #获取小说章节目录主页所有章节的链接号（格式：8位数字.html）
        #print(list)

        #测试获取页面内容是否成功
#####       test_getNovalContent()

        
        #直接根据有规律的url获取小说内容
        ##        for i in range(0,11):
##                url="https://www.234bqg.com/book_27731/"+str(6772997+i)+".html"
##                #print(url)
##                getNoval(url,charset,titleRe=titleRe,textRe=textRe)


         
                

        #小说简介
        #get_bookintro(first_url, bookintroRe=bookintro_re, charSet=charset)

        #根据章节页来获取小说中正文和标题
        for item in list:
                url=first_url+str(item)
                
                print(url)
                text = getNoval(url, charset, titleRe=titleRe, textRe=textRe)









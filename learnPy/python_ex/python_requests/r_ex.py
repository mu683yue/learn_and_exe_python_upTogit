#!/usr/bin/python3
#!-*- coding:utf-8 -*-

import requests

url='https://www.baidu.com'
r=requests.get(url,stream=True)
print(r.url)
print(r.encoding)
r.encoding='utf-8'
#print(r.text)
print(r.raw)

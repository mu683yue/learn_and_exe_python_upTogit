#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import json

#variables
baseurl='https://www.cloudscreen.com'

url='https://www.cloudscreen.com/cscapi/web/proxyHost'
host_email_header={'Content-Type':'application/json'}
host_email_param={'accessToken':'myj5uAZdakwTIvxawQ4Lnv','email':'cstest2@cloudscreen'}

host_email_r=requests.get(baseurl+'/cscapi/web/proxyHost',params=json.dumps(host_email_param))
print(host_email_r.url)
print(host_email_r.status_code)
print(host_email_r.json())

#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import json

basic_url="http://10.10.11.51:8090"
login_url="/1.0/user/login"
payload={"device_id":1,"login_name":'333@qq.com',"password":'123456'}

web=requests.post(url=basic_url+login_url,data=payload)
ty=web.text
print(web.text)
print(web.status_code)
print(web.data)

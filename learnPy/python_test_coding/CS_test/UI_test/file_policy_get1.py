#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import json

#variable
url='https://www.cloudscreen.com/fpc/web/policy/fetch'
json_head={'Content-Type':'application/json'}
json_str={'access_token': 'c45a07e6-f3bb-418c-bfc3-a66f6e0eca1a',
      'last_update': 7368116800122}

r=requests.post(url,data=json.dumps(json_str),headers=json_head)

print(r.status_code)
print(r.text)

#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
套接字-基于TCP协议创建时间客户端

version：1.0
date：2019\6\15
"""

from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('localhost',6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
client.close()

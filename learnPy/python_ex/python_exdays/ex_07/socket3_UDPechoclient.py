#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
套接字-基于TCP协议创建时间客户端

version：1.0
date：2019\6\15
"""
from socket import *

client=socket(AF_INET,SOCK_DGRAM)
while True:
    data_str=input("请输入：")
    client.sendto(data_str.encode("utf-8"),("localhost",6789))
    data,addr = client.recvfrom(1024)
    data_str = data.decode("utf-8")
    print("服务器回应：",data_str)
    if data_str == 'bye':
        break
client.close()

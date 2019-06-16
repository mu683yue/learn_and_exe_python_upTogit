#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
套接字-基于UDP协议创建Echo服务器

version：1.0
date：2019\6\15
"""

from socket import *
from time import *

server = socket(AF_INET,SOCK_DGRAM)
server.bind(("localhost",6789))
while True:
    data,addr = server.recvfrom(1024)
    server.sendto(data,addr)
server.close()

#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
套接字-基于TCP协议创建时间服务器

version：1.0
date：2019\6\15
"""

from socket import *
from time import *

#1、创建套接字对象并指定使用哪种传输服务
    #family=AF_INET -IPV4地址
    #family = AF_INET6 - IPV6地址
    #type = SOCK_STREAM - TCP套接字
    #type = SOCK_DGRAM - UDP套接字
    #type = SOCK_RAW - 原始套接字
server = socket(AF_INET,SOCK_STREAM)
#2、绑定IP地址和端口（区分不同的服务）
server.bind(('localhost',6789))
#3、开启监听 - 监听客户端连接到服务器
server.listen()
print("服务器已经启动正在监听客户端连接。")
while True:
    #accept方法是一个阻塞方法如果没有客户端连接到服务器
    #这个方法就会阻塞代码不会往下执行
    #accept方法返回元组，其中的第一个元素是客户端对象
    #第二个元素是客户端地址（由IP和端口两部分构成）
    client,addr = server.accept()
    print("客户端%s:%d连接成功。" % (addr[0],addr[1]))
    currtime = localtime(time())
    timestr = strftime("%Y-%m-%d %H:%M:%S",currtime)
    #5、发送数据
    client.send(timestr.encode("utf-8"))
    #6、断开连接
    client.close()
server.close()

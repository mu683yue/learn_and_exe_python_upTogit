#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用socketserver模块创建时间服务器

version：1.0
date：2019\6\15
"""

from socketserver import TCPServer,StreamRequestHandler
from time import *

class EchoRequestHandler(StreamRequestHandler):
    def handler(self):
        currtime = localtime(time())
        timestr=strftime("%Y-%m-%d %H-%M-%S" % currtime)
        self.wfile.write(timestr.encode("utf-8"))

server=TCPServer(("localhost",6789),EchiRequestHandler)
server.serve_forever()

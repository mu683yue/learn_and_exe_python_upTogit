#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os

BASE_PATH = os.path.dirname(
    os.path.dirname = (os.path.abspath(__file__))
    ) #找到APT这个文件夹的地址
LOG_PATH = os.path.join(BASE_PATH,'log')  #拼接出存放日志的路径
CASE_PATH = os.path.join(BASE_PATH,'cases') #拼接处存放用例的路径

LEVEL = 'debug' #日志级别
LOG_NAME = 'apt.log' #日志文件名

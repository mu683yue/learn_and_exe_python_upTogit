#!/usr/bin/python3
# -*- coding:utf-8 -*-

import logging
import time

import os

def get_log(logname):

    #创建一个logger
    logger = logging.getLogger(logname)
    logger.setLevel(logging.INFO)

    #设置日志存放路径，日志文件名
    #获取本地时间，转换为设置的格式
    rq = time.strftime('%Y-%m-%d %H%m',time.localtime(time.time()))
    #设置所有日志存放路径
    path = os.path.join(os.getcwd(),"Logs/")

    #设置日志文件名
    log_name = path + rq +'.log'

    #创建handler
    #创建一个handler写入所有日志
    fh = logging.FileHandler(log_name)
    fh.setLevel(logging.DEBUG)
    #创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    #定义日志输出格式
    #以时间-日治其名称-日志级别-日志内容的形式展示
    log_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    #将定义号的输出形式添加到handler
    fh.setFormatter(log_formatter)
    ch.setFormatter(log_formatter)

    #给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
    

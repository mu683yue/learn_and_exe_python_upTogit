#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
这个模块主要内容是记录日志的功能。
构造一个可实例化的类，实例化后在其他模块可以直接调用生成相应等级的日志。
"""
import logging
import os
from logging import handles
from config import setting

class MyLogger(object):
    def __init__(self,file_name,level='info',backCount=5,when='D'):
        logger = logging.getLogger()
        logger.setlevel(self.get_level(level))   #设置日志的级别
        cl = logging.StreamHandler()   #负责往控制台输出
        bl = handlers.TimedRotatingFileHandler(filename=file_name,when=when,interval=1,
        										backupCount=backCount,encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineo)d]-%(levelname)s:%(message)s')
        #指定日志的格式
        cl.setFormatter(fmt) #设置控制台输出的日志格式
        bl.setFormatter(fmt) #设置文件里写入日志的格式
        logger.addHandler(cl) #把已经设置好的日志放入
        logger.addHandler(bl) #同上

    def get_level(self,sss):
       	level = {
       		'debug': logging.DEBUG,
       		'info': logging.INFO,
       		'warn': logging.WARN,
       		'error':logging.ERROR
       	}
       	sss = sss.lower()
       	return level.get(sss)

path = os.path.join(setting.LOG_PATH, setting.LOG_NAME)  #拼接好日志的绝对路径
apt_log = MyLogger(path,setting.LEVEL).logger
#直接在这边实例化，并.logger，使用时就可以直接apt_log.warning了




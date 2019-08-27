#!/usr/bin/python3
#-*- coding:utf-8 -*-
import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):
        """
            指定日志的文件路径，日志级别，调用它文件
            将日志存入指定的目标路径
        """

        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setlevel(logging.DEBUG)

        #创建一个handler,用于写入日志文件
        rq = time.strftime("%Y%m%d%H%M%S",time.localtime())
        #项目目录下的/Logs，保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger
    
        

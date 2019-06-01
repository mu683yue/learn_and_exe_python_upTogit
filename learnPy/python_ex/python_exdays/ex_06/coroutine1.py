#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用协程 - 模拟快递中心派发快递
        -查看协程状态
version:1.0
date:2019\6\1
"""

from time import sleep
from random import random
from inspect import getgeneratorstate

def build_deliver_man(man_id):
    total=0
    while True:
        total+=1
        print("%d快递员准备接今天的第%d单。" % (man_id,total))
        pkg = yield
        print("%d号快递员收到编号为%s的包裹。" % (man_id,pkg))
        sleep(random() *3)

def package_center(deliver_man,max_per_day):
    num = 1
    #创建状态（Gen_CREATED） - 等待开始执行
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    #挂起状态（Gen_SUSPENDED) - 在yield表达式处暂停
    print(getgeneratorstate(deliver_man))
    #next(deliver_man)
    while num <= max_per_day:
        package_id = "PKG-%d" % num
        deliver_man.send(package_id)
        num+=1
        sleep(0.1)
    deliver_man.close()
    #结束状态（Gen_CLOSED）-执行完毕
    print(getgeneratorstate(deliver_man))
    print("今天的包裹派送完毕！")

if __name__=='__main__':
    dm=build_deliver_man(1)
    package_center(dm,10)

#两个函数虽然没有调用关系但是创建快递员的函数作为一个协程协助了快递中心函数完成任务


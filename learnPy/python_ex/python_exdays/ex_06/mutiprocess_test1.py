#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用多进程多复杂任务进行“分而治之”
完成1~100000000求和的计算密集型任务：
"""

from time import time
from multiprocessing import Process,Queue
from random import randint

def time_cosuming():
    """
    比较耗时的方法
    """
    total=0
    number_list=[x for x in range(1,100000001)] #创建列表填入100000000个数比较耗时
    start=time()
    for number in number_list:
        total+=number
    print(total)
    end=time()
    print("Execution time:%.3fs" % (end-start))

def task_handler(curr_list,result_queue):
    total=0
    for number in curr_list:
        total+=number
    result_queue.put(total)

def need_less_time_perform():
    '''
    将这个任务分解到8个进程中去执行的时候，
    我们暂时也不考虑列表切片操作花费的时间，
    只是把做运算和合并运算结果的时间统计出来.
    '''
    process=[]
    number_list=[x for x in range(1,100000001)]
    result_queue=Queue()
    index=0
    #启动8个进程将数据切片后运算
    for _ in range(8):
        p=Process(target=task_handler,args=(number_list[index:index+12500000],))
        index += 12500000
        process.append(p)
        p.start()
    #开始记录多有进程执行完成需要花费的时间
        start=time()
        for p in process:
            p.join()
        #合并执行结果
        total=0
        while not result_queue.empty():
            total+=result_queue.get()
        print(total)
        end=time()
        print("Execution time:",(end-start),'s',sep='')
        

if __name__=='__main__':
    """
    比较两段代码的执行结果,，使用多进程后由于获得了更多的CPU执行时间以及更好的
    利用了CPU的多核特性，明显的减少了程序的执行时间，而且计算量越大效果越明显。
    当然，如果愿意还可以将多个进程部署在不同的计算机上，做成分布式进程，
    具体的做法就是通过multiprocessing.managers模块中提供的管理器将Queue对象
    通过网络共享出来（注册到网络上让其他计算机可以访问）
    """
    need_less_time_perform()

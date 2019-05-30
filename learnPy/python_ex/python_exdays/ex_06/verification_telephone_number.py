#!usr/bin/python3
#-*- coding:utf-8 -*-

"""
创建正则表达式，使用前瞻和后顾来保证手机号前后不应该出现数字
version:1.0
date:2019\5\30
"""
import re

def main():
    pattern=re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence='''
    重要的事说8140123456789遍，
    文档手机号是13512346789这个号，不是15600998765，也不是110或119，
    王大锤的手机号才是15600998765。
    '''
    #查找所有匹配并保存到一个列表中
    mylist=re.findall(pattern,sentence)
    print(mylist)
    print("----------分割线----------")
    #通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print("----------分割线----------")
    #通过search函数指定搜索位置找出所有匹配
    m=pattern.search(sentence)
    while m:
        print(m.group)
        m=pattern.search(sentence,m.end())

if __name__=='__main__':
    main()

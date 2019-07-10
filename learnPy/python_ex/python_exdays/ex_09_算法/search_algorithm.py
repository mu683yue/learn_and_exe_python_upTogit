#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
查找算法
-顺序查找 seq_search
-折半查找 bin_search

author:LHQ
date:2019\7\10
version:1.0
"""

def seq_search(items,key):
    """顺序查找"""
    for index,item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items,key):
    """折半查找"""
    start,end = 0,len(items)-1
    while start <= end:
        mid = (start + end)//2
        if key > items[mid]:
            start = mid +1
        elif key < items[mid]:
            end = mid -1
        else:
            return mid
    return -1
    


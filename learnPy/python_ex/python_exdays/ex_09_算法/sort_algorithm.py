#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
排序算法
-简单选择排序 select_sort
-冒泡排序 bubber_sort
-归并排序  merge_sort
-快速排序 quik_sort
"""

def select_sort(origin_items,comp=lambda x,y:x<y):
    '''
    简单选择排序：
    共n个数。每次选择最小的元素与第i个元素互换，如此n-1趟后排序完成。
    '''
    items = origian_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(item)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],itmes[min_index] = items[min_index],items[i]
    return items

def bubber_sort(origin_items,comp = lambda x,y:x>y):
    '''
    高质量冒泡排序（搅拌排序）：
    共n个数。
    遍历若干次要排序的数列，每次遍历时，它都会从前往后依次的比较相邻两个数的大小；
    如果前者比后者大，则交换它们的位置。这样，一次遍历之后，最大的元素就在数列的末尾！
    采用相同的方法再次遍历时，第二大的元素就被排列在最大元素之前。
    重复此操作，直到整个数列都有序为止！
    '''
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i,len(items)-1-i): #将最大的数挪到末尾
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True #若发生交换，标记为True
            if swapped:
                swapped = False
                for j in range(len(items)-2-i,i,-1): #len(items)-2-i~i-1,倒着取数
                    if comp(items[j-1],items[j]):
                        items[j],items[j-1] = items[j-1],items[j]
                        swapped = True
            if not swapped:
                break #没有发生交换，说明已经有序
    return items

def merge_sort(items, comp =lambda x,y:x<y):
    '''
    归并排序（分治法）
    '''
    if len(items<2):
        return items[:]
    mid = len(items)//2
    left = merge_sort(items[:mid],comp)   #递归
    right = merge_sort(items[mid:],comp)
    return merge(left,right,comp)
def merge(items1,items2,comp):
    '''
    合并（将两个有序的列表合并成一个有序的列表）
    '''
    items = []
    index,index2=0,0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[inex2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 2        
    items += items[index1:]
    items += items[index2:]
    return items


#快速排序-选择去留对元素进行划分，左边都比枢纽小，右边都比枢纽大
def quick_sort(origin_items,comp = lambda x,y:x<=y):
    items = origin_items[:]
    _quick_sort(items,0,len(items)-1,comp)
    return items
def _quik_sort(items,start,end,comp):
    if start < end:
        pos = _partition(items,start,end,comp)
        _quick_sort(items,start,pos-1,comp)
        _quick_sort(items,pos+1,end,comp)
def _psrtition(items,start,end,comp):
    pivot = items[end]
    i = start-1
    for j in range(start,end):
        if comp(items[j],pivot):
            i += 1
            items[i],items[j] = items[j],items[i]
    items[i+1],itmes[end] = items[end],items[i]
    return i+1
        


    
    
                
        
    
    

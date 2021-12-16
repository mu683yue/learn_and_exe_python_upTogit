#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    合并排序
方法：
    （1）分解。将待排序的n个元素分成规模大致相同的2个子序列，即从中间一分为二，2个子序列的元素个数要么相等，要么相差1个元素。
    （2）治理。递归解决2个子问题。2个子序列有序了，然后将排好序的2个子序列合并成1个有序的序列，即原问题的解。

"""

def merge(arr,left,mid,right):
    '''
    :param arr: n个元素存储的列表。
    :param left: 子问题的下边界。
    :param mid:
    :param right: 子问题的上边界。
    :return: 排好序的序列arr[left:right]
    '''
    n1 = mid - left +1    #子问题1的元素个数
    n2 = right - mid      #子问题2的元素个数
    #创建临时数组L用于存储子问题1的元素，R用于存储子问题2的元素。
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    #归并临时数组到arr[l:r]
    i = 0   #初始化第一个子问题的索引
    j = 0    #初始化第二个子问题的索引
    k = left      #初始归并子数组的索引
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #拷贝L[]的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    print(arr)

def mergeSort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)     #将2个子问题发解合并成原问题的解

if __name__=="__main__":
    arr = [12,11,13,5,6,12,7,20,10,100,34]
    n = len(arr)
    mergeSort(arr,0,n-1)
    print(arr)
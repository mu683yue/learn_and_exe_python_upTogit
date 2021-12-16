#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    快速排序
    一种划分排序。基本思想：通过一趟扫描，将待排序的元素分成独立的3个序列：第一个序列中所有元素均不大于基准元素、第二个序列
    是基准元素、第三个序列中所有元素均大于基准元素。由于第2个序列已经处于正确的位置，因此需要再按此方法对第一个序列和第三个序列、
    分别进行排序，整个排序过程可以递归进行，最终可使整个序列变成有序序列。
方法：


"""

def partution(lis,left,right):
    '''
    :param lis: 待排序元素
    :param left: 起始索引
    :param right: 结束索引
    :return: 基准元素的位置
    '''
    i = left
    j = right + 1
    pivot = lis[left]   #用列表的的第一个元素作为基准元素
    while(True):
        i += 1
        while(lis[i] < pivot):   #从前往后扫描，找到比基准元素大的停止，该元素的位置不变
            i += 1          #向右推动指针
        j -= 1              #向左推动指针
        while(lis[j] > pivot):   #从后往前扫描，找到比基准元素小的为止，该元素的位置不变
            j -= 1
        if (i>j):
            break
        lis[i],lis[j] = lis[j],lis[i]   #交换lis[i]和lis[j]，交换后的i加1
    lis[j],lis[left] = lis[left],lis[j]
    return j

def quickSort(lis,left,right):
    if left < right:
        j = partution(lis,left,right)
        quickSort(lis,left,j-1)
        quickSort(lis,j+1,right)

if __name__=="__main__":
    arr = [54,26,37,12,3,26,77,3,22,13]
    n = len(arr)
    quickSort(arr,0,n-1)
    print("排序后的数组：",arr)
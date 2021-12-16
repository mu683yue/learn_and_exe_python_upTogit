#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    线性时间选择-找第k小的问题

方法：
    （1）分解。选取基准元素，将待排序序列中的元素与基准元素比较，不大于基准元素的组成一个子序列，大于基准元素的组成另一个子序列。
    （2）治理。检查基准元素的位置与k的大小关系，若两者相等，则基准元素就是要找的第k小的元素；若基准元素的位置大于k,则在不
    大于基准元素的子序列中找第k小；若基准元素的位置小于k,则在大于基准元素的子序列中找第（k-基准元素位置）小的元素.


"""

def local_sort(A,left,right):
    """
    采用插入排序完成组内元素排序
    :param A: 待排序元素
    :param left:
    :param right:
    :return: 排序好的A
    """
    for j in range(left+1,right+1):
        x = A[j]
        for i in range(j,left-1,-1):
            if A[i-1]>x:
                A[i] =A[i-1]
            else:
                break
        A[i] = x
    return A

def partition(A,left,right,p):
    """
    以A中第p个元素为基准，将A划分为大于基准元素的子序列和小于基准元素的子序列.
    :param A:
    :param left:
    :param right:
    :param p:
    :return: 划分后基准元素的位置
    """
    i = left
    j = right+1
    A[left],A[p] = A[p],A[left]
    pivot  = A[left]   #记录基准元素
    while(True):
        i += 1
        while(A[i] < pivot):
            i += 1
        j -= 1
        while(A[j]>pivot):
            j -=1
        if (i>j):
            break
        A[i],A[j] = A[j],A[i]
    A[j],A[left] = A[left],A[j]
    return j

def select(A,left,right,k):
    n = right - left + 1  #A[p]到A[r]的长度
    if n == 1:
        return left
    if n < 5:
        local_sort(A,left,right)
        return left+k-1

    groups = n//5
    for i in range(1,groups+1):
        A = local_sort(A,left+5*(i-1),left+5*i-1)  #逐段对每5个元素进行插入排序
        A[left+i-1],A[left+5*i-3] = A[left+5*i-3],A[left+i-1]  #记录每组中位数
    j = select(A,left,left+groups-1,groups//2)
    print("j=",str(A[j]))
    q = partition(A,left,right,j)
    print("q=",str(q))
    print(A)
    i = q-left+1
    if k == i:
        return q
    if k < i:
        return select(A,left,q-1,k)
    if k > i:
        return select(A,q+1,right,k-i)

if __name__=="__main__":
    A = [88,34,46,23,57,879,45,34,8,98,3]
    k =select(A,0,len(A)+1,4)
    print(f"第{str(k+1)}小元素为：{str(A[k])}")

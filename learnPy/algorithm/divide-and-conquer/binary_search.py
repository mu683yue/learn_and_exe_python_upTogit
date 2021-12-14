#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    二分查找（折半查找）
    假定用a_list表示n个元素的有序序列，该序列由小到大排序。
    （1）分解。将有序序列分成规模大致相等的两部分，即每部分的规模大致为n/2。
    （2）治理。用有序序列的中间位置的元素与特定元素x比较，如果x等于中间元素，那么算法终止；如果x小于中间元素，那么在序列
        的左半部递归查找；否则，在序列的右半部递归查找。递归终止的条件是序列规模为0或1。

伪代码：
算法：binary_search(a_list,left,right,x)
输入：a_list,left,right,x
输出：x在序列a_list中的位置或-1
if left >right then
    return -1
mid <- (left+right)/2
if x == a_list[mid] then
    return mid
if x<a_list[mid] then
    return  binary_search(a_list,left,mid-1,x)
else
    return binary_search(a_list,mid+1,right,x)


"""

def binary_search(lis,left,right,num):
    if left > right:        #递归结束条件
        return -1
    mid = (left+right)//2    #分解操作
    print(mid)
    if num < lis[mid]:
        return binary_search(lis,left,mid-1,num)
    elif num > lis[mid]:
        return binary_search(lis,mid+1,right,num)
    else:
        return mid

if __name__=="__main__":
    lis = [11,32,51,21,42,9,5,6,7,8]
    lis.sort()
    print(lis)
    left = 0
    right = len(lis) - 1
    num = 8
    res = binary_search(lis,left,right,num)
    print("list[" + str(res) + "]=" + str(num))


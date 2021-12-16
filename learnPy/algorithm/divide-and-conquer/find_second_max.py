#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    找第二大元素

步骤：
    （1）分解。一分为二
    （2）治理。递归两个子问题，分别找出2个子问题的最大值，同时将被淘汰的较小元素记录在较大元素列表中。比较子问题的最大值，取
    较大元素为问题的最大值。在淘汰的元素列表找出最大值即为较小值。

"""

def find_max(a_list,left,right):
    global dic
    if left >= right:
        return a_list[left]
    mid = (left + right)//2
    left_max = find_max(a_list,left,mid)
    right_max = find_max(a_list,mid+1,right)
    if left_max > right_max:
        dic[left_max].append(right_max)    #将right_max插入到left_max的淘汰元素列表中
        return left_max                   #返回最大元素
    else:
        dic[right_max].append(left_max)
        return right_max

def find_second(n_max):
    n = len(n_max)
    second_max = n_max[0]
    for i in range(1,n):
        if n_max[i] > second_max:
            second_max = n_max[i]
    return second_max

if __name__=="__main__":
    a_list = [6,12,3,7,12,18,90,87,54,23]
    n = len(a_list)
    dic = {}
    for i in range(n):
        dic.update([(a_list[i],[])])  #初始化字典列表
    print(dic)
    first_max = find_max(a_list,0,n-1)
    second_max = find_second(dic[first_max])
    print("最大值的淘汰元素为：",dic[first_max])
    print("第二大元素为：",second_max)



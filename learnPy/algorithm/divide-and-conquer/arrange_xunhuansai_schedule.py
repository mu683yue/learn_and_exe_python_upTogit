#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    循环赛日程表问题
    设有n=2的k次方个运动员要进行羽毛球循环比赛，现要设计一个满足以下要求的比赛日程表：
        （1）每个选手必须与其他n-1个选手各比赛一次；
        （2）每个选手一天只能比赛一次；
        （3）循环赛一共要进行n-1天；
        由于n=2的k次方，n为偶数。


"""

def arrange(p,q,n,arr):
    if (n>1):                       #规模大于1，分解
        arrange(p,q,n//2,arr)       #递归解决子问题
        arrange(p,q+n//2,n//2,arr)
    #两组对打
    #填左下角
        for i in range(p+n//2,p+n):
            for j in range(q,q+n//2):
                arr[i][j] = arr[i-n//2][j+n//2]
            #填右下角
        for i in range(p+n//2,p+n):
            for j in range(q+n//2,q+n):
                arr[i][j] = arr[i-n//2][j-n//2]
    return arr

if __name__=="__main__":
    import numpy as np
    k = 4
    n = 2**k
    arr = np.zeros((n,n),dtype=int)
    for i in range(n):
        arr[0][i] = i+1
    arrange(0,0,n,arr)
    print(arr)
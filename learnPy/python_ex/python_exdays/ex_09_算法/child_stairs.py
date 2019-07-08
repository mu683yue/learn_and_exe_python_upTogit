#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
题目描述:

有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
实现一个算法，计算小孩有多少种上楼梯的方式。输入n，返回一个整数。

"""

def countSteps(n):
    """
    算法:
    假定n = 4:则可以看作走了1阶后再走3阶，也可以看作走了2阶后再走2阶，也可以看作走了3阶后再走1阶

    因此f(4) = f(1)+f(2)+f(3)，f(n) =f(n-1)+f(n-2)+f(n-3)

    递归的结束条件：

    n ==1:上台阶方法为走1，因此return 1

    n ==2:上台阶方法为走11，2，因此return 2

    n ==3:上台阶方法为走111，12，21，3，因此return 4

    本层递归要做什么：

    本层n阶台阶的情况下，计算上楼梯的方式

    本层递归的返回值：

    返回n-1,n-2,n-3阶情况下的上楼梯方式总和
    """
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return countSteps(n-1)+countSteps(n-2)+countSteps(n-3)

def get_stepResult(n):
    """
    进阶思考:

    如何查看n阶台阶的情况下上楼梯的具体方式，即求出具体的上楼梯方式。

    进阶算法:

    已知上楼梯的方式有3种---1阶2阶3阶，因此此题可以转换为，输入一个n,求由1，2，3三个数组成和为n的组合结果。

    用回溯法解此题，使用temp记录已爬楼梯阶数和：

    爬楼梯的方式可以爬1，2，3阶3种方式；

    当已爬楼梯和小于n的时候继续爬楼梯；

    当已爬楼梯和等于n的时候记录当前爬楼梯的组合方式放入结果列表中；

    当爬楼梯和大于n的时候剪枝，不再继续爬楼梯；
    """
    result = []
    def detailSteps(n,temp=''):
        if sum([int(x) for x in temp])==n:
            result.append(temp)
            return
        if sum([int(x) for x in temp])>n:
            return
        for i in range(1,4):
            detailSteps(n,temp+str(i))
    detailSteps(n)
    return result


if __name__ == '__main__':
    print(countSteps(2))
    print(get_stepResult(5))
    print(len(get_stepResult(5)))

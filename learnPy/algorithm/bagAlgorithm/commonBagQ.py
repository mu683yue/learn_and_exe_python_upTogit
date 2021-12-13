#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    背包问题
    n个物品和1个被包。都物品i(i=1,2,3,```,n),其价格为Vi,重量为Wi,背包的容量为W.物品可分割,如何选择，使选入背包的总价值最大。
    选择单位价值最大的物品优先装入背包。

伪代码：
算法:knapsack(v[1,2,```,n],w[1,2,```,n])
输入:物品集合，物品重量，物品价值，背包装载能力
i<-1
while i<=n do
    a[i] <- v[i]/w[i]
    i <- i+1
sort a   //按照单位重量的价值从大到小排列
w<- 0
while i<=n and w+w[i]<=W do
    x[1] <-1
    w <- w[i] +w
    p <- p + v[i]
    i <- i+1
if i <=n then
    x[i] <- (W-w)/w[i]
    p <- p + x[i]*v[i]
return x,p
"""


def knapsack(capacity=0,goods_set=[]):
    #按照单位价值排序
    goods_set.sort(key=lambda goods:goods[1]/goods[2],reverse=True)

    result = []       #装入背包的物品集
    sum_v = 0
    for goods in goods_set:
        if capacity < goods[2]:
            result.append([goods[0],capacity*goods[1]/goods[2],capacity])   #分割一部分装入
            sum_v += capacity * goods[1]/goods[2]
            break
        result.append(goods)
        sum_v += goods[1]
        capacity -= goods[2]
    return result,sum_v

if __name__=="__main__":
    some_goods = [(0,4,2),(1,6,8),(2,3,5),(3,8,2),(4,2,1)]
    res,sum_v = knapsack(6,some_goods)
    for goods in res:
        print('物品编号：'+str(goods[0]) + ',放入重量：' + str(goods[2]) + ',放入价值：' + str(goods[1]))
    print("总价值为：" +str(sum_v))

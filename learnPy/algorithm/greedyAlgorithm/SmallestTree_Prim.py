#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    最小生成树-Prim算法
    从图的顶点出发，紧扣最小生成树的性质，把顶点集分成2个互不相交的集合，贪心选择两个集合最小权的边加入到最小生成树中。
    用list存储closest、lowcost、集合U、集合V、最小生成树T。Prim算法适用于稠密图，所以选用邻接矩阵数据结构存储图。
步骤：

伪代码:
输入：无向带权图G
输出：最小生成树T
U <-{1},T <- {}
for i <- 1 to n do
    if w(1,i)<wq then
        closest[i] <- 1
        lowcost <- w(1,i)
while V-U != None do
    从V-U中选择最小的lowcost[j]
    U <- U + {j}
    T <- T + {(closest[j],j)}
    for i <- 1 to n do
        if i (属于) V-U and w(j,i)<lowcost[i]
            closest[i] <- j
            lowcost <- w(j,i)
return T
"""

import sys
def Prim_mst(graph,vertexs):
    ulist = []
    ulist.append(vertexs[0])         #集合U
    tree_list = []                   #最小生成树
    closest = []                    #closest[i]表示生成树集合中与点i最近的点的编号
    lowcost = []                     #lowcost[i]表示生成树集合中与点i最近的点构成的边
                                     #最小权值-1表示i已经在生成树集合中
    lowcost.append(-1)
    closest.append(0)
    n = len(vertexs)
    for i in range(1,n):             #初始化closest和lowcost数组
        lowcost.append(graph[0][i])
        closest.append(0)
    sum = 0
    for _ in range(1,n):            #n-1次贪心选择
        minid = 0                   #记录V-U中顶点最近的U中的顶点编号
        min = sys.maxsize           #系统最大值，相当于无穷大
        for j in range(1,n):        #寻找每次插入生成树的权值最小lowcost
            if (lowcost[j]!=-1 and lowcost[j]<min):
                minid = j
                min = lowcost[j]
        ulist.append(vertexs[minid])
        tree_list.append([vertexs[closest[minid]],vertexs[minid],lowcost[minid]])
        sum += min
        lowcost[minid] = -1
        for j in range(1,n):        #更新插入节点后lowcost和closest的值
            if(lowcost[j] != -1 and lowcost[j]>graph[minid][j]):
                lowcost[j] = graph[minid][j]
                closest[j] = minid
    return sum,tree_list

if __name__=="__main__":
    graph = [[0,54,32,70,50,60],[54,0,21,58,76,69],[32,21,0,35,67,66],
             [7,58,35,0,50,62],[50,76,67,50,0,14],[60,69,66,62,14,0]]
    vertexs = ['A','B','C','D','E','F']
    sum,tree_list = Prim_mst(graph,vertexs)
    for edge in tree_list:
        print(edge[0] + '--' + edge[1] + '权:' + str(edge[2]))
    print('树的耗费：',sum)



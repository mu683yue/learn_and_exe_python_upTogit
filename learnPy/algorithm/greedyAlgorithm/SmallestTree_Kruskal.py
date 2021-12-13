#!usr/bin/python3
#-*- coding=utf-8 -*-

"""
说明：
    最小生成树-Kruskal算法
    从图的边出发，选择权最小的边，判断该边的两个端点是否在一个连通分支，若在，则舍弃该边。
    设图G=(V,E)是五向连通带权图,V={1,2,```,n;设最小生成树T=(V,TE)
步骤：

伪代码：
输入:图G=(V,E)
输出:最小生成树T
sort(E)            //E为边集，按照边权由小到大排序
T <- None
j <- 0            //记录加入的边的条数
for i <-1 to n do
    e<-E[i]
    if e 的两个端点不在同一个连通分支
    then
        T<-{e}
        j<-j+1
    if j=n-1
        break;
return T

"""

#定义一个kruskal函数，接收图的顶点集vertexs和边集edge_list,返回最小生成树tree_mst.

def kruskal(edge_list,vertexs):
    vertex_num = len(vertexs)
    edge_num = len(edge_list)
    tree_mst = []
    if vertex_num <= 0 or edge_num < vertex_num-1:
        return tree_mst
    edge_list.sort(key = lambda a:a[2])    #按照边权从小到大排列
    group = [[i] for i in range(1,vertex_num+1)]      #初始化，将图G的顶点看成n个孤立分支
    for edge in edge_list:
        k = len(group)                               #获取分支数
        if k == 1:                                   #若只有一个分支，结束
            break
        for i in range(k):                          #判断两个端点是否属于同一个分支
            if edge[0] in group[i]:
                m = i
            if edge[1] in group[i]:
                n = i
        if m!=n:
            tree_mst.append(edge)                    #如果不在同一个分支，将边加入到最小生成树中
            group[m] = group[m] + group[n]           #合并分支
            group.remove(group[n])
    return tree_mst

if __name__=="__main__":
    edge_list = [(1,2,6),(1,3,1),(1,4,5),(2,3,5),(2,5,3),(3,4,5),(3,6,4),(3,5,6),(4,6,2),(5,6,6)]
    vertexs = [1,2,3,4,5,6]
    tree_mst = kruskal(edge_list,vertexs)
    for edge in tree_mst:
        print(edge)
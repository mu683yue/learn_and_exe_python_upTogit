#!/usr/bin/python3
# -*- coding:utf-8  -*-

from random import randint

def chicken():

    """
    求解《百钱百鸡》问题
    公鸡5元/只，母鸡3元/只，小鸡1元/3只，用100元买100只鸡
    问：公鸡、母鸡、小鸡各多少只

    """
    for x in range(0,20):
        for y in range(0,33):
            z=100-x-y
            if 5*x+3*y+z/3==100:
                print("100元可以买公鸡%d只，母鸡%d只，小鸡%d只。"%(x,y,z))

def Craps():
    """
    Craps赌博游戏
    玩家摇2颗色子，如果第一次摇出7点或11点，玩家胜；
    如果摇出2点、3点、12点，庄家胜，其他情况游戏继续。
    玩家再次摇筛子，如果摇出7点，庄家胜；
    如果摇出第一次摇的点数，玩家胜
    否则游戏继续，玩家继续摇色子。
    玩家进入游戏时有1000元赌注，全部输光游戏结束。
    
    version:1.0
    date:2019/5/21
    ms:需要修改，有BUG
    """
    print("""欢迎，你有1000元赌注。
    游戏规则为：玩家摇2颗色子，如果第一次摇出7点或11点，玩家胜；
    如果摇出2点、3点、12点，庄家胜，其他情况游戏继续。
    玩家再次摇筛子，如果摇出7点，庄家胜；
    如果摇出第一次摇的点数，玩家胜
    否则游戏继续，玩家继续摇色子。
    玩家进入游戏时有1000元赌注，全部输光游戏结束。""")
    money = 1000
    while money>0:
        print("您的总资产：",money)
        needs_go_on=False
        while True:
            debt=int(input("请下注："))
            if debt < 0 and debt >=money:
                break
            first = randint(1,6)+randint(1,6)
            print("玩家摇出了%d点" % first)
            if first==7 or first ==11:
                print("玩家胜")
                money+=debt
            elif first==2 or first==3 or first==12:
                print("庄家胜")
                money-=debt
            else:
                needs_go_on=True

            while needs_go_on:
                current=randint(1,6)+randint(1,6)
                print("玩家摇出了%d点" % current)
                if current==7:
                    print("庄家胜")
                    money-=debt
                    needs_go_on=False
                elif current==first:
                    print("玩家胜")
                    money+=debt
                    needs_go_on=False
    print("你破产了，游戏结束！")

def Fibonacci():
    """
    输出斐波那契数列的前20个数：
    1 1 2 3 5 8 13 21 ····

    version:1.0
    date:2019/5/21
    
    """
    num=20
    a=0
    b=1
    for _ in range(num):
        (a,b) = (b,a+b)
        print(a,end=' ')  #效果等同于print("%d " % a)
                    









    
if __name__=='__main__':
    #chicken()
    #Craps()
    #Fibonacci()

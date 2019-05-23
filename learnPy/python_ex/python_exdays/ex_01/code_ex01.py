#!/usr/bin/python3
# -*- coding:utf-8  -*-

from random import randint
import math

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
                    break
                elif current==first:
                    print("玩家胜")
                    money+=debt
                    needs_go_on=False
                    break
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


def Guess_num():
    """
    猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别提示大一点\小一点\猜对了
    
    version：1.0
    date：2019-5-22
    """
    rand_num=randint(1,100)
    counter = 0
    while True:
        counter+=1
        guess_num=int(input("输入你才的1到100的数字："))
        if guess_num<1 or guess_num>100:
            print("数字超出游戏范围！")
            break
        if guess_num>rand_num:
            print("大了")
        elif guess_num<rand_num:
            print("小了")
        else:
            print("猜对了")
            break
    print("您一共猜了%d次！" % counter)
    if counter > 10:
        print("笨蛋")

def Daffodil():
    """
    找出100~999之间的所有水仙花数
    水仙花数是各位立法和等于这个数本身的数
    如：153 = 1**3 + 5**3 + 3**3

    version：1.0
    date：2019\5\22
    
    """
    for num in range(100,999):
        low=num%10
        mid=num//10%10
        high=num//100

        if num==low**3 + mid**3 + high**3:
            print(num)

def palindrome():
    """
    判断输入的正整数是不会回文数
    回文数指将一个正整数从左到右排列和从右到左排列是一样的数

    version:1.0
    date:2019\5\22
    """
    num = int(input("请输入正整数"))
    temp=num
    num2=0
    while temp>0:
        num2*=10
        num2+=temp%10
        temp//=10
    if num==num2:
        print("%d是回文数"% num)
    else:
        print("%d不是回文数"% num)

def perfect_num():
    """
    找出1~9999之间的完美数
    完美数：除自身外的其他所有因子的和正好等于这个数本身的数
    例如：6=1+2+3,28=1+2+7+14

    version：1.0
    date：2019\5\22
    """
    for num in range(1,9999):
        sum=0
        for factor in range(1,int(math.sqrt(num))+1):
            if num%factor==0:
                sum +=factor
                if factor >1 and num/factor!=factor:
                    sum+=num/factor            
        if sum==num:
            print(num)

def yanghui():
    """
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...
"""
    num=int(input("Number of rows"))
    yh = [[]]*num
    for row in range(len(yh)):
        yh[row] = [None]*(row-1)
        for col in range(len(yh[row])):
            if col==0 or col==row:
                yh[row][col]=1
            else:
                yh[row][col]=yh[row-1][col]+yh[row-1][col-1]
            print(yh[row][col],end='\t')
        print()
        
    def is_primenumber():
    """
    判断输入的数是不是素数
    """
    num=int(input('请输入一个正数：'))
    end = int(sqrt(num))
    is_prime=True
    for x in range(2,end+1):
        if num % x == 0:
            is_prime=False
            break
    if is_prime and num !=1:
        print('%d是素数'% num)
    else:
        print('%d不是素数'% num)

def output_triangle():
    """
    打印各种形状的三角形图案
    """
    row = int(input('请输入行数：'))
    for x in range(row):
        for _ in range(x+1):
            print('*',end='')
        print()

    for x in range(row):
        for y in range(row):
            if y < row-x-1:
                print(' ',end='')
            else:
                print('*',end='')
        print()
        
    for x in range(row):
        for _ in range(row-x-1):
            print(' ',end='')
        for _ in range(2*x+1):
            print('*',end='')
        print()
    print('打印三角形状图案结束')

def muplication_table():
    """
    输出九九乘法表
    """
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d * %d = %d'%(i,j,i*j),end='\t')
        print('')
    print('九九乘法表输出结束')
               
if __name__=='__main__':
    #chicken()
    #Craps()
    #Fibonacci()
    #Guess_num()
    #Daffodil()
    #palindrome()
    #perfect_num()
    yanghui()

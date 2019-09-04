#!/usr/bin/pythhon3
#-*- coding:utf-8 -*-

import xlrd
#import os

def read_excle(file_path,x,y):
    data=xlrd.open_workbook(file_path)
    #get a table
    table=data.sheets()[0]   #通过索引顺序获取
    print("该文件有%s 行" % table.nrows)
    print("该文件有%s 列" % table.ncols)
    if (x<=table.nrows and y<=table.ncols):
        print('查找到的单元格内容',table.cell(x,y).value)
    else:
        print('查找失败')
    return (table.cell(x,y).value)

if __name__=='__main__':
    nr=input("请输入要查找的行号：")
    nc=input("请输入要查找的列号：")
    print(type(nr))
    a = read_excle(r'F:\云屏科技\林\7个100k关键字 boring 工作\100Kxls工作 - 副本.xls.csx',int(nr),int(nc))





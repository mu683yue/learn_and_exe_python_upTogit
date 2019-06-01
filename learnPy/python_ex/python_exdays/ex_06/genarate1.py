#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
生成器 - 生成器语法
version:1.0
date:2019\6\1
"""

seq = [x*x for x in range(10)]
print(seq)

gen = [x*x for x in range(10)]
print(gen)
for x in gen:
	print(x)

num=10
gen = (x**y for x,y in zip(range(1,num),range(num-1,0,-1)))
print(gen)
n = 1
while n<num:
	print(next(gen))
	n +=1
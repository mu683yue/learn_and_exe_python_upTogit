#!/usr/bin/python3
# -*- coding:utf-8 -*-

#显示出指定路径下有.py后缀的文件名
import os
files=os.listdir(r'D:\LHQ_develop\python_ex\Cookbook')
fn=[]
for name in files:
    if name.endswith('.py'):
        fn.append(name)
        print("There be python")
    else:
        print('sorry,no python')                
print(fn)

#output a tuple as CSV
s=('ACME',50,123.45)
print(','.join(str(x) for x in s))

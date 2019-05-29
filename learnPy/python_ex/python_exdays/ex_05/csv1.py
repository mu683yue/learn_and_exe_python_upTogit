#!usr/bin/python3
# -*0- coding:utf-8 -*-

"""
读取写入csv

version：1.0
date：2019\5\29

"""
import csv

class Teacher(object):
    def __init__(self,name,age,title):
        self._name=name
        self._age=age
        self._title=title
        self._index=-1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def title(self):
        return self._title

if __name__=='__main__':
    filename = r"E:\恒生测试用例v3.csv"
    teachers = [Teacher("王",35,"叫兽"),Teacher("林",26,"砖家")]

    try:
        with open(filename,"w") as f:
            writer = csv.writer(f)
            for teacher in taechers:
                writer.writer([teacher.name,teacher.age,teacher.title])
    except BaseException as e:
        print("无法写入文件：",filename)
    else:
        print("保存数据完成！")

    try:
        with open(filename) as f:
            reader=csv.reader(f)
            data=list(reader)
    except FileNotFoundError as e:
        print("无法打开文件",filename)
    else:
        for item in data:
            print("%-30s%-20s%-10s" % (item[0],item[1],item[3]))
            

        
    

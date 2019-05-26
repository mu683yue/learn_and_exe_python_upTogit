#!usr/bin/python3
#-*- coding:utf-8 -*-

class Rectangle(object):
    """
    定义和使用矩阵类

    version：1.0
    date：2019\5\24
    """

    def __init__(self,width=0,height=0):
        """
        初始化方法
        """
        self._width=width
        self._height=height

    def perimeter(self):
        """计算周长"""
        return  round((self._width+self._height)*2,2)  #round(x,k),x是要处理的浮点数，k是保留的小数点后位数

    def area(self):
        """计算面积"""
        return round(self._width*self._height,2)

    def __str__(self):
        """ 矩形对象的字符串表达式 """
        return "矩形[%f,%f]" % (self._width,self._height)

    def __del__(self):
        """ 析构器 """
        print("销毁矩形对象")

if __name__=='__main__':
    rect1=Rectangle()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2=Rectangle(4.7,8.3)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
    
        

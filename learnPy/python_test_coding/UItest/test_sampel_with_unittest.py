#!/usr/bin/python3
#-*-coding:utf-8-*-

class Count:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    #计算加法
    def add(self):
        return self.a+self.b
'''
#非unittest测试方法
class TestCount():
    def test_add(self):
        try:
            j=Count(2,34.5)
            add=j.add()
            assert(add==5),'Integer addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass!')

#执行测试类测试方法
mytest=TestCount()
mytest.test_add()
'''


#unittest单元测试方法
import unittest  #引入unittest模块

'''
#未封装测试类的测试方法
class TestCount(unittest.TestCase):

#测试用例执行前的初始化
    def setUp(self):
        print('test atart!')


#测试用例1
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5,msg="计算正确")   #使用assertEqual()方法断言

#测试用例2
    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117,msg="计算失败")   #使用assertEqual()方法断言

#测试用例执行的善后工作
    def tearDown(self):
        print('test end!')

if __name__=='__main__':
   # unittest.main() #无测试集的时候的简单的执行测试方法

   #构建测试集
   suite=unittest.TestSuite()
   suite.addTest(TestCount("test_add2"))

   #执行测试
   runner=unittest.TextTestRunner()
   runner.run(suite)5
 '''


#封装测试类的方法
class Mytest(unittest.TestCase):
    def setUp(self):
        print('Test start!')

    def tearDowm(self):
        print('test case end!')

class TestCount(Mytest):

    #测试用例1
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5,msg="计算正确")   #使用assertEqual()方法断言

    #测试用例2
    def test_add2(self):
        j=Count(41,76)
        self.assertEqual(j.add(),117,msg="计算正确")   #使用assertEqual()方法断言


if __name__=='__main__':
    unittest.main()

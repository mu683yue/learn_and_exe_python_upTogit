#!/usr/bin/python3
#*-* coding:utf-8 -*-

import unittest
import ddt

# 测试数据
datas = [ {"user": "admin", "psw": "123", "result": "true"},
        {"user": "admin1", "psw": "1234", "result": "true"},
        {"user": "admin2", "psw": "1234", "result": "true"},
        {"user": "admin3", "psw": "1234", "result": "true"},
        {"user": "admin4", "psw": "1234", "result": "true"},
        {"user": "admin5", "psw": "1234", "result": "true"},
        {"user": "admin6", "psw": "1234", "result": "true"},
        {"user": "admin7", "psw": "1234", "result": "true"},
        {"user": "admin8", "psw": "1234", "result": "true"},
        {"user": "admin9", "psw": "1234", "result": "true"},
        {"user": "admin10", "psw": "1234", "result": "true"},
        {"user": "admin11", "psw": "1234", "result": "true"}]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*datas)
    def test_(self, d):
        """上海-悠悠：{0}"""
        print("测试数据：%s" % d)

if __name__ == "__main__":
    unittest.main()

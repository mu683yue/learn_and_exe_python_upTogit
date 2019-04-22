#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
使用支撑函数（support function）来处理，不区分大小写方式的对文本的查找和替换；
代替换的文本和匹配的文本大小写要吻合
'''
import re

def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
#--------------验证方法
text='UPPER PYTHON, lower python, Mixed Python'
a=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
print(a)

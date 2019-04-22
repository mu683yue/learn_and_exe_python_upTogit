#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
找出序列中次数最多的元素
collections.Counter类的most_common()方法可以解决
Couter对象的数学运算
'''
from collections import Counter

words=['look','into','my','eyes','look','into','my','eyes',
       'the','eyes','the','eyes','the','eyes','not','around',
       'the','eyes',"don't",'look','around','the','eyes','look','into',
       'my','eyes',"you're",'under']
word_counts=Counter(words)

#出现最频繁的3个元素
top_three=word_counts.most_common(3)
print("words中出现最频繁的3个元素是：",top_three)

#Counter数学运算
morewords=['why','are','you','not','looking','in','my','eyes']
a=Counter(words)
b=Counter(morewords)
print("words=",a)
print("morewords=",b)

#Combine counts
c=a+b
print("combine words+morewords:",c)
#subtract counts
d=a-b
print("subtract counts:",d)

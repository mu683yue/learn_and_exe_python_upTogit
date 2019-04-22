#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''保存最后N个元素
应用：保存有限的历史记录-----collections.deque

以下对一系列文本行做简单的文本匹配操作，当发现匹
配时就输出当前的匹配行以及最后检查过的N行
'''

from collections import deque

def search(lines,pattern,history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

#example use on a file
if __name__ == '__main__':
    with open(r'E:\2.3.5测试问题记录.txt') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)

            

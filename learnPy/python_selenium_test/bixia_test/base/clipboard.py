#/usr/bin/python3
#-*- coding:utf-8 -*-

"""
class clipboard():
    --getCBText :读取剪贴板
    --setCBText :写入剪贴板
"""

import win32con
import win32api
import win32clipboard as wcb

class clipboard():

    def getCBText(self):
        wcb.OpenClipboard()
        d = wcb.GetClipboardData(win32con.CF_UNICODETEXT)
        wcb.CloseClipboard()
        return d

    def setCBText(self,info):
        wcb.OpenClipboard()
        wcb.EmptyClipboard()
        wcb.SetClipboardData(win32con.CF_UNICODETEXT,info)
        wcb.CloseClipboard()

    


if __name__=='__main__':
    c = clipboard()
    c.setCBText('林 测试')
    print(c.getCBText())

    

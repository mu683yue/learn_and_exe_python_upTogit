#!usr/bin/python3.7
# -*- coding:utf-8 -*-

"""
结合win32自动发送foxmail并带附件邮件
"""

import win32gui
import win32con
import win32api
import pyautogui
from pywinauto.application import Application
import time


#没有打开foxmail用start,打开后连接到foxmail
foxmail_path=r"D:\Program Files\Foxmail 7.2\Foxmail.exe"
app=Application().connect(path=foxmail_path)
foxmail_mainclass="TFoxMainFrm.UnicodeClass"  #foxmail主窗体类名
win_hwnd=win32gui.FindWindow(foxmail_mainclass,None) #获取foxmail主窗体句柄
win_dlg=app.window(handle=win_hwnd)     #获取主窗体的dialog
#win_dlg.print_control_identifiers()


'''
#触发窗体含有的控件，子窗体，菜单
#触发方式:app[window_title].child_window(title='窗体名',class_name="窗体类名")
'''
#方法1从identifies结合spy++找到“发邮件的”控件并按下


#方法2通过坐标点击“发邮件”
left, top, right, bottom = win32gui.GetWindowRect(win_hwnd)#获取Foxmail的坐标
w_left=132+left #"写邮件"的相对与Foxmail主窗体left坐标
w_top=44+top    #"写邮件"的相对与Foxmail主窗体top坐标
pyautogui.click(w_left,w_top)  #点击“写邮件”





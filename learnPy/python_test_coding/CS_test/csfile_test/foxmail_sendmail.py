#!usr/bin/python3.7
# -*- coding:utf-8 -*-

"""
结合win32自动发送foxmail并带附件邮件
"""

import win32gui
import win32con
import win32api
import pyautogui
import pykeyboard
from pykeyboard import PyKeyboard
from pywinauto.application import Application
import time

k = PyKeyboard()

#判断是否字符串为数字
def is_number(s): 
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def send_keybd(num):
        win32api.keybd_event(num,0,0,0)   #键入num
        win32api.keybd_event(num,0,win32con.KEYEVENTF_KEYUP,0)  #释放num键
        
    

#没有打开foxmail用start,打开后连接到foxmail
foxmail_topclass = "TFoxMainFrm.UnicodeClass"  #foxmail主窗体类名
ttbxdoc_class = "TTBXDock"
ttbxdoc_first_childclass = "TTBXToolbar"
ttbxdoc_second_childclass = "TTBXToolbar"  #"写邮件"的类名和兄弟同类名，可以通过兄弟句柄来FindNextWindow

foxmail_path = r"D:\Program Files\Foxmail 7.2\Foxmail.exe"
app = Application().connect(path=foxmail_path)


#从顶窗体一层层往下找到“写邮件”的窗口句柄
top_hwnd = win32gui.FindWindow(foxmail_topclass,None) #获取foxmail主窗体句柄
top_dlg = app.window(handle=top_hwnd)     #获取主窗体的dialog
#win_dlg.print_control_identifiers()
ttbxdoc_hwnd = win32gui.FindWindowEx(top_hwnd,0,ttbxdoc_class,None)
ttbxdoc_first_childhwnd = win32gui.FindWindowEx(ttbxdoc_hwnd,0,ttbxdoc_first_childclass,None)
ttbxdoc_second_childhwnd = win32gui.GetWindow(ttbxdoc_first_childhwnd,2)  #写邮件是搜索邮件同级别下一个窗口
print("主窗口：%x，主窗口的第一个子窗口：%x，写邮件的兄弟窗口：%x，写邮件窗口句柄：%x" % (top_hwnd,ttbxdoc_hwnd,ttbxdoc_first_childhwnd,ttbxdoc_second_childhwnd))

'''
#写邮件所在窗口是个ToolBar，基本上toolbar里面按钮是直接绘制的，没有handler，所以只能使用坐标操作了
#方法一、通过坐标点击“写邮件”
rect = win32gui.GetWindowRect(ttbxdoc_second_childhwnd)#获取窗口的坐标
left, top, right, bottom = rect
print("所获取窗口坐标：left:%d,top:%d,right:%d,bottom:%d" % (left,top,right,bottom))
x = int(left+(right-left)*3/16)
y = int(top+(bottom-top)*1/2)
print(x,y)
pyautogui.click(x,y)  #通过坐标点击"写邮件"按钮
'''
#方法二、通过快捷键 control+N ,点击“写邮件”
win32api.keybd_event(17,0,0,0)  #control
win32api.keybd_event(78,0,0,0)  #N
win32api.keybd_event(78,0,win32con.KEYEVENTF_KEYUP,0)  #释放N按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  #释放control键


#====================================================
#写邮件
#一层层找到“收件人”的hwnd，并输入收件人
'''
实际无法实现Foxmail自动发送邮件，因为点击“写邮件”后，有相同的title和类名，
无法准确获取到写邮件句柄.
但是找到一个方法：
可以把同名的窗口通过win32gui.SetWindowText(hwnd,"windowtext")改变窗口名后，找到另一个实际需要的窗口
'''
mail_toptitle = "未命名 - 写邮件"
mail_topclass = "TFoxComposeForm.UnicodeClass"  #"写邮件"窗体类名
mail_child1class = "TFoxComposeFrame.UnicodeClass"  #写邮件第一个子窗口，和“保存”、“发送”等窗口同级别的窗口
mailchild1_childclass = "TLayoutManager"
htmledit_class = "TFoxHTMLEditor" #邮件正文窗口类名
reciver_class="TFMZRichEdit.UnicodeClass"   #“收件人”等所在窗口类名


'''
mail_tophwnd = win32gui.FindWindow(mail_topclass,None)
print("%x" % mail_tophwnd)
#将获取到的第一个窗口句柄改窗口名
win32gui.SetWindowText(mail_tophwnd,"123")
#重新获取写邮件窗口句柄（此乃我们需要的窗口）
mail_tophwnd = win32gui.FindWindow(mail_topclass,None)
print("%x" % mail_tophwnd)
mail_child1hwnd = win32gui.FindWindowEx(mail_tophwnd,0,mail_child1class,None)
print(mail_child1hwnd)
mail_child1_childhwnd = win32gui.FindWindowEx(mail_child1hwnd,0,mailchild1_childclass,None)
print(mail_child1_childhwnd)
#邮件正文窗口句柄
htmledit_hwnd = win32gui.FindWindowEx(mail_child1_childhwnd,0,htmledit_class,None)
print(htmledit_hwnd)
#密送窗口句柄，其同级别下一个窗口为抄送人
seTo_hwnd = htmledit_hwnd = win32gui.FindWindowEx(mail_child1_childhwnd,0,reciver_class,None)
#抄送人窗口句柄,其同级别下一个窗口为收件人
copyTo_hwnd = win32gui.GetWindow(seTo_hwnd,2)
#收件人窗口句柄
reciever_hwnd = win32gui.GetWindow(copyTo_hwnd,2)
print("mail_tophwnd:%x,htmledit_hwnd:%x,seTo_hwnd:%x,copyTo_hwnd:%x,reciever_hwnd:%x" % (mail_tophwnd,htmledit_hwnd,seTo_hwnd,copyTo_hwnd,reciever_hwnd))

#添加收件人
reciever1=b"mu683yue@163.com"
#返回1，但是实际没有输入成功，需要研究
#win32gui.SendMessage(reciever_hwnd,win32con.WM_SETTEXT,0,0)  #返回1，但是实际没有输入成功
for x in reciever1: #依次发送字节串中的每个字节
	win32gui.SendMessage(hWndEdit,win32con.WM_CHAR,x,0)
'''

###使用快捷键control+1，将光标定位到收件人栏
win32api.keybd_event(17,0,0,0)  #control
win32api.keybd_event(97,0,0,0)  #1
win32api.keybd_event(97,0,win32con.KEYEVENTF_KEYUP,0)  #释放1按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  #释放control键
time.sleep(2) #需要等待光标定位时间
#收件人栏输入reciever1
reciever1="mu683yue@163.com"
k.type_string(reciever1)
k.tap_key(k.enter_key,n=2,interval=1) #按两次回车键，每次间隔1s
time.sleep(2)

#使用快捷键control+shift+A添加附件
k.press_key(k.control_key) #长按control
k.press_key(k.shift_key)   #长按shift
k.tap_key('A')   #按'A'
k.release_key(k.control_key) #松开control
k.release_key(k.shift_key) #松开shift
time.sleep(10)  #等待自动保存

#通过“打开”窗口一层层查找后，添加附件
open_class = "#32770 (Dialog)"
file_topclass = "ComboBoxEx32" #文件名第一个窗体
file_childclass = "ComboBox" #文件名第一个窗体
edit_class = "Edit"
button_title = "打开(&O)"
button_class = "Button"
#打开窗口是写邮件窗口的同级别的上一个窗口
mail_tophwnd = win32gui.FindWindow(mail_topclass,None)  #写邮件窗口句柄
print("%x" % mail_tophwnd)
open_dialog=win32gui.GetWindow(mail_tophwnd,3)

file_tophwnd = win32gui.FindWindowEx(open_dialog,0,file_topclass,None)
file_childhwnd = win32gui.FindWindowEx(file_tophwnd,0,file_childclass,None)
edit_hwnd = win32gui.FindWindowEx(file_childhwnd,0,edit_class,None)
button_hwnd = win32gui.FindWindowEx(file_childhwnd,0,edit_class,button_title)


#上传fileDir的文件,并点击“打开”来确定
fileDir=r"E:\2.3.5测试问题记录.txt"
win32gui.SendMessage(edit_hwnd, win32con.WM_SETTEXT, 0, fileDir)
win32gui.SendMessage(open_dialog, win32con.WM_COMMAND, 1, button_hwnd)






    



'''
#触发窗体含有的控件，子窗体，菜单
#触发方式:app[window_title].child_window(title='窗体名',class_name="窗体类名")


##        if (title.find(targetTitle) >= 0):    #调整目标窗口到坐标(600,300),大小设置为(600,600)
##            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600,300,600,600, win32con.SWP_SHOWWINDOW)

'''




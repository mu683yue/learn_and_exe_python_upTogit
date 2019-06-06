#!usr/bin/python3
# -*- coding:utf-8 -*-

import win32gui
import win32con
import win32gui_struct

#获取某个菜单的内容
def get_menu_item_txt(menu,idx):
    mii,extra=win32gui_struct.EmptyMENUITEMINFO()
    win32gui.GetMenuItemInfo(menu,idx,True,mii)
    ftype,fstate,wid,hsubmenu,hbmpchecked,hbmpunchecked,\
    dwitemdata,text,hbmpitem=win32gui_struct.UnpackMENUITEMINFO(mii)  #解包
    return text

if __name__=='__main__':
    window_class="Notepad++"
    hwnd=win32gui.FindWindow(window_class,None)
    menu=win32gui.GetMenu(hwnd)

    for i in range(5):
        t=get_menu_item_txt(menu,i)
        print(t)


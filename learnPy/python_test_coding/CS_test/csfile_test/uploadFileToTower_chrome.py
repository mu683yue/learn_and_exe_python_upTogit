#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
-通过chrome浏览器登录Tower
-将文件上传至Tower的文件夹

version:1.0
date:2019\5\27
author:LHQ
"""

from selenium import webdriver
import time
import win32gui
import win32con

##chromedriver=r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
##driver=webdriver.Chrome(chromedriver)

def loginTower(username,password):
    tower_base_url="https://tower.im"
    driver.get(tower_base_url)
    #跳转至登录页面
    time.sleep(2)
    driver.find_element_by_xpath("//*[@class='actions']/a[2]").click()
    #登录
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("btn-signin").click()

def uploadFile(projectSelector,fileDir):
    #driver.switch_to_window(driver.window_handles[1])
    time.sleep(5)
    driver.find_element_by_xpath(projectSelector).click()
    time.sleep(5)
    #定位到文件“2压缩 谷歌”文件夹
    driver.find_element_by_xpath('//*/div[@class="dir-name"]/div[@class="link-name"]/a[@title="2压缩 谷歌"]').click
    #在定位到的文件夹点击“上传文件”
    time.sleep(3)
    driver.find_element_by_xpath('//*/a[@class="btn btn-mini btn-upload-file"]').click()
##    driver.find_element_by_xpath("//*[@id='uploads']/h3/div/button").click()
##    driver.find_element_by_xpath("//*[@id='uploads']/h3/div/ul/li[1]/a").click()
    time.sleep(5)
    
    #点击上传文件后，通过定位弹出的windows对话框的句柄和控件上传fileDir文件
    dialog = win32gui.FindWindow('#32770', u'打开') #找到windows对话框参数是（className，title）
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #上面3句依次找对象，直到找出输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None) #确定按钮
    # 跟上面示例的代码是一样的，只是这里传入的参数不同，如果愿意可以写一个上传函数把上传功能封装起来
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, fileDir)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

if __name__=='__main__':
    #变量
    chromedriver=r"D:\allWebDriver/chromedriver.exe"
    driver=webdriver.Chrome(chromedriver)
    email="huqiong.lin@cloudscreen.com"
    password="1qaz2wsx#"
    filepath_1=r"F:\林\代码\压缩\压缩--改名.7z"



    #成功登录
    loginTower(email,password)
    uploadFile("//*[@data-access-id='18619755']",filepath_1)

    #关闭浏览器
    driver.quit()
        
    

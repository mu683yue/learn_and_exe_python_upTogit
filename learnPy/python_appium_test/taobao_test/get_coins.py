#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用appium+python
进行2019\6\18的618活动中“淘金币”+“合猫猫”自动浏览网页10秒，
收取金币和喵币需要暂时自己点击（暂时不想实现）

version:1.0
date:2019\6\10
"""

from appium import


#desired_capabilities
"""
使用adb dump badging taobao.apk(淘宝apk的全路径)
来获取auncherActivity：
    package: name='com.taobao.taobao'
    launchable-activity: name='com.taobao.tao.welcome.Welcome'
一般的desired_capabilities除了platformName\deviceName\platformVersion\appPackage\appActivity，
其他非必需
"""
desired_caps={
    "platformName":"Android",      #系统
    "deviceName":"621QECQC46DJT",                #移动设备号
    "platformVersion":"7.0",           #系统版本
    "appPackage":"com.taobao.taobao",#操作的app
    "appActivity":"com.taobao.tao.wecome.Welcome",#打开淘宝app
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "dontStopAppOnReset":True,
    "autoGrantPermissions":True,
    "noReset":True,             #noReset=True后，appium启动后结束后不清空应用数据
    #"automationName":"uiautomator2",
    "newCommandTimeout":"36000",        #超时时间
    #"systemPort":"8202",                #设备端口号，操作不同设备使用不同端口
    #"udid":"",                          #移动设备号
    #"command_excutor":""                #和启动命令保持一致
    }
driver=webdriver.Remote("http://127.0.01:4723/wd/hub",desired_caps)    #url根据appium连接的信息获得


#登录淘宝,进入|“我的淘宝”
driver.findElementByAccessibilityId("我的淘宝").click()


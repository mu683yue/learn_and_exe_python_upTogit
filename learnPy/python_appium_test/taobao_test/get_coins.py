#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
使用appium+python
进行2019\6\18的618活动中“淘金币”+“合猫猫”自动浏览网页10秒，
收取金币和喵币需要暂时自己点击（暂时不想实现）

version:1.0
date:2019\6\10
"""

from appium import webdriver
import time


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
    "deviceName":"MI MAX-5d5bf4e4",                #移动设备号
    "platformVersion":"6.0.1",           #系统版本
    "appPackage":"com.taobao.taobao",#操作的app
    #"appActivity":"com.taobao.tao.welcome.Welcome",
    "appActivity":"com.taobao.tao.TBMainActivity",#打开淘宝app,使用com.taobao.tao.welcome.Welcome作为activity失败，需要研究下
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "dontStopAppOnReset":True,
    "autoGrantPermissions":True,
    "noReset":True,             #noReset=True后，appium启动后结束后不清空应用数据
    #"automationName":"uiautomator2",
    "newCommandTimeout":"36000",       #超时时间
    #"systemPort":"8202",                #设备端口号，操作不同设备使用不同端口
    "udid":"5d5bf4e4",                          #移动设备号，必须
    #"command_excutor":""                #和启动命令保持一致
    }
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)    #url根据appium连接的信息获得

#坐标点击封装
def touch_tap(self,x,y,duration=100):   #点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = driver.get_window_size()['width']  #获取当前屏幕的宽
        screen_height = driver.get_window_size()['height']   #获取当前屏幕的高
        a =(float(x)/screen_width)*screen_width
        x1 = int(a)
        b = (float(y)/screen_height)*screen_height
        y1 = int(b)
        driver.tap([(x1,y1),(x1,y1)],duration)

#登录淘宝,进入|“我的淘宝”
#无法自动登录淘宝，淘宝登录页面不能截图，无法分析元素
#driver.findElementByAccessibilityId("我的淘宝").click()

#看是否可以登录后，使用noReset来保留登录数据
# content-desc为空，获取的是text
time.sleep(5)
t3 = driver.find_element_by_id("com.taobao.taobao:id/tv_right_icon_content").get_attribute("name")
print(t3)  #合猫猫

driver.find_element_by_id("com.taobao.taobao:id/tv_right_icon_content").click()
time.sleep(3)
"""
#查看是否有猫币在休息期间产生并收取
#reward_coins=driver.find_element_by_name("奖励来袭")
ele_x="className('android.view.View').index('5')"
if driver.find_element_by_name("奖励来袭")!=False:
        touch_tap(550,1350)
    #driver.find_element_by_android_uiautomator(ele_x).click()  #点击“X”关闭
"""
touch_tap(550,1350)        
time.sleep(2)

#由于“领猫币”页面无法元素定位，通过坐标不断点击关闭，“召唤理想猫”tap(600,1600)
#需要判断是否会弹出“喵币不足”（无法判断是图片显示，但是点击空白处可以处理）"逛店铺得理想猫"tap(500,1380)
touch_tap(600,1600)
touch_tap(500,1380)


#店铺等10秒后，领猫币按钮坐标"text=猫猫出现啦" [915,1086][1031,1124]，
ele_text="猫猫出现啦"
time.sleep(15)
driver.find_element_by_name(ele_text).click()
time.sleep(2)

#点击后“成功抓到猫猫啦”+点击“开心收下”收猫币 tap（550,1350）
touch_tap(550,1350)
time.sleep(2)

#点击店铺页面的“X”[942,94][1042,174]：class=android.widget.FrameLayout,content_desc="返回"，返回“合猫猫”领金币页面重复
#driver.back()
driver.find_element_by_accessibility_id('返回').click()


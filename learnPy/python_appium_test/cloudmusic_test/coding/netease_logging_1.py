#!/usr/bin/python3
#-*- coding:utf-8 -*-

from appium import webdriver
import time


caps={}
caps["platformName"]="android"
caps["platformVersion"]="6.0.0"
caps["deviceName"]="vnox86p"
caps["appPackage"]="com.netease.cloudmusic"
caps["appActivity"]="com.netease.cloudmusic.activity.LoadingActivity"

driver=webdriver.Remote('',caps)
driver.find_element_by_id().click()









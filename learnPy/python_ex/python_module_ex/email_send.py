#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
email模块构造邮件，smtplib模块负责发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'huqiong.lin@cloudscreen.com'
reciever = 'mu683yue@163.com'
smtpserver = 'smtp.cloudscreen.com'
username = 'huqiong.lin@cloudscreen.com'
password = '1qaz2wsx#'

#邮件主题
mail_title = '主题：测试1'

#读取文件内容
with open(r'E:\2.3.5测试问题记录.txt') as f:
    mail_body=f.read()

#邮件内容，格式，编码
message= MIMEText(mail_body,'html','utf-8')
message['From']=sender
message['To']=reciever
message['Subject']=Header(mail_title,'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password) #登录SMTP服务器
    smtp.set_debuglevel(1) #打印出和SMTP服务器交互的所有信息
    smtp.sendmail(sender,reciever,message.as_string()) #发送邮件，as_string()把MIME Text对象变成str
    print('发送邮件成功！')
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！")

#!usr/bin/python3
#-*-coding:utf-8 -*-

import win32com.client
import time,os
import warnings
import pythoncom
import sys

def sendmail(sub,body,reciever,addfiles):
    outlook=win32com.client.Dispatch("outlook.application")
    mail=outlook.CreateItem(0)
    mail.To=reciever
    #mail.Subject=sub.decode('utf-8')
    #mail.Body=body.decode('utf-8')
    for item in addfiles:
        mail.Attachments.Add(item)
    mail.Send()

if __name__=="__main__":
    sub='outlook python mail test'
    body='my test \r\n my python mail'
    reciever="ting@XX.com"

##    addfiles=[r"F:\移动",
##              ]
    fpath = r"F:\移动"
    fname_list = os.listdir(fpath)
    addfiles = []
    for item in fname_list:
        addfiles.append(os.path.join(fpath,item))
    print(addfiles)
    sendmail(sub,body,reciever,addfiles)
    print("send email success")
    
    







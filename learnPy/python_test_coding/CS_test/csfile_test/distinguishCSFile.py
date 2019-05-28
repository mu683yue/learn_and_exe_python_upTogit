#!usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import shutil
import re

"""
-修改文件名，根据文件名识别企业文件
-修改文件内容，添加文件关键字，根据关键字识别企业文件

version：1.0
date：2019\5\25
author:LHQ
"""

sourcedir=os.path.abspath(r"\\10.10.10.2\guest\software\\lin\测试文件\关键字识别不加密文件")
targetdir=os.path.abspath(r"E:\CS工作\临时测试结果\testfile")

def copyFiles(sourceDir,targetDir):
    for f in os.listdir(sourceDir):
        sourceF=os.path.join(sourceDir,f)
        targetF=os.path.join(targetDir,f)

        if os.path.isfile(sourceF):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
        shutil.copy(sourceF,targetDir)

def splitFilenameAndExtention_inDir(targetDir):
    filename_extention_dict={}
    for f in os.listdir(targetDir):
        (filename_pre,extention)=os.path.splitext(f)
        filename_extention_dict[filename_pre]=extention
    print(filename_extention_dict)
    return filename_extention_dict

def addFileName(filename,add_name):
    edited_files=[]
    (file_ex,extention)=os.path.splitext(filename)
    return edited_files.append(file_ex+add_name+extention)
    
        


def is_CSfile(ex=".csx"):
    """
    根据后缀是否包含ex判断是否企业加密文件,并返回加密文件列表
    return cs_files
    """
    file_dict=splitFilenameAndExtention_inDir(targetdir)
    print(file_dict)
    cs_files=[] #加密企业文件列表
    #根据文件后缀是否包含csx判断加密的企业文件，并将加密文件添加至加密企业文件列表
    for key,value in file_dict.items():
        if re.match(value,ex):
            print("%s是企业加密文件"% (key+value))
            cs_files.append(key+value)
        else:
            print("%s不是企业加密文件"% (key+value))
    print(cs_files)
    return cs_files
    
        

if __name__=='__main__':
    print(sourcedir)
    print(targetdir)
    is_CSfile()

            
        
                    

















                
            
    

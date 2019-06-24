#!usr/bin/python3
# -*- coding:utf-8 -*-

"""
-拷贝文件夹下所有文件至目标文件夹 copyFiles
-拷贝文件夹下某文件至目标文件夹 copyFile
-移动文件：moveFile:move s_filedir -> d_filedir
-拷贝文件夹至目标路径 copyFold
-改文件名和后缀 editFilename
-创建文件夹 createFold

version：1.0
date：2019\5\27
author:LHQ
"""
import os
import shutil


#-拷贝文件夹下所有文件至目标文件夹 copyFiles
def copyFiles(sourceDir,targetDir):  
    for f in os.listdir(sourceDir):
        sourceF=os.path.join(sourceDir,f)
        targetF=os.path.join(targetDir,f)

        if os.path.isfile(sourceF):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
        shutil.copy(sourceF,targetDir)

-拷贝文件夹下某文件至目标文件夹 copyFile
def copyFile(sourceDir,targetDir,filename):
    sourceF=os.path.join(sourceDir,filename)
    targetF=os.path.join(targetDir,filename)
    if not os.path.exists(targetF):
        if os.path.isfile(sourceF):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            shutil.copy(sourceF,targetDir)
            
#-移动文件：moveFile:move s_file -> d_filedir
def moveFile(s_file,d_filedir):
	if os.path.isfile(s_file) and os.path.is_dir(d_filedir):
		shutil.move(s_file,d_filedir)
		print("moveFile:move %s -> %s "% (s_file,d_filedir))
	else:
		print("move fail,please make sure s_file is a file,and d_filedir is a fold.")



#-拷贝文件夹至目标路径 copyFold        
def copyFold(sourceDir,targetDir,foldname):
    sourceDir=sourceDir+"\\"+foldname
    print(sourceDir)
    targetDir=targetDir+"\\"+foldname
    print(targetDir)
    if os.path.exists(targetDir):
        print(targetDir,"已经存在需要先删除")
        shutil.rmtree(targetDir)
        print("删除",targetDir,"成功")
    if os.path.exists(sourceDir):
        shutil.copytree(sourceDir,targetDir)
        print("将%s拷贝到目标路径成功" % foldname)
        #返回添加了新文件夹的目标绝对路径
        return os.path.abspath(targetDir)

#-创建文件夹 createFold
def createFold(sourcePath,foldname):
    newdir=os.path.join(sourcePath,foldname)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    return newdir

#-改文件名和后缀 editFilename
def editFilename(filePath,oldFilename,newFilename):
    os.rename(filePath+"\\"+oldFilename,filePath+"\\"+newFilename)

if __name__=='__main__':
    #从10.10.10.2目标文件夹把原代码文件拷贝到测试文件夹
    sourcedir=os.path.abspath(r"\\10.10.10.2\guest\software\lin\测试文件\代码\policy_server-master")
    sourcefold="CLCTPolicy"
    targetdir=os.path.abspath(r"E:\CS工作\临时测试结果\林\代码\原代码")
    basepath=os.path.abspath(r"E:\CS工作\临时测试结果\林\代码")
    #copyFold(sourcedir,targetdir,sourcefold)
    #修改测试文件夹的文件名文件后缀
    #拷贝至“改名改后缀拷贝文件夹”,改名改后缀
    t_path=createFold(basepath,"改名改后缀拷贝文件夹")
    print(t_path)
    copyFile(targetdir+"\\CLCTPolicy\\3rdparty",t_path,"cloudPolicy.pb.cc")
    editFilename(t_path,"cloudPolicy.pb.cc","cloudPolicy改名改后缀拷贝.c")
    



    
                              
    

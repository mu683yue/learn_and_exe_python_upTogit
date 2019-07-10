#!/usr/bin/python3
# -*- coding:utf-8 -*-



"""
-拷贝文件夹下所有文件至目标文件夹 copyFiles
-拷贝文件夹下某文件至目标文件夹 copyFile
-移动文件：moveFile:move s_filedir -> d_filedir
-拷贝文件夹至目标路径 copyFold
-改文件名和后缀 editFilename
-创建文件夹 createFold
-批量改文件名 rename_filename

version：1.0
date：2019\7\10
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

#-拷贝文件夹下某文件至目标文件夹 copyFile
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

#-批量改文件名 rename_filename
def rename_filename(fileDir,add_string):
    file_list = os.listdir(fileDir)
    print(file_list)
    os.chdir(fileDir) #切换工作路径至要处理数据所在路径，否则os.rename(sour,dst)重命名的时候会报错：系统找不到文件
    for file in file_list:
        if file.endswith('.txt'):   #判断是不是文本文档，只处理文本文档
            f = file.split(".")  #正常要处理的文件f[0]是名,f[1]是后缀

            #add_string插入.txt前面，文件名中其他“.”转换成“、”
            if add_string not in file:
                new_name = '{}{}.{}'.format("、".join(f[:-1]),add_string,f[-1])
                os.rename(file,new_name)
                print("修改了%s" % file)

if __name__ == '__main__':
    add_string = "(婚后文)"
    filedir = r'E:\书籍\小说\婚后文\非台言'
    rename_filename(filedir,add_string)
        
            

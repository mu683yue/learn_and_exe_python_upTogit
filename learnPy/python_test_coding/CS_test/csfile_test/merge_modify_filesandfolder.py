#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
-合并两个文件
-将文件夹里面的文件合并成一个文件
-添加文件内容
'''
import os

#-合并两个文件
def mergeFile(t_filedir,o_filedir):
    f = open(t_filedir,'a+')
    #遍历单个文件，读取行
    for line in open(o_filedir):
        f.writelines(line)
    #关闭文件f
    f.close()

#-将文件夹里面的文件合并成一个文件
def mergeFoldToFile(folder_dir,new_fileName):
    #获取文件夹所有文件名
    filenames = os.listdir(folder_dir)
    #打开同一路径下的new_fileName，没有则创建
    f = open(folder_dir+'\\'+new_fileNamwe,'a+')
    #先遍历文件名
    for filename in filenames:
        filepath = folder_dir + '\\' + filename
        f.write(filepath)
        #遍历单个文件，读取行
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
    #关闭文件f
    f.close()
    


#-添加文件内容
def modifyFile(t_filedir,add_text):
    f = open(t_filedir,'a+')
    f.write(add_text)  #在t_filedir文件后追加内容add_text
    #关闭文件f
    f.close()


    
        
    

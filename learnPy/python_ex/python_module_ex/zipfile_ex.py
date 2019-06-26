#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
练习使用zipfile模块:
zipfile.is_zipfile(filename) #判断一个文件是不是压缩文件
ZipFile.namelist()  #返回文件列表 
ZipFile.open(name[, mode[, password]])  #打开压缩文档中的某个文件 
ZipFile.infolist() #返回ZipInfo对象列表
ZipFile.getinfo(name)  #返回ZipInfo对象
ZipInfo.filename  
ZipInfo.date_time  #返回值的格式为(year,month,date,hour,minute,second) 
ZipInfo.compress_type 
ZipInfo.comment 
ZipInfo.extra 
ZipInfo.create_system
ZipInfo.extract_version
ZipInfo.reserved 
ZipInfo.flag_bits 
ZipInfo.volume 
ZipInfo.internal_attr 
ZipInfo.external_attr 
ZipInfo.header_offset 
ZipInfo.CRC 
ZipInfo.file_size 
ZipInfo.compress_size 
ZipFile.testzip() #检查每个文件和它对应的CRC，如果有错误返回对应的文件列表 
ZipFile.setpassword(password) 
ZipFile.read(name[,password]) 
ZipFile.printdir() 
ZipFile.writestr(zipinfo_or_arcname, bytes) 

"""

from zipfile import ZipFile


def check_zip(zip_f,added_files):
    """
    """
    zipf = ZipFile(zip_f,'a')   #使用追加方式打开zip_f
    zipf.write(added_files)   #追加added_files
    zipf.printdir()              #查看zipf目录结构
    zipf.namelist()            #查看zipf包含的文件，列表形式
    print(zipf.filename,zipf.debug,zipf.comment)   #ZipFile的属性

    #练习ZipInfo，ZipInfo的操作对象是ZipFile.getinfo(name)的返回值
    file1=zipf.namelist().pop() #获取zipf的第一个文件名
    zipi=zipf.getinfo(file1)     #返回ZipInfo对象
    print(zipi.filename,zipi.date_time,zipi.compress_type,zipi.comment,
          zipi.extra,zipi.create_system,zipi.extract_version,zipi.reserved,zipi.file_size)
    
    
    
    
    

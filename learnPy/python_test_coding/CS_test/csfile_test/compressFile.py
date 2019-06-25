#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
compressFile.py里面的方法用来压缩文件或文件夹

-make_zip
-make_tar
-make_gzip
-make_bz2
-make_lzbm
-make_xz
    
"""

import os,zipfile,tarfile

def make_zip(zipName,zipPath,source_files):
    '''
    zipName:要生成的zip包名，以.zip为后缀
    zipPath:要保存zip包的路径
    source_files：要压缩的文件，可以是目录，也可以是文件
    '''
    zipFullpath=os.path.join(zipPath,zipName)
    zip = tarfile.open( zipFullpath,'')
    


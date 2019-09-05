#!usr/bin/python3
#-*- coding:utf-8 -*-

import xlrd

class ExcelUtil():
    '''
    封装读取excel
    '''
    def __init__(self,excelpath,sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)   #index从0开始
        #获取总行数
        self.rowNum = self.table.nrows
        print(self.rowNum)
        #获取总列数
        self.colNum = self.table.ncols
        print(self.colNum)

    def dict_data(self):
        if self.rowNum <=1:
            print("总行数为1，没有获取测试用例，请检查！")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                #从第二行开始读取对应的values值
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j +=1
            return r

if __name__=='__main__':
    filepath = "debug_api.xlsx"
    sheetName = "sheetTest1"
    data = ExcelUtil(filepath,sheetName)
    print(data.dict_data())














            
        

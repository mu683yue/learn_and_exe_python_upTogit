# -*- coding:utf-8 -*-
import sys
import time
import xlwt  
import xlrd  
import xlutils.copy

def main(argv):
    top = int(argv[3])
    sec = int(argv[4])
    rb = xlrd.open_workbook(argv[1])
    nrows = rb.sheets()[0].nrows # open the first sheet
    for i in range(0, top):
        wb = xlutils.copy.copy(rb)
        ws = wb.get_sheet(0)
        ws.write(nrows+1, 0, argv[2] + " {:d} ".format(i))
        wb.save(argv[1])
        print("excel modifed ............ {:d} ".format(i))
        time.sleep(sec)

if __name__ == '__main__':
    main(sys.argv)
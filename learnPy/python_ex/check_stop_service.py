#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import logging

def get_stop_service(ser_list):
    '''
    input the service name needed to be checked;
    return stopping service
    '''
    lines=os.popen('net start').readlines()
    line = [item.strip() for item in [i for i in lines]]
    if ser_list in line:
        print('Service [%s] is running!' % ser_list)
        return True
    else:
        logging.error('Service [%s] is down!' % ser_list)
        return False

if __name__=='__main__':
    '''
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datetime='%Y/%m/%d %H:%M:%S',
                        filename='D:\\logs\\Monitor.log',
                        filemode='ab'
                        )
                        '''
    name='Service Name'
    assert get_stop_service('Power')
    assert get_stop_service('Print Spooler')

    assert get_stop_service('ScanService')
    

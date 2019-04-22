#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re

def is_valid_email(addr):
    if re.match(r'^[0-9a-zA-Z.]+@+[0-9a-zA-Z]+.com$',addr):
        print(addr)
        return True
    else:
        print('they don\'t match')
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
    
    

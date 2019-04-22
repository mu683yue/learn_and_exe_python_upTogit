#!/usr/bin/python3

import yagmail
from config import setting
from lib.log import apt_log

def sendemail(title,content,attrs=None):
	m=yagmail.SMTP(host)




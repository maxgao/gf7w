#!/usr/bin/python 
#-*-coding:utf8-*-
#by maxgao

import os
import sys

valus = 0

def checkDisk():
    res = os.popen('df -hT |grep / ','r').read()
    res = res.strip().split('\n')
    for i in res:
    	num = i.split(' ')
    	partition = num[-1]
    	data = num[-2]
    	data = data.split("%")[-2]
    	intdata =int(data)
    	if intdata > valus:
    		print intdata,
	    	print partition
	else:
	    pass
if __name__ == '__main__':
	
	checkDisk()

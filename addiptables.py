#!/usr/bin/python 
#-*-coding:utf8-*-
#file里的文件不能为空，随便写个
import os
import time

def add_iptables(ip):
    f = open('/home/gaofeng/iptables','a+')
    for row in f.readlines():
        if ip == row[:-1]:
            break
    else:
        res = os.popen('iptables -I INPUT -s %s -j DROP' % ip)
        print res
        f.write("%s\n" % ip)
    f.close()


if __name__=="__main__":

    add_iptables('1.1.1.2')

#!/usr/bin/python
#file里的文件不能为空，随便写个
import os
import time

def add_iptables(ip):
    f = open('/root/iptables','a+')
    for row in f.readlines():
        if ip == row[:-1]:
            break
    else:
        res = os.popen('iptables -I INPUT -s %s -j DROP' % ip)
        print res
        f.write("%s\n" % ip)
    f.close()


add_iptables('1.1.1.2')

#!/usr/bin/python
#-*-coding:utf8-*-

import socket

HOST='127.0.0.1'
PORT=50000
BUFFER=4096


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))  #连接服务器

sock.send('hello tcpServer') 
recv=sock.recv(BUFFER)  #读取数据

print('[tcpServer said]: %s' % recv)

sock.close()
#!/usr/bin/python

import socket

HOST='baidu.com'
PORT=80
BUFFER=4096


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))
message='GET / HTTP/1.1\r\nHost: %s \r\n\r\n'  % HOST

try:
    sock.send(message)
except socket.error:
    print "send failed"

recv=sock.recv(BUFFER)

print('[tcpServer said]: %s' % recv)

sock.close()
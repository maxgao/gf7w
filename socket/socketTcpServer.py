#!/usr/bin/python
#-*-coding:utf8-*-

import socket

HOST='127.0.0.1'
PORT=50000
BUFFER=4096

#第一个参数AF_INET，AF_INET6,AF_UNIX默认AF_INET,第二个参数有SOCK_STREAM和SOCK_DGRAM
#默认为SOCK_STREAM流套接字提供双向有序且不重复的数据服务也可以直接写
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((HOST,PORT)) #绑定socket地址只有一个参数 是一个地址+端口的元组

sock.listen(0) #开始监听，参数是队列长度


print ('tcpServer listen at: %s:%s\n\r' %(HOST,PORT))
while True:
	client_sock,client_addr=sock.accept() #接受一个连接
	print('%s:%s connect' %client_addr)
	while True:
		recv=client_sock.recv(BUFFER) #读取数据
		if not recv:
			client_sock.close()
			break
		print ('[Client %s:%s said] :%s' % (client_addr[0],client_addr[1],recv))
		client_sock.send('tcpServer has received your message')
sock.close()
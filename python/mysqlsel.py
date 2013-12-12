#!/usr/bin/python
# *-*coding:utf8 *-*
# maxgao 

import os
import sys
import MySQLdb
import datetime


now =  datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
#print date

DATABASE_NAME ='cacti'
HOST ='127.0.0.1'
PORT = '3306'
USER_NAME = 'aa'
PASSWORD = 'aaa1111'
CHAR_SET = 'utf8'

def getStatus(conn,date):
    query = "select * from user_auth_realm into outfile '/tmp/%s'" % date
#    query = "select * from user_log "
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

if __name__ == '__main__':
    conn = MySQLdb.connect(host = HOST,user = USER_NAME,passwd = PASSWORD,db = DATABASE_NAME,unix_socket = '/tmp/mysql.sock',charset = CHAR_SET)			
    status = getStatus(conn,date)
#    print status


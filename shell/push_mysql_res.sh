#!/bin/bash


now=`date +%Y-%m-%d`
echo $now


/usr/bin/mysql -pna cacti -e "select * from user_auth_realm into outfile '/tmp/$now'"


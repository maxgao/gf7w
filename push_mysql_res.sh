#!/bin/bash


now=`date +%Y-%m-%d`
echo $now


/usr/bin/mysql -pnaizhao1234 cacti -e "select * from user_auth_realm into outfile '/tmp/$now'"


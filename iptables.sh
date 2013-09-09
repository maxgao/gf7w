
#!/bin/bash
# 新机器iptables配置
#by maxgao 

#初始化iptables ,删除之前的规则
/sbin/iptables -F INPUT
/sbin/iptables -F FORWARD
/sbin/iptables -F OUTPUT

/sbin/iptables -Z INPUT
/sbin/iptables -Z FORWARD
/sbin/iptables -Z OUTPUT

#设置默认出站的规则
/sbin/iptables -P INPUT DROP
/sbin/iptables -P FORWARD DROP
/sbin/iptables -P OUTPUT ACCEPT

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
iptables -A INPUT -p icmp -j ACCEPT


####tcp####
for i in 22 80 445 24800 443
do
        iptables -I INPUT -p tcp --dport $i -j ACCEPT
#        iptables -I OUTPUT -p tcp --sport $i -j ACCEPT
done

####udp####
for i in 53
do
        iptables -I INPUT -p udp --dport $i -j ACCEPT
#        iptables -I OUTPUT -p udp --sport $i -j ACCEPT
done

#iptables -I INPUT -p tcp --dport 3306 -j DROP
#iptables -I INPUT -s 10.196.10.0/8 -p tcp --dport 3306 -j ACCEPT
#iptables -I INPUT -s 172.43.0.0/8 -p tcp --dport 3306 -j ACCEPT

#封禁某个IP 
#iptables -I INPUT -s 172.3.2.1 -j DROP 







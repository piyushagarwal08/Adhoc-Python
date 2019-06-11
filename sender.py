#!/usr/bin/python2

import socket
re_ip="127.0.0.1"
re_port=4444  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Sending data to target
s.sendto("hello",(re_ip,re_port))

data=s.recvfrom(100)
print(data)

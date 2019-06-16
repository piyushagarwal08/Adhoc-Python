#!/usr/bin/python2

import socket
re_ip="127.0.0.1"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print "To close communication send an blank message"
# Sending file to target
while(True):
	file_name = raw_input('Enter file name to send: ')
	if len(file_name) == 0:
		s.sendto('',(re_ip,re_port))
		break
	f = open(file_name)
	s.sendto(f.read(),(re_ip,re_port))
	
s.close()

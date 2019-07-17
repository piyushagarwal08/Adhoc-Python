#!/usr/bin/python2

import socket
re_ip="127.0.0.1"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# fitting ip and port with UDP socket
s.bind((re_ip,re_port))
while(True):
	# receive file from sender
	file_name  =  raw_input("File name to save data: ")
	data=s.recvfrom(10000)
	file = open(file_name,'w+')
	file.write(data[0])
	if len(data[0]) == 0:
		break

s.close()

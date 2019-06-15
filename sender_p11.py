#!/usr/bin/python2

import socket
re_ip="127.0.0.1"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print "To close communication send an blank message"
# Sending data to target
while(True):
	text = raw_input('Server says: ')
	if len(text) > 150:
		print("Message limit exceeded")
	else:
		s.sendto(text,(re_ip,re_port))
		data = s.recvfrom(100)
		print 'Client says: '+data[0]
		re_ip,re_port = data[1]
		if len(data[0]) == 0:
			s.sendto('',(re_ip,re_port))
			break
s.close()

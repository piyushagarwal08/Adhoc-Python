#!/usr/bin/python3

import socket
re_ip="192.168.43.134"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# fitting ip and port with UDP socket
s.bind((re_ip,re_port))
print("To Close communication reply the sender with a blank message")
while(True):

	# receiver data from sender
	data=s.recvfrom(150)
	print('Server says: '+data[0].decode('ascii'))
	text = input('Client says: ')
# Converting str to bytes - like object
	s.sendto(text.encode('ascii'),data[1])
	if len(data[0]) == 0:
		s.sendto('',data[1])
		break

s.close()

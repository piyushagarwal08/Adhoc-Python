#!/usr/bin/python2

import socket
re_ip="127.0.0.1"
re_port=4484  # 0 - 1024 -- you can check free udp port : netstat -nulp

# Creating UDP socket
#		  ip type v4	   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# fitting ip and port with UDP socket
s.bind((re_ip,re_port))
print '1. text communication \n 2.file transfer'
option = input('Choose an option: ')
if option == 1:
	print "To Close communication reply the sender with a blank message"
	while(True):

		# receiver data from sender
		data=s.recvfrom(150)
		print 'Server says: '+data[0]
		text = raw_input('Client says: ')
		if len(text) > 150:
			print("Sorry, but message length exceeded")
		else:
			s.sendto(text,data[1])
			if len(data[0]) == 0:
				s.sendto('',data[1])
				break

	s.close()

elif option == 2:
	print "only sender can send file and close connection"
	while(True):
		# receive file from sender
		file_name  =  raw_input("File name to save data: ")
		data=s.recvfrom(10000)
		if len(data[0]) == 0:
			break
		file = open(file_name,'a+')
		file.write(data[0])


	s.close()

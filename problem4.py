#!/usr/bin/python3
import os
import string
user_name = input('Enter user-name: ')
flag = 0
for i in list(user_name):
	if i not in string.ascii_letters:
		print('incorrect username')
		flag = 1
if flag == 0 :
	os.system(f'sudo useradd -p $(openssl passwd -1 hello+{user_name}) '+ user_name)

	

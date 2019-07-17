#!/usr/bin/python3
import os
user_name = ['user1','user2','user3']
for i in user_name:
	os.system('sudo useradd '+i)
print(f'{len(user_name)} users added')

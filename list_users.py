#!/usr/bin/python3

import os
os.system('ls /home > users_list.txt')
print('Currently no of users in the system are: ')
os.system('wc -l users_list.txt')

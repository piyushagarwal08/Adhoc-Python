#!/usr/bin/python3
import time
name = input('Enter your name: ')
hr = time.localtime().tm_hour
min = time.localtime().tm_min

if hr>=12 and hr<17:
	print('Good Afternoon',name)
elif hr>=17 and hr<20:
	print('Good Evening',name)
elif hr>=20 and hr<24:
	print('Good Night',name)
else:
	print('Good Morning',name)

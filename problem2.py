#!/usr/bin/python3
from googlesearch import search
import time
web=input('pls enter topic:')

# now time for search
list1 = []
for i in search(web,stop=10):
	print(i) # i will only print the url
	time.sleep(1)
	list1.append(i)
print(list1)
f = open('url.txt','a+')
for i in list1:
	f.write(i+'\n')
f.close()

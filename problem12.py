!/usr/bin/python3
from googlesearch import search
import pyqrcode
import os
url = input('Enter text to search')
urllist = []
u = 0
for i in search(url,stop=3):
	urllist.append(i)
	print(i)

# Generate a QR
	qr = pyqrcode.create(i)
# create and save file
	qr.svg(f"qr{u}.svg",scale=2)
	print(qr.terminal())
	u = u+1
for i in range(3):
  os.system(f'mv qr{u}.svg /var/www/html')

# you can check for QR code by typing url http://my-instance-ip/qr0.svg 

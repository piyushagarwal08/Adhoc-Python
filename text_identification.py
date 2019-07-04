#!/usr/bin/python3
import cv2
import pytesseract as pt
import subprocess

image = cv2.imread('/home/pykid/Desktop/paper.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
text = input('Find text you wish you search: ')
img_2_text = pt.image_to_string(image)
if text in img_2_text:
    print(f'{text} Found')
else:
    print('Sorry not found')

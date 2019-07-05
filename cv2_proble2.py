#!/usr/bin/python3
import cv2
import numpy as np

# loading image
image = cv2.imread('/home/pykid/Desktop/test1.jpeg',1)
imagex = cv2.imread('/home/pykid/Desktop/test2.jpeg')

# merging the two images
merging = np.concatenate((image,imagex),axis=1)
cv2.imshow('merged image',merging)

# printing the shape
print(image.shape)

def CallBackFunc(event,x,y,flags,params):
    # on hovering it collects the position of mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f" left button of mouse - position ({x},{y})")
        printx(x,y)

def printx(a,b):
    crop_img = image[a-20:a+20,b:b+40] # cropping a part of image based on mouse click
    image1 = cv2.resize(crop_img,(500,500),fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
    cv2.imshow('zoomed',image1)

cv2.imshow('original image',image)
cv2.setMouseCallback('original image',CallBackFunc)
cv2.waitKey(0)
cv2.destroyAllWindows()

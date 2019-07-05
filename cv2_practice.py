#!/usr/bin/python3
import cv2
import numpy as np
image = cv2.imread('/home/pykid/Desktop/test1.jpeg')
image1 = cv2.imread('/home/pykid/Desktop/test2.jpeg')
output1 = cv2.add(image1,image)

cv2.imshow('a',output1)
cv2.waitKey(0)
cv2.destroyAllWindows()


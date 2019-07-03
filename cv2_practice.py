#!/usr/bin/python3
import cv2
import numpy as np
a = np.ones(480*640*3).reshape(480,640,3)

cv2.imshow('a',a)
print(a.shape)
cv2.imwrite('/home/pykid/Desktop/test1.jpeg',a[0][0]+60)
cv2.imshow('window1',a[0][0]+160)
cv2.waitKey(10000)
cv2.destroyAllWindows()


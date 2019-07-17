import cv2
import numpy as np

image1 = cv2.imread('/home/pykid/Desktop/test1.jpeg')

image2 = cv2.imread('/home/pykid/Desktop/test2.jpeg')

image3 = image2.copy()

# difference is of 2 types
# absolute difference and subtract
# | x - y |                x - y
difference = cv2.absdiff(image2,image1)
subtract = cv2.subtract(image1,image2)


cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.imshow('difference',difference)
cv2.imshow('subtrcat',subtract)

# making a single image by adding two images
output = np.concatenate((image3,image2),axis=1)
cv2.imshow('added two images',output)

cv2.waitKey(0)
cv2.destroyAllWindows()


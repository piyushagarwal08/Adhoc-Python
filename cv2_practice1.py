#!/usr/bin/python3
import cv2
image = cv2.imread('/home/pykid/Downloads/image3')   # loading image

#row = love.shape[0]     # finding the no of rows in image
#column = love.shape[1]  # finding the no of columns in image

rows = int(input('Enter the row size you prefer: '))    # users preference of rows  
columns = int(input('Enter the column size you prefer: '))  #users preference of columns

print(image.shape[0]/rows)  # calculates the fx value
y_ratio = image.shape[1]/columns  # calculates the fy value

#output = cv2.resize(image,None,fx=x_ratio,fy=y_ratio,interpolation=cv2.INTER_AREA)
#cv2.imshow('window1',output)
#cv2.waitKey(5000)

#cv2.destroyWindow('window1')

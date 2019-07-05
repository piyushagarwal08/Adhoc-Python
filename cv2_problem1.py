import cv2

# reading image data
image1 = cv2.imread('/home/pykid/Desktop/test1.jpeg')
image2 = cv2.imread('/home/pykid/Desktop/test2.jpeg')


# finding head of character
head1 = image1[32:132,26:136] # (100,110)
head2 = image2[26:126,29:139] # (100,110)

# replacing the heads of both characters 
image1[32:132,26:136] = image2[26:126,29:139]
image2[26:126,29:139] = head1

# display the actual image
cv2.rectangle(image2,(24,48),(121,123),(0,0,243),2)
cv2.rectangle(image1,(37,29),(136,139),(0,255,0),2)
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)

cv2.waitKey(0)

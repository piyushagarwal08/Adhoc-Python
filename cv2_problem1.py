import cv2

# reading image data
image1 = cv2.imread('/home/pykid/Desktop/test1.jpeg')
image2 = cv2.imread('/home/pykid/Desktop/test2.jpeg')


# finding head of character
head1 = image1[32:132,26:136].copy() # (100,110)
head2 = image2[26:126,29:139].copy() # (100,110)

# replacing the heads of both characters 
image1[32:132,26:136] = head2
image2[26:126,29:139] = head1

# display the altered image
cv2.imshow('image1',image1)
cv2.imshow('image2',image2)

# replacing some 10 rows and 20 columns of image2 with that of image 1
image2[40:50,134:154] = image1[87:97,27:47].copy()
cv2.imshow('random',image2)


cv2.waitKey(0)
cv2.destroyAllWindows()

import nltk
import cv2
import pytesseract as pt

# attaching my phone camera
#cap = cv2.VideoCapture(0)
#status,image1 = cap.read()

# loading image of newspaper
image1 = cv2.imread('/home/pykid/Desktop/paper.png')
#image1 = cv2.resize(image1,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_LINEAR)

text = pt.image_to_string(image1)
print(len(text))
with open('/home/pykid/Desktop/file1.txt','w+') as file:
    file.write(text)

cv2.imshow('image1',image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

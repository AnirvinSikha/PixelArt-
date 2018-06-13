import numpy as np
import matplotlib 
import cv2




def pixelize():
    return
img = cv2.imread('/Users/asikha/Desktop/poppies.jpg',1)
#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

height, width = img.shape[:2]

#img = cv2.resize(img, (100, 100))
print (img.mean())

#h, w = img.shape[:2]
#for j in range(h):
#    for k in range(w):




cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np 
import cv2

img=cv2.imread('lenna.jpg')
img1=img[0:500,0:500]
img=cv2.imread('opencv-logo.jpg')
img2=img[0:500,0:500]
dst=cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
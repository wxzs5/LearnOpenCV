import cv2
import numpy as np 

im = cv2.imread('../../img/test.png')
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

##Draw all contours in an image
cv2.drawContours(im2,contours,-1,(0,255,0),3)
##Draw an individual contour
# cv2.drawContours(im2,contours,3,(0,255,0),3)
# ##Most useful method
# cnt=contours[4]
# cv2.drawContours(im2,[cnt],0,(0,255,0),3)


cv2.imshow('im2',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()


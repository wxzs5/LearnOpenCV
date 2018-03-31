import cv2 as cv
import numpy as np 

im = cv.imread('../../img/test.png')
imgray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,127,255,0)
im2,contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

##Draw all contours in an image
cv.drawContours(im2,contours,-1,(0,255,0),3)
##Draw an individual contour
# cv.drawContours(im2,contours,3,(0,255,0),3)
# ##Most useful method
# cnt=contours[4]
# cv.drawContours(im2,[cnt],0,(0,255,0),3)


cv.imshow('im2',im2)
cv.waitKey(0)
cv.destroyAllWindows()


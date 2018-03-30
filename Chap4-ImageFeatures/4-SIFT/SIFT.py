import cv2 as cv
import numpy as np


img = cv.imread('../../img/home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

##### First way
sift = cv.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
# ##### Second way
# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)

img=cv.drawKeypoints(gray,kp,img)

cv.imshow('sift_keypoints.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

img = cv.imread('../../img/lenna.jpg')
img1 = img[0:500, 0:500]
img = cv.imread('opencv-logo.jpg')
img2 = img[0:500, 0:500]
dst = cv.addWeighted(img1, 0.8, img2, 0.2, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()

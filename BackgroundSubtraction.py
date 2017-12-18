##### These methods are just suitable for static background images

import numpy as np
import cv2 as cv  
cap = cv.VideoCapture('res/vtest.avi')  #temporarily,the test video from PETS are not available

# ##### BackgroundSubtractorMOG
# fgbg = cv.createBackgroundSubtractorMOG()
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv.imshow('frame',fgmask)
#     k = cv.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv.destroyAllWindows()

# ##### BackgroundSubtractorMOG2
# fgbg = cv.createBackgroundSubtractorMOG2()
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv.imshow('frame',fgmask)
#     k = cv.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv.destroyAllWindows()

##### BackgroundSubtractorGMG
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
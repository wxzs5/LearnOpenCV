# These methods are just suitable for static background images

########################################################################
# BackgroundSubtractorMOG
########################################################################
# import numpy as np
# import cv2 as cv
# # temporarily,the test video from PETS are not available
# cap = cv.VideoCapture('../../img/vtest.avi')

# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()  # BUG
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv.imshow('frame', fgmask)
#     k = cv.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv.destroyAllWindows()

########################################################################
# BackgroundSubtractorMOG2
########################################################################
# import numpy as np
# import cv2 as cv
# # temporarily,the test video from PETS are not available
# cap = cv.VideoCapture('../../img/vtest.avi')

# fgbg = cv.createBackgroundSubtractorMOG2()
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv.imshow('frame', fgmask)
#     k = cv.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv.destroyAllWindows()

########################################################################
# BackgroundSubtractorGMG
########################################################################
import numpy as np
import cv2 as cv
# temporarily,the test video from PETS are not available
cap = cv.VideoCapture('../../img/vtest.avi')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()  # BUG
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow('frame', fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

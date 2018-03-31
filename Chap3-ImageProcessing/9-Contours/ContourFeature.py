# #####Calculate Image Moments
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv.imread('../../img/j.png',0)
# ret,thresh=cv.threshold(img,127,255,0)
# im2,contours,hierarchy=cv.findContours(thresh,1,2)

# cnt=contours[0]
# M=cv.moments(cnt)
# print(M)

# cx=int(M['m10']/M['m00'])
# cy=int(M['m01']/M['m00'])
# print(cx)
# print(cy)

# #####Contour Area
# area=cv.contour(cnt)

# #####Convexity Defects
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv.imread('../../img/j.png')
# img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,thresh=cv.threshold(img_gray,127,255,0)
# im2,contours,hierarchy=cv.findContours(thresh,2,1)
# cnt = contours[0]

# hull=cv.convexHull(cnt,returnPoints=False)
# defects=cv.convexityDefects(cnt,hull)

# for i in range(defects.shape[0]):
#     s,e,f,d=defects[i,0]
#     start=tuple(cnt[s][0])
#     end=tuple(cnt[e][0])
#     far=tuple(cnt[f][0])
#     cv.line(img,start,end,[0,255,0],2)
#     cv.circle(img,far,5,[0,0.255])

# cv.imshow('img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#####Matching shapes
import cv2 as cv
import numpy as np
img1 = cv.imread('../../img/j.png',0)
img2 = cv.imread('../../img/jopen.png',0)
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
im2,contours,hierarchy = cv.findContours(thresh,2,1)
cnt1 = contours[0]
im2,contours,hierarchy = cv.findContours(thresh2,2,1)
cnt2 = contours[0]
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print(ret)



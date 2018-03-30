# #####Calculate Image Moments
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv2.imread('../../img/j.png',0)
# ret,thresh=cv2.threshold(img,127,255,0)
# im2,contours,hierarchy=cv2.findContours(thresh,1,2)

# cnt=contours[0]
# M=cv2.moments(cnt)
# print(M)

# cx=int(M['m10']/M['m00'])
# cy=int(M['m01']/M['m00'])
# print(cx)
# print(cy)

# #####Contour Area
# area=cv2.contour(cnt)

# #####Convexity Defects
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv2.imread('../../img/j.png')
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(img_gray,127,255,0)
# im2,contours,hierarchy=cv2.findContours(thresh,2,1)
# cnt = contours[0]

# hull=cv2.convexHull(cnt,returnPoints=False)
# defects=cv2.convexityDefects(cnt,hull)

# for i in range(defects.shape[0]):
#     s,e,f,d=defects[i,0]
#     start=tuple(cnt[s][0])
#     end=tuple(cnt[e][0])
#     far=tuple(cnt[f][0])
#     cv2.line(img,start,end,[0,255,0],2)
#     cv2.circle(img,far,5,[0,0.255])

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#####Matching shapes
import cv2
import numpy as np
img1 = cv2.imread('../../img/j.png',0)
img2 = cv2.imread('../../img/jopen.png',0)
ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
im2,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
im2,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)


